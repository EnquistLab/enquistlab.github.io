# Publication Grouping Workflow

This workflow governs subject-area grouping on the publications page.

## Goals

- Allow a paper to appear in multiple categories.
- Keep automated grouping fast and deterministic.
- Preserve manual ecological judgment for edge cases.
- Track papers that need curator review.

## Current Grouping Stack

1. Keyword-weighted auto-classification in `_pages/publications.html`.
2. Manual override layer for known edge cases.
3. `needs-review` category for uncategorized papers.

## Manual Overrides

Override metadata is stored in `_data/publication_category_overrides.yml`.

Required fields per override:

- `id`: unique identifier.
- `title_hints`: lowercase phrases used to match the target paper.
- `force_categories`: category ids to force-add.
- `rationale`: short scientific reason.

Papers matched by an override keep all auto labels and receive all forced labels.

## Review Procedure

1. Open `/publications/` and click `Needs Review`.
2. For each paper in this bucket:
   - Confirm intended category memberships.
   - Add or update override entry when needed.
3. Rebuild/publish and verify paper appears in all expected tabs.

## Curation Guidance

- Prefer specific phrases in `title_hints` to avoid false matches.
- Keep category overlap when scientifically justified.
- Do not remove categories unless classification is clearly wrong.
- Record rationale in override entries for provenance.

## Example

`Althuizen et al. (2026)` is explicitly forced into:

- `arctic-alpine`
- `ecophysiology`

This guarantees the paper appears in both tabs even if wording drift affects keyword scoring.