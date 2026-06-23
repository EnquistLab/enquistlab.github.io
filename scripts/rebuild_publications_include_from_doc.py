#!/usr/bin/env python3
"""
Rebuild the publications include from the current cleaned include plus the
public Google Doc HTML export.

This script fixes two recurring drift problems:
1. Items can sit under the wrong year block if the Google Doc year heading
   formatting changes.
2. New items can appear in the public Google Doc but not in the website include.

The strategy is conservative:
- Start from the existing cleaned website include.
- Reassign each existing <li> to the year inferred from the citation text.
- Parse the public Google Doc HTML export, clean the anchor URLs, and add any
  missing items by year.
- Render a normalized include with one explicit year block per inferred year.
"""

import re
import urllib.parse
import urllib.request
from collections import OrderedDict
from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path


DOC_ID = "1OMolpDfY6c73qRgUFgYh0XbMS8EykUoy_hvrI8fnTn0"
DOC_HTML_URL = f"https://docs.google.com/document/d/{DOC_ID}/export?format=html"
PUBS_HTML = Path("_includes/publications_full_from_doc.md")
SECTION_LABEL = "Peer Reviewed Journal Aricles"
SECTION_END_LABELS = (
    "Other Publications",
    "Book Chapters",
    "Books",
)

SECTION_RE = re.compile(r"<p>\s*([^<]+?)\s*</p><ol>(.*?)</ol>", re.IGNORECASE | re.DOTALL)
LI_RE = re.compile(r"<li>.*?</li>", re.IGNORECASE | re.DOTALL)
YEAR_RE = re.compile(r"\((19|20)\d{2}\)|\b(19|20)\d{2}\b")
HREF_RE = re.compile(r'href="([^"]+)"', re.IGNORECASE)
DOI_RE = re.compile(r'10\.\d{4,9}/[^\s"<>]+', re.IGNORECASE)


def normalize_doi(raw_doi):
    doi = (raw_doi or "").strip().lower()
    if not doi:
        return ""
    doi = re.sub(r"[?#].*$", "", doi)
    doi = doi.rstrip(').,;]"\'')
    return doi


def clean_google_href(href):
    href = unescape(href or "").strip()
    parsed = urllib.parse.urlparse(href)
    if parsed.netloc.endswith("google.com") and parsed.path == "/url":
        q = urllib.parse.parse_qs(parsed.query).get("q")
        if q:
            return q[0]
    return href


def strip_tags(html_text):
    text = re.sub(r"<[^>]+>", "", html_text)
    text = text.replace("\xa0", " ")
    return re.sub(r"\s+", " ", unescape(text)).strip()


def infer_year(html_text):
    text = strip_tags(html_text)
    match = YEAR_RE.search(text)
    if not match:
        return None
    year_text = match.group(0).strip("()")
    return int(year_text)


