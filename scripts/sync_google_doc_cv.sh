#!/usr/bin/env bash
set -euo pipefail

# Sync a Google Docs CV export into the repository only when source content changes.

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOC_ID="${GOOGLE_DOC_CV_ID:-1OMolpDfY6c73qRgUFgYh0XbMS8EykUoy_hvrI8fnTn0}"

EXPORT_BASE="https://docs.google.com/document/d/${DOC_ID}/export"
TMP_DIR="$(mktemp -d)"
TXT_TMP="${TMP_DIR}/cv.txt"
PDF_TMP="${TMP_DIR}/cv.pdf"

HASH_FILE="${REPO_ROOT}/assets/cv/google_doc_cv.sha256"
TXT_OUT="${REPO_ROOT}/assets/cv/google_doc_cv_latest.txt"
PDF_OUT="${REPO_ROOT}/assets/pdf/enquist_cv.pdf"

mkdir -p "${REPO_ROOT}/assets/cv" "${REPO_ROOT}/assets/pdf"

echo "Fetching Google Doc exports for CV sync..."
curl -fsSL "${EXPORT_BASE}?format=txt" -o "${TXT_TMP}"
curl -fsSL "${EXPORT_BASE}?format=pdf" -o "${PDF_TMP}"

NEW_HASH="$(shasum -a 256 "${TXT_TMP}" | awk '{print $1}')"
OLD_HASH=""

if [[ -f "${HASH_FILE}" ]]; then
  OLD_HASH="$(tr -d '[:space:]' < "${HASH_FILE}")"
fi

if [[ "${NEW_HASH}" == "${OLD_HASH}" ]]; then
  echo "No CV update detected in Google Doc."
  rm -rf "${TMP_DIR}"
  exit 0
fi

cp "${TXT_TMP}" "${TXT_OUT}"
cp "${PDF_TMP}" "${PDF_OUT}"
printf "%s\n" "${NEW_HASH}" > "${HASH_FILE}"

echo "CV update detected and synced."
rm -rf "${TMP_DIR}"
