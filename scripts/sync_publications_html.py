#!/usr/bin/env python3
"""
sync_publications_html.py

Reads the Google Doc CV text, parses the peer-reviewed publications section,
then cross-checks against _includes/publications_full_from_doc.md to:
  1. Detect papers present in CV but missing from the HTML.
  2. Detect "In Press" entries in HTML that now have volume/page data in the CV.
  3. Verify all DOIs found in the CV against the CrossRef API.

Writes an updated publications HTML (if In Press patches are found) and a
plain-text report to assets/cv/publications_sync_report.txt.

Always exits 0 so the GitHub Actions workflow never fails on partial results.
"""

import os
import re
import sys
import time
import datetime
import urllib.request
import urllib.error
import json

# ---------------------------------------------------------------------------
# Paths (relative to repo root, which is the cwd in CI)
# ---------------------------------------------------------------------------
CV_TXT      = "assets/cv/google_doc_cv_latest.txt"
PUBS_HTML   = "_includes/publications_full_from_doc.md"
REPORT_OUT  = "assets/cv/publications_sync_report.txt"
GDOC_URL    = (
    "https://docs.google.com/document/d/"
    "1OMolpDfY6c73qRgUFgYh0XbMS8EykUoy_hvrI8fnTn0/export?format=txt"
)
CROSSREF_UA = "sync_publications_html/1.0 (mailto:benquist@arizona.edu)"
CROSSREF_SLEEP = 0.3  # seconds between API calls

# CrossRef API base
CROSSREF_API = "https://api.crossref.org/works/{doi}"

# ---------------------------------------------------------------------------
# Regex helpers
# ---------------------------------------------------------------------------
DOI_RE   = re.compile(r'10\.\d{4,9}/\S+')
URL_RE   = re.compile(r'https?://\S+')
YEAR_RE  = re.compile(r'^\s*((?:19|20)\d{2})\s*$')
ENTRY_RE = re.compile(r'^\s*(\d+)\.\s+(.+)$', re.DOTALL)

# Matches volume/page patterns like "17, 3623" or "122(26)" or "00, 1–29"
VOL_PAGE_RE = re.compile(
    r'\b\d{1,4}(?:\(\d+\))?,\s*[\d–\-]+|'  # "17, 3623" or "122(26), 1-10"
    r'\b\d{1,4}\(\d+\)'                     # "122(26)" alone
)

INPRESS_RE = re.compile(r'\bIn\s+[Pp]ress\b')


