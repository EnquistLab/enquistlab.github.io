#!/usr/bin/env python3
"""
sync_people_sheet.py
====================
Reads lab member data from a Google Sheet and writes:
  - _data/people.yml   (Jekyll data file consumed by _pages/people.md)
  - assets/img/team/<name>.jpg  (photos downloaded from Google Drive share links)

Usage (locally):
  export GOOGLE_API_KEY=<your_key>        # OR use a service-account JSON
  export PEOPLE_SHEET_ID=<sheet_id>
  python scripts/sync_people_sheet.py

In GitHub Actions the two secrets GOOGLE_API_KEY and PEOPLE_SHEET_ID are
injected automatically (see .github/workflows/sync-people-sheet.yml).

Google Sheet expected columns (row 1 = headers):
  Timestamp | Full Name | Role | Institution/Affiliation | Degree |
  Short Bio | Google Scholar URL | Personal Website URL | GitHub URL |
  Email | Google Drive Photo Link | Quote

Role values (case-insensitive, partial match):
  postdoc / postdoctoral → postdocs
  phd / ms / grad        → grad_students
  visiting               → visiting_students
  staff / manager / tech → staff
"""

import os
import re
import sys
import hashlib
import unicodedata
import urllib.request
import urllib.error
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
# Config from environment
# ---------------------------------------------------------------------------
SHEET_ID = os.environ.get("PEOPLE_SHEET_ID", "")
API_KEY = os.environ.get("GOOGLE_API_KEY", "")

if not SHEET_ID:
    print("ERROR: PEOPLE_SHEET_ID environment variable is not set.", file=sys.stderr)
    sys.exit(1)
if not API_KEY:
    print("ERROR: GOOGLE_API_KEY environment variable is not set.", file=sys.stderr)
    sys.exit(1)

# Google Sheets tab/range – adjust if the form responses land on a different sheet
SHEET_RANGE = "Form Responses 1!A:L"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fetch_sheet_rows(sheet_id: str, api_key: str, sheet_range: str) -> list[list[str]]:
    """Fetch all rows from a Google Sheet using the Sheets v4 REST API."""
    import json

    encoded_range = urllib.request.quote(sheet_range, safe="!:")
    url = (
        f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}"
        f"/values/{encoded_range}?key={api_key}"
    )
    with urllib.request.urlopen(url, timeout=30) as resp:  # nosec B310 – https only
        data = json.loads(resp.read().decode())
    return data.get("values", [])


def sanitize_filename(name: str) -> str:
    """Convert a person's name to a safe filename component."""
    nfkd = unicodedata.normalize("NFKD", name)
    ascii_name = nfkd.encode("ascii", "ignore").decode("ascii")
    safe = re.sub(r"[^\w\s-]", "", ascii_name).strip().lower()
    return re.sub(r"[\s]+", "_", safe)


def gdrive_direct_url(share_url: str) -> str | None:
    """
    Convert a Google Drive share URL to a direct download URL.
    Accepts:
      https://drive.google.com/file/d/FILE_ID/view?usp=sharing
      https://drive.google.com/open?id=FILE_ID
    """
    m = re.search(r"/d/([^/?#]+)", share_url)
    if not m:
        m = re.search(r"[?&]id=([^&]+)", share_url)
    if not m:
        return None
    file_id = m.group(1)
    return f"https://drive.google.com/uc?export=download&id={file_id}"


