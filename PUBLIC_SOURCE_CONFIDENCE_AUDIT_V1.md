# Public Source Confidence Audit v1

## Sprint 88 Audit — Public Reference Source Confidence Layer v1

**Date:** 2026-06-23  
**Decision:** DEC-106  
**Gate:** G88  
**Sprint:** Sprint 88

## Audit Scope

This audit verifies that Hoax.ai’s public source-confidence layer was embodied across homepage and ten Sprint 84/85 production pages without new routes, forbidden capability, registry/sitemap inflation, or support-type collapse into scoring or verification. Production changes precede governance documentation per Hoax.ai production-first discipline.

## Surface Count Verification

| Check | Expected | Result |
|-------|----------|--------|
| Sitemap URL count | 29 | PASS |
| Route registry entry count | 29 | PASS |
| New public routes added | 0 | PASS |
| New sitemap entries added | 0 | PASS |
| New registry entries added | 0 | PASS |

Sitemap and registry remain aligned at twenty-nine URLs: homepage, language layer, twelve legacy `/reference/` pages, standard, protocol, interface, four utilities, and six Sprint 85 reference routes.

## Homepage Update

| Requirement | Status |
|-------------|--------|
| Source-confidence component present with required fields | PASS |
| Primary support type declared (Boundary Statement / repository sections as governed) | PASS |
| Page support statement describes category reference role | PASS |
| Does-not-support negates score, verdict, verification, upload, automation | PASS |
| AI-readable source-confidence capsule with enum support type | PASS |
| **Not a score** and **Not verification** explicit in capsule | PASS |
| Non-verdict category boundary language preserved | PASS |
| Sprint 87 reference graph and utility links intact | PASS |
| No upload, score, verdict, detector, API, or JavaScript behavior introduced | PASS |

## Ten Pages Updated

Sprint 88 updated ten production HTML pages with governed source-confidence components. Homepage is audited separately above.

### Sprint 84 Utility Routes (4)

| Page | support_type | human_block | ai_capsule | does_not_support | not_a_score | not_verification | route_field |
|------|--------------|-------------|------------|------------------|-------------|------------------|-------------|
| `/manual-evidence-checklist/` | Manual Utility Guidance | PASS | PASS | PASS | PASS | PASS | PASS |
| `/evidence-posture-map/` | Manual Utility Guidance | PASS | PASS | PASS | PASS | PASS | PASS |
| `/synthetic-examples/` | Synthetic Example | PASS | PASS | PASS | PASS | PASS | PASS |
| `/evidence-risk-questions/` | Manual Utility Guidance | PASS | PASS | PASS | PASS | PASS | PASS |

### Sprint 85 Reference Routes (6)

| Page | support_type | human_block | ai_capsule | does_not_support | not_a_score | not_verification | sprint_87_intact |
|------|--------------|-------------|------------|------------------|-------------|------------------|------------------|
| `/evidence-risk/` | Conceptual Definition | PASS | PASS | PASS | PASS | PASS | PASS |
| `/provenance-risk/` | Conceptual Definition | PASS | PASS | PASS | PASS | PASS | PASS |
| `/context-collapse/` | Conceptual Definition | PASS | PASS | PASS | PASS | PASS | PASS |
| `/claim-drift/` | Conceptual Definition | PASS | PASS | PASS | PASS | PASS | PASS |
| `/traceability-gap/` | Conceptual Definition | PASS | PASS | PASS | PASS | PASS | PASS |
| `/why-hoax-ai-is-not-a-detector/` | Boundary Statement | PASS | PASS | PASS | PASS | PASS | PASS |

**Component summary:** All required fields from `PUBLIC_SOURCE_CONFIDENCE_COMPONENT_STANDARD_V1.md` are met across the audited surface:

- `support_type`
- `page_support_statement`
- `does_not_support`
- `non_verdict_reminder`
- `ai_source_confidence_capsule`
- `not_a_score`
- `not_verification`
- `route`

## Support Type Integrity

| Rule | Result |
|------|--------|
| Each updated page declares exactly one primary allowed support type | PASS |
| No forbidden support types in components or capsules | PASS |
| Support type enum strings match JSON schema | PASS |
| Page support statements are page-specific (not identical boilerplate) | PASS |
| Synthetic examples page states fiction in Supports field | PASS |
| Boundary page does not imply alternative detection product | PASS |

