# Sprint 27 — Public Category Language Validation and Surface Audit

**Date:** 2026-06-17  
**Sprint:** 27 — Public Category Language Validation and Surface Audit v1  
**Decision:** DEC-045

## Summary

Sprint 27 validated Hoax.ai’s public category language layer at `/language/` across 25 dimensions including Hoax-Specific Language Ownership Integrity. Publisher status moved to `blocked_until_evidence_posture_workbench_governance`. No new public expansion occurred.

## Files Created

- `PUBLIC_CATEGORY_LANGUAGE_VALIDATION_AND_SURFACE_AUDIT.md`
- `data/public-category-language-validation-policy.json`
- `data/public-category-language-surface-audit-v1.json`
- `data/public-category-language-validation-results-v1.json`
- `validators/validate_public_category_language_validation.py`
- `SPRINT_27_PUBLIC_CATEGORY_LANGUAGE_VALIDATION_SURFACE_AUDIT.md`

## Files Updated

- `data/publisher-governance-policy.json` — `blocked_until_evidence_posture_workbench_governance`
- `data/publisher-quality-gates.json` — PUB-GATE-0027
- `data/reference-expansion-gate.json`
- `data/publisher-state-machine.json`
- `data/content-quality-standard.json`
- `data/route-registry.json` — language validation status annotation on ROUTE-0004
- `validators/validate_all.py`
- `validators/public_surface_checks.py`
- `validators/validate_public_category_language_layer.py`
- `validators/validate_publisher_control_plane.py` and related publisher validators
- `data/source-registry.json` — SOURCE-0155 through SOURCE-0159
- `data/evidence-ledger.json` — CLAIM-0033
- `data/claim-source-map.json`
- `DECISION_LOG.md` — DEC-045
- `ROADMAP.md`
- `MASTER_EXECUTION_PLAN.md` — G27
- `CATEGORY_INTELLIGENCE_FACTORY_PLAN.md`

## Validation Outcomes

- Public category language validation created
- Language validation policy created
- Language surface audit created (4 surface records)
- Validation results created (25 dimensions, hoax_governed_language_validated)
- Validator created and wired into `validate_all.py`
- Language page audited at `/language/`
- Term registry audited (8 terms)
- Relation map audited (7 relations)
- Sitemap audited (4 URLs unchanged)
- Route registry audited (4 routes)
- Internal link graph audited
- Metadata and JSON-LD boundaries audited
- Forbidden capability checks pass

## Prohibited Items Not Created

- No new public pages
- No individual term pages
- No new reference pages
- No public classifier, engine, or tool
- No upload workflow, scoring, forms, analytics, API, or monetization
- No DNS or Cloudflare work
- No custom domain launch
- No external factual claims or real-world examples
- `.nojekyll` not created
- Deployment settings not changed
- Broader publication remains blocked
- Engine/classifier remains blocked until explicit future governance

## Validation

```
python validators/validate_all.py
```

Result: **PASS** (required for sprint closure)

## Next Phase

**Sprint 28 — Evidence Posture Workbench Governance v1**

Sprint 28 may use the validated Hoax-governed language layer as governance input, not as proof that the public engine is ready.
