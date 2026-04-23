#!/usr/bin/env python3
"""
sync_people_sheet.py
====================
Reads lab member data from a PUBLIC Google Sheet (CSV export — no API key
required) and writes:
  - _data/people.yml   (Jekyll data file consumed by _pages/people.md)
  - assets/img/team/<name>.jpg  (photos downloaded from Google Drive share links)

Usage (locally or in GitHub Actions):
  python scripts/sync_people_sheet.py

The sheet must be shared as "Anyone with the link can view".
No Google API key or service account is needed.

Google Sheet row 1 MUST contain these headers (column order flexible,
wording matched by keyword substring so minor variations are fine):
  Full Name | Role | Institution/Affiliation | Degree |
  Short Bio | Google Scholar URL | Personal Website URL | GitHub URL |
  Email | Photo (Google Drive link) | Favorite Quote

Role values (case-insensitive partial match):
  postdoc / postdoctoral  -> postdocs
  visiting                -> visiting_students
  phd / ms / grad / student -> grad_students
  anything else           -> staff
"""

import csv
import hashlib
import io
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "_data" / "people.yml"
PHOTO_DIR = REPO_ROOT / "assets" / "img" / "team"
PHOTO_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SHEET_ID = (
    os.environ.get("PEOPLE_SHEET_ID")
    or "1oW_QHLvJ1DGIFUP956T4W2nwn8xThw5t6QmaM_nxDjM"
)
SHEET_GID = os.environ.get("PEOPLE_SHEET_GID", "0")

CSV_URL = (
    f"https://docs.google.com/spreadsheets/d/{SHEET_ID}"
    f"/export?format=csv&gid={SHEET_GID}"
)

