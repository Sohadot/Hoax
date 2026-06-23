# Public Reference Link Graph Audit v1

## Sprint 87 Audit — Public Reference Authority Internal Linking v1

**Date:** 2026-06-23  
**Decision:** DEC-105  
**Gate:** G87  
**Sprint:** Sprint 87

## Audit Scope

This audit verifies that Hoax.ai’s public authority link graph was strengthened across the unchanged twenty-nine-URL surface without new routes, forbidden capability, or registry/sitemap inflation. Production changes precede governance documentation per Hoax.ai production-first discipline.

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
| **Explore the Evidence-Risk Reference Layer** section links all six Sprint 85 reference routes | PASS |
| Public utility section links all four Sprint 84 utilities | PASS |
| Non-verdict category boundary language preserved | PASS |
| No upload, score, verdict, detector, API, or JavaScript behavior introduced | PASS |
| Homepage acts as authority graph root for human and crawl entry | PASS |

## Ten Pages Updated

Sprint 87 updated ten production HTML pages with governed authority linking components. Homepage is audited separately above.

### Sprint 84 Utility Routes (4)

| Page | reference_path | related_concepts | use_next | page_end_reference_nav | page_end_utility_nav | contextual_body_links |
|------|----------------|------------------|----------|------------------------|----------------------|----------------------|
| `/manual-evidence-checklist/` | PASS | PASS | PASS | PASS (6/6) | PASS (4/4) | PASS |
| `/evidence-posture-map/` | PASS | PASS | PASS | PASS (6/6) | PASS (4/4) | PASS |
| `/synthetic-examples/` | PASS | PASS | PASS | PASS (6/6) | PASS (4/4) | PASS |
| `/evidence-risk-questions/` | PASS | PASS | PASS | PASS (6/6) | PASS (4/4) | PASS |

### Sprint 85 Reference Routes (6)

| Page | reference_path | ai_readable_link_capsule | related_concepts | use_next | page_end_reference_nav | page_end_utility_nav | sibling_links |
|------|----------------|--------------------------|------------------|----------|------------------------|----------------------|---------------|
| `/evidence-risk/` | PASS | PASS | PASS | PASS | PASS (6/6) | PASS (4/4) | PASS (≥2) |
| `/provenance-risk/` | PASS | PASS | PASS | PASS | PASS (6/6) | PASS (4/4) | PASS (≥2) |
| `/context-collapse/` | PASS | PASS | PASS | PASS | PASS (6/6) | PASS (4/4) | PASS (≥2) |
| `/claim-drift/` | PASS | PASS | PASS | PASS | PASS (6/6) | PASS (4/4) | PASS (≥2) |
| `/traceability-gap/` | PASS | PASS | PASS | PASS | PASS (6/6) | PASS (4/4) | PASS (≥2) |
| `/why-hoax-ai-is-not-a-detector/` | PASS | PASS | PASS | PASS | PASS (6/6) | PASS (4/4) | PASS (≥2) |

**Component summary:** All six `required_components` from `data/public-reference-authority-internal-linking-v1.json` are met across the audited surface:

- `reference_path`
- `related_concepts`
- `use_next`
- `ai_readable_link_capsule`
- `homepage_reference_graph`
- `page_end_reference_navigation`

## Link Graph Integrity

| Rule | Result |
|------|--------|
| All `href` targets resolve to registered routes | PASS |
| No links to candidate-only SEO authority map paths | PASS |
| No orphan utilities (each links to full reference cluster) | PASS |
| No orphan reference units (each links to utilities and siblings) | PASS |
| Bidirectional utility ↔ reference discovery via page-end nav | PASS |
| Fragment anchors resolve to existing IDs | PASS |
| Trailing-slash path consistency with registry | PASS |

## Human and AI Standard Compliance

| Standard document | Requirement area | Result |
|-------------------|------------------|--------|
| HUMAN_AI_INTERNAL_LINKING_STANDARD_V1.md | Human-readable linking | PASS |
| HUMAN_AI_INTERNAL_LINKING_STANDARD_V1.md | AI-readable capsules and labels | PASS |
| HUMAN_AI_INTERNAL_LINKING_STANDARD_V1.md | Anchor text rules | PASS |
| HUMAN_AI_INTERNAL_LINKING_STANDARD_V1.md | Non-verdict linking language | PASS |
| HUMAN_AI_INTERNAL_LINKING_STANDARD_V1.md | Thin-link prevention | PASS |

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

## Governance Artifacts

| Artifact | Status |
|----------|--------|
| PUBLIC_REFERENCE_AUTHORITY_INTERNAL_LINKING_V1.md | Created |
| HUMAN_AI_INTERNAL_LINKING_STANDARD_V1.md | Created |
| PUBLIC_REFERENCE_LINK_GRAPH_AUDIT_V1.md | Created |
| SPRINT_87_PUBLIC_REFERENCE_AUTHORITY_INTERNAL_LINKING_V1.md | Created |
| data/public-reference-authority-internal-linking-v1.json | Present |
| data/public-reference-authority-internal-linking-v1.schema.json | Present |
| DEC-105 decision log entry | Required companion |
| validators/validate_public_reference_authority_internal_linking_v1.py | Added |
| validators/validate_all.py includes Sprint 87 validator | Added |

## Validator and Harness Results

| Check | Result |
|-------|--------|
| `validators/validate_public_reference_authority_internal_linking_v1.py` | PASS |
| `validators/validate_all.py` | PASS |
| Internal prototype harnesses | PASS |
| Link-route integrity cross-check | PASS |
| Public surface checks (29 routes / 29 sitemap) | PASS |

## Audit Conclusion

Sprint 87 successfully embodied a governed authority link graph across homepage plus ten updated pages without expanding the public route surface. Utilities and Sprint 85 reference routes now form a bidirectional, human-readable and AI-readable concept cluster at twenty-nine URLs. No forbidden capability was introduced. Validation infrastructure protects the graph for future edits.

**Gate G87:** Criteria met — audit PASS.