def title_key(html_text):
    text = strip_tags(html_text)
    match = re.search(r"\(\d{4}\)[.\s]+(.+)", text)
    if match:
        text = match.group(1)
    text = re.sub(r"\bfrontiers in ecology and the environment\b.*$", "", text, flags=re.IGNORECASE)
    text = re.sub(r"[^a-z0-9]+", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()[:160]


def item_identity_key(html_text):
    urls = [clean_google_href(url) for url in HREF_RE.findall(html_text)]

    doi_candidates = []
    for url in urls:
        doi_match = DOI_RE.search(url)
        if doi_match:
            normalized = normalize_doi(doi_match.group(0))
            if normalized:
                doi_candidates.append(normalized)

    if not doi_candidates:
        text_doi_match = DOI_RE.search(strip_tags(html_text))
        if text_doi_match:
            normalized = normalize_doi(text_doi_match.group(0))
            if normalized:
                doi_candidates.append(normalized)

    if doi_candidates:
        # Use one canonical DOI token to avoid split identities for link/query variants.
        return "doi:" + sorted(set(doi_candidates))[0]

    clean_urls = sorted({url for url in urls if url})
    if clean_urls:
        return "url:" + "|".join(clean_urls)

    return "title:" + title_key(html_text)


def normalize_li(html_text):
    html_text = html_text.replace("\xa0", " ")
    html_text = re.sub(r"\s+", " ", html_text)
    html_text = re.sub(r">\s+", ">", html_text)
    html_text = re.sub(r"\s+<", "<", html_text)
    html_text = re.sub(r"\s+([,.;:)])", r"\1", html_text)
    html_text = re.sub(r"([(" + "\[] )\s+", r"\1", html_text)
    return html_text.strip()


class DocPublicationParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items = []
        self.in_li = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == "li":
            self.in_li = True
            self.parts = []
            return

        if self.in_li and tag == "a":
            attr_map = dict(attrs)
            href = clean_google_href(attr_map.get("href", ""))
            self.parts.append(
                '<a href="{}" target="_blank" rel="noopener noreferrer">'.format(
                    escape(href, quote=True)
                )
            )

    def handle_endtag(self, tag):
        if self.in_li and tag == "a":
            self.parts.append("</a>")
            return

        if tag == "li" and self.in_li:
            item = normalize_li("<li>" + "".join(self.parts) + "</li>")
            if strip_tags(item):
                self.items.append(item)
            self.in_li = False
            self.parts = []

    def handle_data(self, data):
        if self.in_li:
            self.parts.append(escape(data, quote=False))

    def handle_entityref(self, name):
        if self.in_li:
            self.parts.append(escape(unescape(f"&{name};"), quote=False))

    def handle_charref(self, name):
        if self.in_li:
            self.parts.append(escape(unescape(f"&#{name};"), quote=False))


def load_doc_html():
    req = urllib.request.Request(DOC_HTML_URL, headers={"User-Agent": "publications-include-sync/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def extract_doc_section(doc_html):
    start = doc_html.find(SECTION_LABEL)
    if start == -1:
        raise RuntimeError(f"Could not find section label: {SECTION_LABEL}")

    end_candidates = [doc_html.find(label, start + len(SECTION_LABEL)) for label in SECTION_END_LABELS]
    end_candidates = [idx for idx in end_candidates if idx != -1]
    end = min(end_candidates) if end_candidates else len(doc_html)
    return doc_html[start:end]


def parse_doc_items_by_year(doc_html):
    parser = DocPublicationParser()
    parser.feed(extract_doc_section(doc_html))

    items_by_year = OrderedDict()
    keys_by_year = {}
    titles_by_year = {}
    for item in parser.items:
        year = infer_year(item)
        if year is None:
            continue
        key = item_identity_key(item)
        tkey = title_key(item)
        if year not in items_by_year:
            items_by_year[year] = []
            keys_by_year[year] = set()
            titles_by_year[year] = set()
        if key not in keys_by_year[year] and (not tkey or tkey not in titles_by_year[year]):
            items_by_year[year].append(item)
            keys_by_year[year].add(key)
            if tkey:
                titles_by_year[year].add(tkey)
    return items_by_year


def parse_existing_include(include_text):
    items_by_year = OrderedDict()
    keys_by_year = {}
    titles_by_year = {}

    for match in SECTION_RE.finditer(include_text):
        section_year = match.group(1).strip()
        body = match.group(2)
        for li_match in LI_RE.finditer(body):
            item = normalize_li(li_match.group(0))
            inferred = infer_year(item)
            if inferred is None:
                try:
                    inferred = int(section_year)
                except ValueError:
                    continue
            key = item_identity_key(item)
            tkey = title_key(item)
            if inferred not in items_by_year:
                items_by_year[inferred] = []
                keys_by_year[inferred] = set()
                titles_by_year[inferred] = set()
            if key not in keys_by_year[inferred] and (not tkey or tkey not in titles_by_year[inferred]):
                items_by_year[inferred].append(item)
                keys_by_year[inferred].add(key)
                if tkey:
                    titles_by_year[inferred].add(tkey)
    return items_by_year, keys_by_year


def render_include(items_by_year):
    ordered_years = sorted(items_by_year.keys(), reverse=True)
    lines = [
        "<!-- Auto-generated from shared Google Doc: peer-reviewed publication section -->",
        f"<p>{SECTION_LABEL}</p>",
    ]
    for year in ordered_years:
        items = "".join(items_by_year[year])
        lines.append(f"<p>{year}</p><ol>{items}</ol>")
    return "\n".join(lines) + "\n"


def dedupe_items_by_title(items_by_year):
    """Remove duplicate items within a year using normalized title keys."""
    deduped = OrderedDict()
    for year, items in items_by_year.items():
        seen_titles = set()
        deduped_items = []
        for item in items:
            tkey = title_key(item)
            if tkey and tkey in seen_titles:
                continue
            if tkey:
                seen_titles.add(tkey)
            deduped_items.append(item)
        deduped[year] = deduped_items
    return deduped


def main():
    include_text = PUBS_HTML.read_text(encoding="utf-8") if PUBS_HTML.exists() else ""
    existing_by_year, keys_by_year = parse_existing_include(include_text)

    doc_html = load_doc_html()
    doc_by_year = parse_doc_items_by_year(doc_html)

    additions = 0
    for year, items in doc_by_year.items():
        if year not in existing_by_year:
            existing_by_year[year] = []
            keys_by_year[year] = set()
        for item in items:
            key = item_identity_key(item)
            if key not in keys_by_year[year]:
                existing_by_year[year].append(item)
                keys_by_year[year].add(key)
                additions += 1

    existing_by_year = dedupe_items_by_title(existing_by_year)

    rendered = render_include(existing_by_year)
    PUBS_HTML.write_text(rendered, encoding="utf-8")
    print(f"[include] Wrote {PUBS_HTML} with {len(existing_by_year)} year blocks and {additions} added item(s).")


if __name__ == "__main__":
    main()