def download_photo(share_url: str, dest_path: Path) -> bool:
    """
    Download a photo from a Google Drive share link to dest_path.
    Returns True if the file was new/changed, False otherwise.
    Skips download if the file already exists with the same content.
    """
    direct_url = gdrive_direct_url(share_url)
    if not direct_url:
        print(f"  WARNING: Could not parse Drive URL: {share_url}", file=sys.stderr)
        return False

    try:
        req = urllib.request.Request(direct_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:  # nosec B310 – https only
            content_type = resp.headers.get("Content-Type", "")
            if "text/html" in content_type:
                # Google returns an HTML warning page for large files without
                # a confirmation token – we can't handle those automatically.
                print(
                    f"  WARNING: Photo download returned HTML (large-file warning). "
                    f"Download manually and commit to assets/img/team/. URL: {share_url}",
                    file=sys.stderr,
                )
                return False
            new_bytes = resp.read()
    except urllib.error.URLError as exc:
        print(f"  WARNING: Failed to download photo ({exc}): {share_url}", file=sys.stderr)
        return False

    new_hash = hashlib.sha256(new_bytes).hexdigest()
    if dest_path.exists():
        old_hash = hashlib.sha256(dest_path.read_bytes()).hexdigest()
        if old_hash == new_hash:
            return False  # unchanged

    dest_path.write_bytes(new_bytes)
    print(f"  Saved photo → {dest_path.relative_to(REPO_ROOT)}")
    return True


def classify_role(raw_role: str) -> str:
    """Map a free-text role to one of the four YAML section keys."""
    r = raw_role.strip().lower()
    if any(k in r for k in ("postdoc", "post-doc", "post doc")):
        return "postdocs"
    if any(k in r for k in ("visiting",)):
        return "visiting_students"
    if any(k in r for k in ("phd", "ms ", "m.s", "grad", "student")):
        return "grad_students"
    # staff / lab manager / technician / researcher etc.
    return "staff"


def col(row: list[str], idx: int) -> str:
    """Safely return a stripped cell value, defaulting to ''."""
    try:
        return row[idx].strip()
    except IndexError:
        return ""


# ---------------------------------------------------------------------------
# Column indices (0-based) – must match the Google Form / Sheet layout
# ---------------------------------------------------------------------------
COL_TIMESTAMP = 0
COL_NAME = 1
COL_ROLE = 2
COL_INSTITUTION = 3
COL_DEGREE = 4
COL_BIO = 5
COL_SCHOLAR = 6
COL_WEBSITE = 7
COL_GITHUB = 8
COL_EMAIL = 9
COL_PHOTO = 10
COL_QUOTE = 11

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"Fetching people data from Google Sheet {SHEET_ID} …")
    rows = fetch_sheet_rows(SHEET_ID, API_KEY, SHEET_RANGE)

    if not rows:
        print("WARNING: Sheet returned no data. Nothing written.", file=sys.stderr)
        return

    # Skip header row
    data_rows = rows[1:]
    if not data_rows:
        print("WARNING: Sheet has only a header row and no member data.", file=sys.stderr)
        return

    sections: dict[str, list[dict]] = {
        "postdocs": [],
        "grad_students": [],
        "visiting_students": [],
        "staff": [],
    }

    for row in data_rows:
        name = col(row, COL_NAME)
        if not name:
            continue  # skip blank rows

        raw_role = col(row, COL_ROLE)
        section = classify_role(raw_role)

        photo_url = col(row, COL_PHOTO)
        photo_filename = ""
        if photo_url:
            safe_name = sanitize_filename(name)
            dest = PHOTO_DIR / f"{safe_name}.jpg"
            print(f"  Downloading photo for {name} …")
            ok = download_photo(photo_url, dest)
            if ok or dest.exists():
                photo_filename = f"{safe_name}.jpg"

        entry: dict = {
            "name": name,
            "role": raw_role,
            "photo": photo_filename,
            "bio": col(row, COL_BIO),
            "google_scholar": col(row, COL_SCHOLAR),
            "website": col(row, COL_WEBSITE),
            "github": col(row, COL_GITHUB),
            "email": col(row, COL_EMAIL),
        }

        institution = col(row, COL_INSTITUTION)
        degree = col(row, COL_DEGREE)
        quote = col(row, COL_QUOTE)

        if institution:
            entry["institution"] = institution
        if degree:
            entry["degree"] = degree
        if quote:
            entry["quote"] = quote

        sections[section].append(entry)

    # ------------------------------------------------------------------
    # Write YAML
    # ------------------------------------------------------------------
    HEADER = (
        "# ============================================================\n"
        "# Enquist Lab – People Data\n"
        "# AUTO-GENERATED by scripts/sync_people_sheet.py\n"
        "# Do not edit manually – changes will be overwritten.\n"
        "# To update your entry fill in the Google Form linked in\n"
        "# _data/people.yml or the lab wiki.\n"
        "# ============================================================\n\n"
    )

    yaml_str = HEADER + yaml.dump(
        sections,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
    )

    # Check for changes
    if DATA_FILE.exists() and DATA_FILE.read_text(encoding="utf-8") == yaml_str:
        print("No changes detected in people data. Nothing written.")
        return

    DATA_FILE.write_text(yaml_str, encoding="utf-8")
    print(f"Written → {DATA_FILE.relative_to(REPO_ROOT)}")
    print(
        f"  {sum(len(v) for v in sections.values())} members across "
        f"{len([s for s in sections.values() if s])} sections."
    )


if __name__ == "__main__":
    main()