# ---------------------------------------------------------------------------
# Step 1: Load CV text
# ---------------------------------------------------------------------------
def load_cv_text() -> str:
    if os.path.exists(CV_TXT):
        print(f"[cv] Reading CV from {CV_TXT}")
        with open(CV_TXT, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    print(f"[cv] {CV_TXT} not found — downloading from Google Docs …")
    try:
        req = urllib.request.Request(GDOC_URL, headers={"User-Agent": CROSSREF_UA})
        with urllib.request.urlopen(req, timeout=30) as resp:
            text = resp.read().decode("utf-8", errors="replace")
        os.makedirs(os.path.dirname(CV_TXT), exist_ok=True)
        with open(CV_TXT, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"[cv] Saved to {CV_TXT}")
        return text
    except Exception as exc:
        print(f"[cv] ERROR downloading CV: {exc}")
        return ""


# ---------------------------------------------------------------------------
# Step 2: Parse peer-reviewed publications section from CV text
# ---------------------------------------------------------------------------
def parse_cv_publications(cv_text: str) -> list[dict]:
    """
    Returns a list of dicts, one per publication entry:
      {year, number, raw_text, doi, url}
    """
    # Locate section boundaries (section headers are approximate)
    section_start = re.search(
        r'Peer Reviewed Journal\s+Ar[ti]+cles', cv_text, re.IGNORECASE
    )
    section_end = re.search(
        r'Other Publications', cv_text, re.IGNORECASE
    )

    if not section_start:
        print("[parse] WARNING: Could not find 'Peer Reviewed Journal Articles' section.")
        return []

    start_pos = section_start.end()
    end_pos   = section_end.start() if section_end else len(cv_text)
    section   = cv_text[start_pos:end_pos]

    entries  = []
    cur_year = None

    # Buffer multi-line entries: collect lines until we hit a new numbered entry
    # or a year header
    pending_num  = None
    pending_text = []

    def flush(num, lines, year):
        if num is None or not lines:
            return
        raw = " ".join(lines).strip()
        doi_m = DOI_RE.search(raw)
        url_m = URL_RE.search(raw)
        entries.append({
            "year":     year,
            "number":   num,
            "raw_text": raw,
            "doi":      doi_m.group(0).rstrip(".,;)") if doi_m else None,
            "url":      url_m.group(0).rstrip(".,;)") if url_m else None,
        })

    for line in section.splitlines():
        year_m  = YEAR_RE.match(line)
        entry_m = ENTRY_RE.match(line)

        if year_m:
            flush(pending_num, pending_text, cur_year)
            pending_num, pending_text = None, []
            cur_year = int(year_m.group(1))
        elif entry_m:
            flush(pending_num, pending_text, cur_year)
            pending_num  = int(entry_m.group(1))
            pending_text = [entry_m.group(2).strip()]
        elif pending_num is not None and line.strip():
            pending_text.append(line.strip())

    flush(pending_num, pending_text, cur_year)
    print(f"[parse] Found {len(entries)} entries in CV peer-reviewed section.")
    return entries


# ---------------------------------------------------------------------------
# Step 3: Load HTML publications file
# ---------------------------------------------------------------------------
def load_pubs_html() -> str:
    if not os.path.exists(PUBS_HTML):
        print(f"[html] ERROR: {PUBS_HTML} not found.")
        return ""
    with open(PUBS_HTML, encoding="utf-8") as fh:
        return fh.read()


# ---------------------------------------------------------------------------
# Step 4: Extract a searchable title fragment from a raw CV entry string
# ---------------------------------------------------------------------------
def title_fragment(raw_text: str, chars: int = 40) -> str:
    """
    Strip leading author/year preamble and return the first `chars` chars
    of the title, lowercased, for fuzzy matching.
    """
    # Remove leading author block heuristically:
    # Pattern: "Surname, I., ... (YYYY). Title starts here"
    m = re.search(r'\(\d{4}\)[.\s]+(.+)', raw_text)
    if m:
        title = m.group(1).strip()
    else:
        # Fallback: just skip to after the first ". " sequence
        parts = raw_text.split('. ', 2)
        title = parts[-1] if len(parts) >= 2 else raw_text

    # Strip markdown/html artifacts and normalise whitespace
    title = re.sub(r'<[^>]+>', '', title)
    title = re.sub(r'\s+', ' ', title).strip()
    return title[:chars].lower()


# ---------------------------------------------------------------------------
# Step 5: Determine if a CV entry has volume/page info (i.e. it is published)
# ---------------------------------------------------------------------------
def has_vol_page(raw_text: str) -> bool:
    """
    Returns True if the entry text contains a volume/page pattern that
    indicates a paper has been assigned a volume and page (i.e. published).
    """
    return bool(VOL_PAGE_RE.search(raw_text))


# ---------------------------------------------------------------------------
# Step 6: CrossRef DOI verification
# ---------------------------------------------------------------------------
def verify_doi(doi: str) -> tuple[bool, str]:
    """
    Returns (valid: bool, message: str).
    Uses the CrossRef works API with a polite User-Agent.
    """
    url = CROSSREF_API.format(doi=urllib.parse.quote(doi, safe='/()+'))
    req = urllib.request.Request(url, headers={"User-Agent": CROSSREF_UA})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status == 200:
                return True, "OK"
            return False, f"HTTP {resp.status}"
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return False, "404 Not Found"
        return False, f"HTTP {exc.code}"
    except Exception as exc:
        return False, f"Error: {exc}"


# Make urllib.parse available (it's in stdlib but needs explicit import)
import urllib.parse


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    report_lines = []
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    report_lines.append(f"Publications Sync Report — {timestamp}")
    report_lines.append("=" * 60)

    # Load inputs
    cv_text   = load_cv_text()
    pubs_html = load_pubs_html()

    if not cv_text or not pubs_html:
        report_lines.append("FATAL: Could not load CV text or publications HTML. Aborting.")
        _write_report(report_lines)
        return

    cv_entries = parse_cv_publications(cv_text)

    # Track outcomes
    missing_from_html  = []   # (entry) present in CV but not HTML
    inpress_to_update  = []   # (entry, li_fragment, new_li) In Press → published
    doi_ok_count       = 0
    doi_failures       = []   # (doi, message)

    # Build working copy of HTML for patching
    html_updated = pubs_html

    # -----------------------------------------------------------------------
    # 4a/4b/4c: Cross-check each CV entry
    # -----------------------------------------------------------------------
    for entry in cv_entries:
        frag = title_fragment(entry["raw_text"])
        if not frag:
            continue

        in_html = frag in pubs_html.lower()

        if not in_html:
            missing_from_html.append(entry)
            continue

        # Paper is in HTML — check if HTML still says In Press while CV is published
        if has_vol_page(entry["raw_text"]):
            # Find the matching <li> in HTML
            li_match = _find_li_containing(pubs_html, frag)
            if li_match and INPRESS_RE.search(li_match):
                # Extract the published journal info from CV entry to build replacement
                new_li = _patch_inpress_li(li_match, entry["raw_text"])
                if new_li and new_li != li_match:
                    inpress_to_update.append((entry, li_match, new_li))
                    html_updated = html_updated.replace(li_match, new_li, 1)

    # -----------------------------------------------------------------------
    # 5: DOI verification
    # -----------------------------------------------------------------------
    all_dois = []
    seen_dois = set()
    for entry in cv_entries:
        doi = entry.get("doi")
        if doi and doi not in seen_dois:
            seen_dois.add(doi)
            all_dois.append((entry, doi))

    print(f"[doi] Verifying {len(all_dois)} unique DOIs …")
    for entry, doi in all_dois:
        # Flag potentially anomalous DOIs before hitting the API
        anomaly_note = ""
        if re.search(r'/s\d+-\d{3}-\d+', doi):
            # Pattern like s41467-026-69952-6: "026" in middle segment is unusual
            parts = doi.split('-')
            for i, p in enumerate(parts):
                if re.match(r'^0\d{2}$', p):
                    anomaly_note = (
                        f" [NOTE: segment '{p}' in DOI looks anomalous — "
                        f"possibly a year-style typo for a 2-digit volume number]"
                    )

        valid, msg = verify_doi(doi)
        time.sleep(CROSSREF_SLEEP)

        if valid:
            doi_ok_count += 1
            if anomaly_note:
                doi_failures.append((doi, f"Resolves OK but flagged: {anomaly_note.strip()}"))
        else:
            doi_failures.append((doi, msg + anomaly_note))

    # -----------------------------------------------------------------------
    # Write updated HTML if patches were applied
    # -----------------------------------------------------------------------
    if inpress_to_update:
        with open(PUBS_HTML, "w", encoding="utf-8") as fh:
            fh.write(html_updated)
        print(f"[html] Wrote updated {PUBS_HTML} ({len(inpress_to_update)} In Press patch(es)).")
    else:
        print("[html] No In Press → published updates needed.")

    # -----------------------------------------------------------------------
    # Build report
    # -----------------------------------------------------------------------
    report_lines.append("")
    report_lines.append(f"CV entries parsed: {len(cv_entries)}")
    report_lines.append(f"In Press → published patches applied: {len(inpress_to_update)}")
    report_lines.append(f"DOIs verified OK: {doi_ok_count}")
    report_lines.append(f"DOI failures / anomalies: {len(doi_failures)}")
    report_lines.append(f"Papers in CV but NOT found in HTML: {len(missing_from_html)}")

    if inpress_to_update:
        report_lines.append("")
        report_lines.append("IN PRESS → PUBLISHED UPDATES")
        report_lines.append("-" * 40)
        for entry, old_li, new_li in inpress_to_update:
            report_lines.append(f"  Year {entry['year']} entry #{entry['number']}:")
            report_lines.append(f"    Old: {old_li[:120].strip()} …")
            report_lines.append(f"    New: {new_li[:120].strip()} …")

    if missing_from_html:
        report_lines.append("")
        report_lines.append("MISSING FROM WEBSITE HTML (in CV but not found in _includes/publications_full_from_doc.md)")
        report_lines.append("-" * 40)
        for entry in missing_from_html:
            snippet = entry["raw_text"][:140].strip()
            report_lines.append(f"  [{entry['year']} #{entry['number']}] {snippet} …")

    if doi_failures:
        report_lines.append("")
        report_lines.append("DOI FAILURES / ANOMALIES")
        report_lines.append("-" * 40)
        for doi, msg in doi_failures:
            report_lines.append(f"  {doi}  →  {msg}")

    report_lines.append("")
    report_lines.append("END OF REPORT")

    _write_report(report_lines)
    print(f"[report] Written to {REPORT_OUT}")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _find_li_containing(html: str, frag: str) -> str | None:
    """Return the full <li>…</li> string that contains frag (case-insensitive)."""
    html_lower = html.lower()
    idx = html_lower.find(frag)
    if idx == -1:
        return None
    # Walk backward to find opening <li>
    start = html_lower.rfind('<li>', 0, idx)
    if start == -1:
        return None
    # Walk forward to find closing </li>
    end = html_lower.find('</li>', idx)
    if end == -1:
        return None
    return html[start:end + 5]  # include "</li>"


def _patch_inpress_li(li: str, cv_raw: str) -> str:
    """
    Replace the In Press status text in `li` with the published journal
    info extracted from cv_raw.  Returns patched li, or original on failure.
    """
    # Extract the journal name + volume/page from the CV entry.
    # Pattern: after the last (YYYY). block, find "Journal. Vol, page"
    # We look for text after the year marker up to (but not including) any URL/DOI.
    after_year = re.search(r'\(\d{4}\)[.\s]+.+', cv_raw, re.DOTALL)
    if not after_year:
        return li

    pub_part = after_year.group(0)
    # Remove DOI/URL tail
    pub_part = re.split(r'https?://', pub_part)[0]
    pub_part = re.split(r'\b10\.\d{4,9}/', pub_part)[0]
    pub_part = pub_part.strip().rstrip('.,;')

    # Extract just the journal info: everything after the title.
    # Heuristic: the title ends at the first ". " that is followed by
    # something that looks like a journal/volume pattern.
    # Simpler: find the vol/page match and grab back to preceding ". "
    vol_m = VOL_PAGE_RE.search(pub_part)
    if not vol_m:
        return li

    # Take from the previous ". " before the vol/page match
    before_vol = pub_part[:vol_m.start()]
    journal_start = before_vol.rfind('. ')
    if journal_start == -1:
        journal_start = before_vol.rfind('. ')
    journal_bit = (before_vol[journal_start + 2:] + pub_part[vol_m.start():]).strip()
    journal_bit = journal_bit.rstrip('.,;').strip()

    if not journal_bit:
        return li

    # Replace "In Press" (and any surrounding whitespace) in the <li>
    # with the resolved journal + volume/page string.
    patched = INPRESS_RE.sub(journal_bit, li)
    return patched


def _write_report(lines: list[str]) -> None:
    os.makedirs(os.path.dirname(REPORT_OUT), exist_ok=True)
    with open(REPORT_OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[ERROR] Unhandled exception: {exc}")
        import traceback
        traceback.print_exc()
    sys.exit(0)
