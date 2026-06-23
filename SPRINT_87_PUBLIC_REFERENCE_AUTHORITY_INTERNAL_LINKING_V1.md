# Sprint 87 — Public Reference Authority Internal Linking v1

**Status:** COMPLETE — 2026-06-23  
**Decision:** DEC-105  
**Gate:** G87

## Goal

Strengthen Hoax.ai public reference authority by connecting the Sprint 84 utility layer and Sprint 85 reference layer into a coherent human-readable and AI-readable internal link graph — without new routes, sitemap expansion, registry inflation, upload, scoring, verdicts, detector claims, public API, automated reports, JavaScript, or forms.

## Problem Statement

After Sprint 85 expanded the surface to twenty-nine URLs, utilities and reference units could be discovered independently but did not consistently expose the same traversal graph. Humans could finish a strong reference page without finding the checklist or posture map. AI agents could retrieve a definition without related concepts, utility routes, or stable navigation labels. Authority lived in page substance but not yet in embodied graph coherence.

Sprint 87 closes that gap on the existing surface.

## Deliverables

### Governance and policy

- PUBLIC_REFERENCE_AUTHORITY_INTERNAL_LINKING_V1.md
- HUMAN_AI_INTERNAL_LINKING_STANDARD_V1.md
- PUBLIC_REFERENCE_LINK_GRAPH_AUDIT_V1.md
- SPRINT_87_PUBLIC_REFERENCE_AUTHORITY_INTERNAL_LINKING_V1.md

### Data records

- data/public-reference-authority-internal-linking-v1.json
- data/public-reference-authority-internal-linking-v1.schema.json

### Validation

- validators/validate_public_reference_authority_internal_linking_v1.py
- validators/validate_all.py — Sprint 87 validator registered

### Production HTML updates (10 pages)

**Utilities (Sprint 84):**

- manual-evidence-checklist/index.html
- evidence-posture-map/index.html
- synthetic-examples/index.html
- evidence-risk-questions/index.html

**Reference units (Sprint 85):**

- evidence-risk/index.html
- provenance-risk/index.html
- context-collapse/index.html
- claim-drift/index.html
- traceability-gap/index.html
- why-hoax-ai-is-not-a-detector/index.html

### Homepage

- index.html — **Explore the Evidence-Risk Reference Layer** and utility sections verified as full graph root

### Decision and claim artifacts

- DEC-105 in DECISION_LOG.md
- CLAIM entry for authority internal linking adoption
- PUB-GATE-0081 (companion publisher gate record)

## Post-Sprint Surface

| Metric | Value |
|--------|-------|
| Sitemap URLs | 29 (unchanged) |
| Route registry entries | 29 (unchanged) |
| New public routes | 0 |
| Updated production pages | 10 + homepage |
| Utility routes in graph | 4 |
| Sprint 85 reference routes in graph | 6 |

## Gate G87 Criteria

Gate G87 passes when all criteria below are met and `validators/validate_all.py` returns PASS.

### G87-1 — No route inflation

- [ ] `new_public_routes_added` is false in linking JSON record
- [ ] Sitemap count remains 29
- [ ] Route registry count remains 29
- [ ] No candidate SEO authority map paths added as live routes

### G87-2 — Homepage reference graph

- [ ] Homepage links all six Sprint 85 reference routes in governed reference layer section
- [ ] Homepage links all four Sprint 84 utilities in governed utility section
- [ ] Homepage preserves non-verdict boundary language

### G87-3 — Required components on updated pages

- [ ] `reference_path` on all ten updated pages
- [ ] `related_concepts` on all ten updated pages
- [ ] `use_next` on all ten updated pages
- [ ] `ai_readable_link_capsule` on all six reference routes
- [ ] `page_end_reference_navigation` — full six-route cluster on all ten pages
- [ ] `page_end_utility_navigation` — full four-utility cluster on all ten pages

### G87-4 — Link graph integrity

