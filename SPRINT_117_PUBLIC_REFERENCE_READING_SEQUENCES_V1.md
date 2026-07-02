# Sprint 117 — Public Reference Reading Sequences v1

**Decision:** DEC-135  
**Status:** Complete

## Goal

Add one public reference route that guides humans and AI agents through governed reading sequences across the Hoax.ai public surface.

## Production change

- Added `/reading-sequences/` as ROUTE-0101 and PUB-FILE-0101.
- Public surface moved from 100 to 101 routes.
- Homepage, system-map, and evidence-condition crosswalk now link to reading sequences.
- Relevant route-group and audience-path pages include concise reading-sequence references.
- Sitemap and registries aligned to 101.

## Governance outputs

- `PUBLIC_REFERENCE_READING_SEQUENCES_V1.md`
- `PUBLIC_REFERENCE_READING_SEQUENCE_STANDARD_V1.md`
- `PUBLIC_REFERENCE_READING_SEQUENCES_AUDIT_V1.md`
- `data/public-reference-reading-sequences-v1.json` and schema
- `validators/validate_public_reference_reading_sequences_v1.py`
- DEC-135 appended
- Claim/source/gate registries updated

## Boundary confirmation

Sprint 117 introduced no extra routes, no workflow logic, no assessment process, no decision-tree behavior, no scoring/rating/detector behavior, no upload/API/forms/JavaScript behavior, and no transaction/sales/consulting/legal/financial representation behavior.

## Validation

- `py -3 validators/validate_public_reference_reading_sequences_v1.py` — PASS
- `py -3 -m compileall validators` — PASS
- `py -3 validators/validate_all.py` — PASS
- internal prototype harnesses — PASS
