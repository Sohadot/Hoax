# Sprint 26 — Public Category Language Layer Audit

**Date:** 2026-06-17  
**Sprint:** 26 — Public Category Language Layer v1  
**Decision:** DEC-044

## Summary

Sprint 26 created Hoax.ai’s first public category language layer: one governed public route at `/language/`, term registry, relation map, policy artifacts, and validator enforcement. Publisher status moved to `blocked_until_public_category_language_validation`. Engine, classifier, tool, upload, scoring, and broader publication remain blocked.

## Files Created

- `language/index.html`
- `PUBLIC_CATEGORY_LANGUAGE_LAYER.md`
- `data/public-category-language-policy.json`
- `data/category-language-term-registry.json`
- `data/category-language-relation-map.json`
- `data/public-category-language-layer-v1.json`
- `validators/validate_public_category_language_layer.py`
- `SPRINT_26_PUBLIC_CATEGORY_LANGUAGE_LAYER_AUDIT.md`

## Files Updated

- `index.html` — Category Language link added
- `sitemap.xml` — 3 → 4 URLs (`/language/` added)
- `data/route-registry.json` — ROUTE-0004 `/language/`
- `data/internal-link-graph.json` — v1.2.0, language links
- `reference/evidence-posture/index.html` — related link to `/language/`
- `reference/artifact-subject-separation/index.html` — related link to `/language/`
- `data/publisher-governance-policy.json` — `blocked_until_public_category_language_validation`
- `data/publisher-quality-gates.json` — PUB-GATE-0026
- `data/reference-expansion-gate.json` — category language layer required
- `data/publisher-state-machine.json`
- `data/content-quality-standard.json`
- `data/public-file-registry.json`
- `styles.css` — language term cards and relation map styles
- `validators/validate_all.py`
- `validators/public_surface_checks.py`
- `validators/validate_controlled_public_reference_pilot.py`
- `validators/validate_public_reference_live_surface.py`
- `validators/validate_technical_quality_gate.py`
- `validators/validate_publisher_control_plane.py` and related publisher validators
- `data/source-registry.json` — SOURCE-0148 through SOURCE-0154
- `data/evidence-ledger.json` — CLAIM-0032
- `data/claim-source-map.json`
- `DECISION_LOG.md` — DEC-044
- `ROADMAP.md`
- `MASTER_EXECUTION_PLAN.md` — G26
- `CATEGORY_INTELLIGENCE_FACTORY_PLAN.md`

## Deliverables Confirmed

- Public category language layer created
- Language route `/language/` created
- Language term registry created (8 terms)
- Relation map created (7 relations)
- Public category language layer policy created
- Homepage link to `/language/` added
- Sitemap updated from 3 to 4 URLs
- Route registry updated with ROUTE-0004
- Internal link graph updated
- Publisher status → `blocked_until_public_category_language_validation`
- Publisher quality gates updated (PUB-GATE-0026)
- Reference expansion gate updated
- Validator created and wired into `validate_all.py`

## Prohibited Items Not Created

- No individual term pages
- No new reference pages
- No public classifier
- No public engine
- No public tool
- No upload workflow
- No scoring
- No forms
- No analytics
- No API
- No monetization
- No DNS or Cloudflare work
- No custom domain launch
- No external factual claims
- No real-world examples
- `.nojekyll` not created
- Deployment settings not changed
- Broader publication remains blocked
- Engine/classifier remains blocked

## Validation

```
python validators/validate_all.py
```

Result: **PASS** (required for sprint closure)

## Next Phase

**Sprint 27 — Public Category Language Validation and Surface Audit v1**
