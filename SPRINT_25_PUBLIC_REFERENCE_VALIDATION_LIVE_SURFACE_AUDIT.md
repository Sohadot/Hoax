# Sprint 25 — Public Reference Validation and Live Surface Audit v1

**Date:** 2026-06-17  
**Decision:** DEC-043  
**Validator:** `validators/validate_public_reference_live_surface.py`  
**validate_all.py:** PASS

## Files Created

- `PUBLIC_REFERENCE_VALIDATION_AND_LIVE_SURFACE_AUDIT.md`
- `data/public-reference-live-surface-policy.json`
- `data/public-reference-live-surface-audit-v1.json`
- `data/public-reference-validation-results-v1.json`
- `validators/validate_public_reference_live_surface.py`
- `SPRINT_25_PUBLIC_REFERENCE_VALIDATION_LIVE_SURFACE_AUDIT.md`

## Files Updated

- `data/publisher-governance-policy.json` → `blocked_until_public_category_language_layer`
- `data/publisher-quality-gates.json` — PUB-GATE-0025
- `data/reference-expansion-gate.json`
- `data/publisher-state-machine.json`
- `data/content-quality-standard.json`
- `data/route-registry.json` — live_surface_validation_status on all three routes
- `data/source-registry.json` — SOURCE-0143 through SOURCE-0147
- `data/evidence-ledger.json` — CLAIM-0031
- `data/claim-source-map.json`
- `validators/validate_all.py`, `validators/public_surface_checks.py`
- `validators/generate_build_manifest.py`, `validators/validate_factory_foundation.py`
- Multiple sprint validators — publisher status allowance
- `DECISION_LOG.md`, `ROADMAP.md`, `MASTER_EXECUTION_PLAN.md`, `CATEGORY_INTELLIGENCE_FACTORY_PLAN.md`
- `BUILD_MANIFEST.json` (regenerated)

## Audited Surfaces

| Record | Path | Outcome |
|--------|------|---------|
| LIVE-SURFACE-0001 | `/` | existing_public_preview_surface |
| LIVE-SURFACE-0002 | `/reference/evidence-posture/` | controlled_public_reference_page_validated |
| LIVE-SURFACE-0003 | `/reference/artifact-subject-separation/` | controlled_public_reference_page_validated |

**Overall outcome:** live_surface_validated_controlled_reference_pilot

## Validation Dimensions

All 20 dimensions pass (dimension 19: pass_expected_local — GitHub Pages preview expected, not network-fetched in CI).

## GitHub Pages Preview

- **Status:** live_preview_expected
- **Canonical URLs:** `https://hoax.ai/` policy
- **GitHub Pages URL (when enabled):** `https://sohadot.github.io/Hoax/`
- Network verification is documented here; deterministic local validation does not require live fetch.

## Prohibitions Verified

- No new public pages, routes, or sitemap URLs
- No classifier, engine, tool, upload, scoring, forms, analytics, API, monetization
- No DNS, Cloudflare, custom domain launch, or `.nojekyll`
- No deployment settings changed
- Broader publication remains blocked

## Next Phase

Sprint 26 — Public Category Language Layer v1