# ---------------------------------------------------------------------------
# Header keyword mapping (lowercase substring match against row 1)
# ---------------------------------------------------------------------------
HEADER_KEYWORDS: dict = {
    "name":        "full name",
    "role":        "role",
    "institution": "institution",
    "degree":      "degree",
    "bio":         "short bio",
    "scholar":     "google scholar",
    "website":     "personal website",
    "github":      "github",
    "email":       "email",
    "photo":       "photo",
    "quote":       "quote",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fetch_csv_rows(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        content_type = resp.headers.get("Content-Type", "")
        raw = resp.read()

    # Detect if Google returned an HTML page (login redirect / CAPTCHA / bot block)
    content = raw.decode("utf-8-sig")
    if content.strip().lower().startswith("<!doctype") or "<html" in content[:200].lower():
        print(
            "ERROR: Google returned an HTML page instead of CSV.\n"
            "  This usually means the sheet is not public, or Google is blocking\n"
            "  requests from this cloud IP range.\n"
            f"  Content-Type: {content_type}\n"
            f"  First 300 chars: {content[:300]!r}",
            file=sys.stderr,
        )
        sys.exit(1)

    reader = csv.reader(io.StringIO(content))
    return list(reader)


def build_index(header_row):
    index = {}
    missing = []
    for key, keyword in HEADER_KEYWORDS.items():
        idx = next(
            (i for i, h in enumerate(header_row) if keyword in h.strip().lower()),
            None,
        )
        if idx is None:
            if key == "name":
                missing.append("Full Name")
        else:
            index[key] = idx
    if missing:
        print(f"ERROR: Required column(s) not found: {missing}", file=sys.stderr)
        print(f"  Found: {header_row}", file=sys.stderr)
        sys.exit(1)
    return index


def get(row, index, key):
    idx = index.get(key)
    if idx is None:
        return ""
    try:
        return row[idx].strip()
    except IndexError:
        return ""


def classify_role(raw_role):
    r = raw_role.strip().lower()
    if any(k in r for k in ("postdoc", "post-doc", "post doc")):
        return "postdocs"
    if "visiting" in r:
        return "visiting_students"
    if any(k in r for k in ("phd", "ms ", "m.s.", "grad", "student", "masters", "undergraduate")):
        return "grad_students"
    return "staff"


def sanitize_filename(name):
    nfkd = unicodedata.normalize("NFKD", name)
    ascii_name = nfkd.encode("ascii", "ignore").decode("ascii")
    safe = re.sub(r"[^\w\s-]", "", ascii_name).strip().lower()
    return re.sub(r"\s+", "_", safe)


def gdrive_direct_url(share_url):
    m = re.search(r"/d/([^/?#]+)", share_url)
    if not m:
        m = re.search(r"[?&]id=([^&]+)", share_url)
    if not m:
        return None
    return f"https://drive.google.com/uc?export=download&id={m.group(1)}"


def download_photo(share_url, dest_path):
    direct_url = gdrive_direct_url(share_url)
    if not direct_url:
        print(f"  WARNING: Cannot parse Drive URL: {share_url}", file=sys.stderr)
        return False
    try:
        req = urllib.request.Request(direct_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            if "text/html" in resp.headers.get("Content-Type", ""):
                print(
                    "  WARNING: Photo download returned HTML page. "
                    "Commit photo manually to assets/img/team/.",
                    file=sys.stderr,
                )
                return False
            new_bytes = resp.read()
    except urllib.error.URLError as exc:
        print(f"  WARNING: Photo download failed ({exc})", file=sys.stderr)
        return False

    new_hash = hashlib.sha256(new_bytes).hexdigest()
    if dest_path.exists():
        if hashlib.sha256(dest_path.read_bytes()).hexdigest() == new_hash:
            return False
    dest_path.write_bytes(new_bytes)
    print(f"  Saved photo -> {dest_path.relative_to(REPO_ROOT)}")
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print(f"Fetching sheet as CSV from Google Sheets ...")
    print(f"  URL: {CSV_URL}")
    try:
        rows = fetch_csv_rows(CSV_URL)
    except urllib.error.URLError as exc:
        print(f"ERROR: Could not fetch sheet ({exc})", file=sys.stderr)
        print(
            "Make sure the sheet is shared as 'Anyone with the link can view'.",
            file=sys.stderr,
        )
        sys.exit(1)

    if not rows:
        print("WARNING: Sheet returned no rows.", file=sys.stderr)
        return

    # Find the header row — the first row that contains "full name" in any cell.
    # This skips any decorative label rows (e.g. A, B, C...) at the top.
    header_row_idx = next(
        (i for i, row in enumerate(rows)
         if any("full name" in cell.strip().lower() for cell in row)),
        None,
    )
    if header_row_idx is None:
        print(
            "ERROR: Could not find a row containing 'Full Name' in the sheet.\n"
            "  Make sure row 1 (or row 2) of the sheet has the header labels.",
            file=sys.stderr,
        )
        sys.exit(1)

    header_row = rows[header_row_idx]
    print(f"  Header row (row {header_row_idx + 1}): {header_row}")
    index = build_index(header_row)

    data_rows = [r for r in rows[header_row_idx + 1:] if any(c.strip() for c in r)]
    if not data_rows:
        print("WARNING: No data rows found (sheet has only a header).", file=sys.stderr)
        return

    sections = {
        "postdocs": [],
        "grad_students": [],
        "visiting_students": [],
        "staff": [],
    }

    for row in data_rows:
        name = get(row, index, "name")
        if not name:
            continue

        raw_role = get(row, index, "role")
        section = classify_role(raw_role)

        photo_url = get(row, index, "photo")
        photo_filename = ""
        if photo_url:
            safe_name = sanitize_filename(name)
            dest = PHOTO_DIR / f"{safe_name}.jpg"
            print(f"  Downloading photo for {name} ...")
            ok = download_photo(photo_url, dest)
            if ok or dest.exists():
                photo_filename = f"{safe_name}.jpg"

        entry = {
            "name": name,
            "role": raw_role,
            "photo": photo_filename,
            "bio": get(row, index, "bio"),
            "google_scholar": get(row, index, "scholar"),
            "website": get(row, index, "website"),
            "github": get(row, index, "github"),
            "email": get(row, index, "email"),
        }

        for optional_key in ("institution", "degree", "quote"):
            val = get(row, index, optional_key)
            if val:
                entry[optional_key] = val

        sections[section].append(entry)
        print(f"  -> {name} ({section})")

    total = sum(len(v) for v in sections.values())
    print(f"\nProcessed {total} members.")

    FILE_HEADER = (
        "# ============================================================\n"
        "# Enquist Lab - People Data\n"
        "# AUTO-GENERATED by scripts/sync_people_sheet.py\n"
        f"# Source: https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit\n"
        "# Do not edit manually - changes will be overwritten on next sync.\n"
        "# ============================================================\n\n"
    )

    yaml_str = FILE_HEADER + yaml.dump(
        sections,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
    )

    if DATA_FILE.exists() and DATA_FILE.read_text(encoding="utf-8") == yaml_str:
        print("No changes detected. Nothing written.")
        return

    DATA_FILE.write_text(yaml_str, encoding="utf-8")
    print(f"Written -> {DATA_FILE.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