## Human and AI Standard Compliance

| Standard document | Requirement area | Result |
|-------------------|------------------|--------|
| PUBLIC_SOURCE_CONFIDENCE_COMPONENT_STANDARD_V1.md | Human-readable component blocks | PASS |
| PUBLIC_SOURCE_CONFIDENCE_COMPONENT_STANDARD_V1.md | AI-readable source-confidence capsules | PASS |
| PUBLIC_SOURCE_CONFIDENCE_COMPONENT_STANDARD_V1.md | Safe language rules | PASS |
| PUBLIC_SOURCE_CONFIDENCE_COMPONENT_STANDARD_V1.md | Forbidden phrasing absent | PASS |
| PUBLIC_SOURCE_CONFIDENCE_COMPONENT_STANDARD_V1.md | Thin-component prevention | PASS |
| PUBLIC_REFERENCE_SOURCE_CONFIDENCE_LAYER_V1.md | Non-verdict boundary | PASS |
| PUBLIC_REFERENCE_SOURCE_CONFIDENCE_LAYER_V1.md | Not-a-score / not-verification thesis | PASS |

## Forbidden Behavior Verification

| Forbidden behavior | Result |
|--------------------|--------|
| Upload | Not introduced |
| Score | Not introduced |
| Verdict | Not introduced |
| Binary authenticity label output | Not introduced |
| Automated detection | Not introduced |
| Public API | Not introduced |
| Automated report | Not introduced |
| Real-world case evaluation | Not introduced |
| User input submission | Not introduced |
| Analytics | Not introduced |
| Monetization | Not introduced |
| JavaScript navigation or forms | Not introduced |
| Automated confidence score labeling | Not introduced |
| Verification or truth-certification claims | Not introduced |

## Layer JSON Record Verification

| Field | Expected | Result |
|-------|----------|--------|
| `decision_ref` | DEC-106 | PASS |
| `sprint` | Sprint 88 | PASS |
| `new_public_routes_added` | false | PASS |
| `expected_sitemap_url_count_after` | 29 | PASS |
| `source_confidence_is_not_score` | true | PASS |
| `source_confidence_is_not_verification` | true | PASS |
| `pages_updated` | 11 routes | PASS |
| `allowed_support_types` | 5 enums | PASS |
| `forbidden_support_types` | 9 entries minimum | PASS |

## Governance Artifacts

| Artifact | Status |
|----------|--------|
| PUBLIC_REFERENCE_SOURCE_CONFIDENCE_LAYER_V1.md | Created |
| PUBLIC_SOURCE_CONFIDENCE_COMPONENT_STANDARD_V1.md | Created |
| PUBLIC_SOURCE_CONFIDENCE_AUDIT_V1.md | Created |
| SPRINT_88_PUBLIC_REFERENCE_SOURCE_CONFIDENCE_LAYER_V1.md | Created |
| data/public-reference-source-confidence-layer-v1.json | Present |
| data/public-reference-source-confidence-layer-v1.schema.json | Present |
| DEC-106 decision log entry | Required companion |
| validators/validate_public_reference_source_confidence_layer_v1.py | Required companion |
| validators/validate_all.py includes Sprint 88 validator | Required companion |

## Validator and Harness Results

| Check | Result |
|-------|--------|
| `validators/validate_public_reference_source_confidence_layer_v1.py` | PASS |
| `validators/validate_all.py` | PASS |
| Internal prototype harnesses | PASS |
| Public surface checks (29 routes / 29 sitemap) | PASS |
| Forbidden phrasing scan on updated pages | PASS |
| Support-type route assignment cross-check | PASS |

## Audit Conclusion

Sprint 88 successfully embodied a governed source-confidence layer across homepage plus ten updated pages without expanding the public route surface. Each page now declares what it supports and what it does not support — for humans and AI agents — without introducing scores, verification outputs, or forbidden capability. Sprint 87 authority link graph remains intact. Validation infrastructure protects support-type integrity for future edits.

**Gate G88:** Criteria met — audit PASS.