- [ ] Every internal link resolves to a registered route in `data/route-registry.json`
- [ ] Bidirectional utility ↔ reference discovery via page-end navigation
- [ ] Each reference page links to ≥2 siblings in body or related-concepts areas
- [ ] No orphan utilities or reference units within the Sprint 84/85 cluster

### G87-5 — Human and AI standard compliance

- [ ] HUMAN_AI_INTERNAL_LINKING_STANDARD_V1.md exists and is referenced by validator
- [ ] Anchor text follows concept-naming rules; forbidden anchors absent
- [ ] Non-verdict linking language preserved
- [ ] Thin-link prevention rules satisfied

### G87-6 — Forbidden behavior boundary

- [ ] No upload, score, verdict, detector claim, public API, automated report, JavaScript, forms, analytics, monetization, or real-world case evaluation introduced
- [ ] All `forbidden_public_behavior` entries in linking JSON remain false / not authorized

### G87-7 — Governance and validation

- [ ] All four Sprint 87 markdown deliverables present
- [ ] Linking JSON validates against schema
- [ ] `validators/validate_public_reference_authority_internal_linking_v1.py` passes
- [ ] `validators/validate_all.py` passes
- [ ] DEC-105 recorded in DECISION_LOG.md

## Completion Checklist

### Production

- [x] Homepage reference graph complete (6 reference + 4 utility links)
- [x] Four utility pages updated with full page-end navigation and Use next
- [x] Six reference pages updated with capsules, siblings, Use next, and page-end navigation
- [x] Contextual body links added where analytically appropriate
- [x] Boundary strips and non-verdict language preserved on all updated pages

### Data and policy

- [x] public-reference-authority-internal-linking-v1.json records DEC-105, Sprint 87, 29/29 counts
- [x] Schema enforces required components and forbidden authorization flags
- [x] PUBLIC_REFERENCE_AUTHORITY_INTERNAL_LINKING_V1.md — authority linking policy
- [x] HUMAN_AI_INTERNAL_LINKING_STANDARD_V1.md — operational linking standard

### Validation

- [x] Sprint 87 validator implemented
- [x] validate_all.py includes Sprint 87 validator
- [x] PUBLIC_REFERENCE_LINK_GRAPH_AUDIT_V1.md documents PASS
- [x] validate_all.py — PASS
- [x] Internal prototype harnesses — PASS

### Governance records

- [x] DEC-105 adopted
- [x] Gate G87 criteria documented
- [x] Sprint record complete (this document)
- [x] Publisher gate companion recorded

## Non-Authorization

Sprint 87 does not authorize:

- New public routes or sitemap expansion
- Engine, classifier, or automated analysis behavior
- Upload workflows, scoring, or verdict outputs
- Public API, forms, or JavaScript interaction
- DNS, Cloudflare, custom domain, or deployment changes
- Analytics, cookies, tracking, or monetization
- Real-world case evaluation on the public surface
- Linking to candidate-only paths from the SEO authority map

## Relationship to Prior Sprints

| Sprint | Contribution | Sprint 87 relationship |
|--------|--------------|------------------------|
| Sprint 84 (DEC-102) | Four utility routes | Utilities gain full reference-cluster navigation |
| Sprint 85 (DEC-103) | Six reference routes | Reference units gain utility navigation and graph consistency |
| Sprint 67 (DEC-085) | SEO authority map | Candidate paths remain candidate-only; no new links authorized |

## Next Phase

Candidate next work (not authorized by Sprint 87):

- Governed links between `/language/` term pages and Sprint 85 reference cluster
- Deeper legacy `/reference/` ↔ top-level reference bridge without route inflation
- Next reference production batch per PUBLIC_REFERENCE_PRODUCTION_PLAN_V1.md — requires separate sprint, registry, and gate approval

Until then, the twenty-nine-URL authority graph is the embodied public reference system for utilities and Sprint 85 concepts.

## Validation

`validators/validate_all.py` — **PASS** required  
Internal prototype harnesses — **PASS** required  
Link graph audit — **PASS** (see PUBLIC_REFERENCE_LINK_GRAPH_AUDIT_V1.md)
