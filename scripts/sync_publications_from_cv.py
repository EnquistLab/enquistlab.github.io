#!/usr/bin/env python3
"""
sync_publications_from_cv.py
----------------------------
Reads the synced CV text (assets/cv/google_doc_cv_latest.txt), extracts DOIs,
fetches BibTeX from CrossRef for any DOI not already in _bibliography/papers.bib,
and appends new entries.  The bib.liquid template renders the `doi` field as a
title hotlink automatically (https://doi.org/<doi>).

Usage (from repo root):
    python scripts/sync_publications_from_cv.py

Exits 0 always; prints a summary of new entries added.
"""

import re
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
import os
from typing import Optional

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CV_TEXT   = os.path.join(REPO_ROOT, "assets", "cv", "google_doc_cv_latest.txt")
BIB_FILE  = os.path.join(REPO_ROOT, "_bibliography", "papers.bib")

CROSSREF_BIBTEX = "https://api.crossref.org/works/{doi}/transform/application/x-bibtex"
# Polite-pool: identify ourselves so CrossRef queues us separately from anonymous traffic
MAILTO = "benquist@arizona.edu"


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def extract_dois_from_cv(path: str) -> list[str]:
    """Return a de-duplicated, ordered list of DOIs found in the CV text."""
    text = open(path, encoding="utf-8", errors="replace").read()
    # Match 10.XXXX/... patterns, allow trailing chars up to whitespace/comma/paren
    raw = re.findall(r'\b(10\.\d{4,9}/[^\s,;\)\]\"\'<>]+)', text)
    # Clean trailing punctuation that isn't part of the DOI
    cleaned = [re.sub(r'[.,;)\]]+$', '', d) for d in raw]
    seen: set[str] = set()
    out: list[str] = []
    for d in cleaned:
        key = d.lower()
        if key not in seen:
            seen.add(key)
            out.append(d)
    return out


def existing_dois_in_bib(path: str) -> set[str]:
    """Return lower-cased DOIs already present in papers.bib."""
    if not os.path.exists(path):
        return set()
    text = open(path, encoding="utf-8", errors="replace").read()
    return {d.lower() for d in re.findall(r'doi\s*=\s*\{([^}]+)\}', text, re.IGNORECASE)}


def fetch_bibtex(doi: str) -> Optional[str]:
    """Fetch BibTeX for a DOI from CrossRef.  Returns None on any failure."""
    url = CROSSREF_BIBTEX.format(doi=urllib.parse.quote(doi, safe="/:@"))
    req = urllib.request.Request(
        url,
        headers={"User-Agent": f"sync_publications_from_cv/1.0 (mailto:{MAILTO})"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        print(f"  [skip] CrossRef HTTP {e.code} for {doi}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  [skip] fetch error for {doi}: {e}", file=sys.stderr)
        return None


def ensure_doi_field(bibtex: str, doi: str) -> str:
    """
    Ensure the BibTeX entry has a `doi` field so bib.liquid renders a title link.
    CrossRef usually includes it; add it explicitly if absent.
    """
    if re.search(r'\bdoi\s*=', bibtex, re.IGNORECASE):
        return bibtex
    # Insert doi field before the closing brace
    return re.sub(r'\}\s*$', f'  doi = {{{doi}}},\n}}', bibtex.rstrip())


def make_cite_key(bibtex: str, doi: str) -> str:  # noqa: F841
    """Return the cite key from a BibTeX entry, or a doi-derived fallback."""
    m = re.match(r'@\w+\{([^,]+),', bibtex)
    if m:
        return m.group(1).strip()
    return "doi_" + re.sub(r'[^a-z0-9]', '_', doi.lower())


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> None:
    if not os.path.exists(CV_TEXT):
        print(f"CV text not found at {CV_TEXT}; nothing to do.")
        return

    cv_dois   = extract_dois_from_cv(CV_TEXT)
    known     = existing_dois_in_bib(BIB_FILE)
    new_dois  = [d for d in cv_dois if d.lower() not in known]

    print(f"CV DOIs found   : {len(cv_dois)}")
    print(f"Already in .bib : {len(known)}")
    print(f"New to fetch    : {len(new_dois)}")

    if not new_dois:
        print("No new publications to add.")
        return

    added = 0
    with open(BIB_FILE, "a", encoding="utf-8") as fh:
        for doi in new_dois:
            print(f"  Fetching {doi} …")
            bib = fetch_bibtex(doi)
            if bib is None:
                continue
            bib = ensure_doi_field(bib, doi)
            fh.write("\n" + bib.strip() + "\n")
            added += 1
            time.sleep(0.5)   # be polite to CrossRef

    print(f"\nDone — {added} new entr{'y' if added == 1 else 'ies'} added to papers.bib.")


if __name__ == "__main__":
    main()
