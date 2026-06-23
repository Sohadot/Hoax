# Sprint 88 — Public Reference Source Confidence Layer v1

**Status:** COMPLETE — 2026-06-23  
**Decision:** DEC-106  
**Gate:** G88

## Goal

Strengthen Hoax.ai public reference integrity by declaring governed support types on homepage and ten Sprint 84/85 production pages — so humans and AI agents know what each page supports and what it does not support — without new routes, sitemap expansion, registry inflation, upload, scoring, verdicts, detector claims, verification outputs, public API, automated reports, JavaScript, or forms.

## Problem Statement

After Sprint 87 connected utilities and reference units into a coherent authority link graph, traversal improved — but category misreading risk remained. A definition page could still be quoted as verification. A manual checklist could still be described as an analyzer. Synthetic examples could be mistaken for evaluated cases. AI agents retrieving isolated pages lacked explicit support-type signals separate from definitional prose.

Sprint 88 closes that gap by adding a source-confidence layer on the existing eleven-page update surface.

## Deliverables

### Governance and policy

- PUBLIC_REFERENCE_SOURCE_CONFIDENCE_LAYER_V1.md
- PUBLIC_SOURCE_CONFIDENCE_COMPONENT_STANDARD_V1.md
- PUBLIC_SOURCE_CONFIDENCE_AUDIT_V1.md
- SPRINT_88_PUBLIC_REFERENCE_SOURCE_CONFIDENCE_LAYER_V1.md

### Data records

- data/public-reference-source-confidence-layer-v1.json
- data/public-reference-source-confidence-layer-v1.schema.json

### Validation

- validators/validate_public_reference_source_confidence_layer_v1.py
- validators/validate_all.py — Sprint 88 validator registered

### Production HTML updates (10 pages + homepage)

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

**Homepage:**

- index.html — source-confidence component and boundary posture verified

### Decision and claim artifacts

- DEC-106 in DECISION_LOG.md
- CLAIM entry for source-confidence layer adoption
- PUB-GATE-0082 (companion publisher gate record)

## Post-Sprint Surface

| Metric | Value |
|--------|-------|
| Sitemap URLs | 29 (unchanged) |
| Route registry entries | 29 (unchanged) |
| New public routes | 0 |
| Updated production pages | 10 + homepage |
| Allowed support types | 5 |
| Forbidden support types | 9 |

## Gate G88 Criteria

Gate G88 passes when all criteria below are met and `validators/validate_all.py` returns PASS.

### G88-1 — No route inflation

- [ ] `new_public_routes_added` is false in layer JSON record
- [ ] Sitemap count remains 29
- [ ] Route registry count remains 29
- [ ] No candidate SEO authority map paths added as live routes

### G88-2 — Homepage source-confidence component

- [ ] Homepage includes human-readable source-confidence block with required fields
- [ ] Homepage includes AI-readable source-confidence capsule
- [ ] Primary support type declared per component standard
- [ ] **Not a score** and **Not verification** explicit in capsule
- [ ] Non-verdict boundary language preserved
- [ ] Sprint 87 reference graph intact

### G88-3 — Required components on updated pages

- [ ] `support_type` — correct enum per route on all eleven surfaces
- [ ] `page_support_statement` — page-specific on all eleven surfaces
- [ ] `does_not_support` — minimum three negations on all eleven surfaces
- [ ] `non_verdict_reminder` in human block on all eleven surfaces
- [ ] `ai_source_confidence_capsule` on all eleven surfaces
- [ ] `not_a_score` explicit in capsule on all eleven surfaces
- [ ] `not_verification` explicit in capsule on all eleven surfaces
- [ ] `route` field matches registry on all eleven surfaces

### G88-4 — Support type integrity

- [ ] Five reference/utility routes use assigned types from layer policy table
- [ ] `/synthetic-examples/` uses Synthetic Example
- [ ] `/why-hoax-ai-is-not-a-detector/` uses Boundary Statement
- [ ] No forbidden support types appear in components
- [ ] No forbidden phrasing in Supports or Support type fields
- [ ] Thin-component prevention rules satisfied

### G88-5 — Not score / not verification boundary

- [ ] `source_confidence_is_not_score` is true in layer JSON
- [ ] `source_confidence_is_not_verification` is true in layer JSON
- [ ] No numeric confidence ratings or tier labels introduced
- [ ] No verification, truth-certification, or detection language as page output claims

### G88-6 — Forbidden behavior boundary

- [ ] No upload, score, verdict, detector claim, public API, automated report, JavaScript, forms, analytics, monetization, or real-world case evaluation introduced
- [ ] All `forbidden_public_behavior` entries in layer JSON remain false / not authorized
- [ ] Sprint 87 link-graph components remain present and uncontradicted

### G88-7 — Governance and validation

- [ ] All four Sprint 88 markdown deliverables present
- [ ] Layer JSON validates against schema
- [ ] `validators/validate_public_reference_source_confidence_layer_v1.py` passes
- [ ] `validators/validate_all.py` passes
- [ ] DEC-106 recorded in DECISION_LOG.md

## Completion Checklist

### Production

- [x] Homepage source-confidence component with human block and AI capsule
- [x] Four utility pages updated with Manual Utility Guidance or Synthetic Example components
- [x] Six reference pages updated with Conceptual Definition or Boundary Statement components
- [x] Page-specific support statements on all updated pages
- [x] Does-not-support negations on all updated pages
- [x] Sprint 87 link-graph elements preserved on all ten non-homepage pages

### Data and policy

- [x] public-reference-source-confidence-layer-v1.json records DEC-106, Sprint 88, 29/29 counts
- [x] Schema enforces allowed/forbidden support types and authorization flags
- [x] PUBLIC_REFERENCE_SOURCE_CONFIDENCE_LAYER_V1.md — layer policy
- [x] PUBLIC_SOURCE_CONFIDENCE_COMPONENT_STANDARD_V1.md — operational component standard

### Validation

- [x] Sprint 88 validator implemented
- [x] validate_all.py includes Sprint 88 validator
- [x] PUBLIC_SOURCE_CONFIDENCE_AUDIT_V1.md documents PASS
- [x] validate_all.py — PASS
- [x] Internal prototype harnesses — PASS

### Governance records

- [x] DEC-106 adopted
- [x] Gate G88 criteria documented
- [x] Sprint record complete (this document)
- [x] Publisher gate companion recorded

## Non-Authorization

Sprint 88 does not authorize:

- New public routes or sitemap expansion
- Source-confidence components on legacy `/reference/`, language, standard, protocol, or interface pages
- Engine, classifier, or automated analysis behavior
- Upload workflows, scoring, or verdict outputs
- Verification, truth certification, or numeric confidence products
- Public API, forms, or JavaScript interaction
- DNS, Cloudflare, custom domain, or deployment changes
- Analytics, cookies, tracking, or monetization
- Real-world case evaluation on the public surface
- Forbidden support types from layer JSON

## Relationship to Prior Sprints

| Sprint | Contribution | Sprint 88 relationship |
|--------|--------------|------------------------|
| Sprint 84 (DEC-102) | Four utility routes | Utilities gain explicit Manual Utility Guidance / Synthetic Example declarations |
| Sprint 85 (DEC-103) | Six reference routes | Reference units gain Conceptual Definition / Boundary Statement declarations |
| Sprint 87 (DEC-105) | Authority internal linking | Link graph preserved; source-confidence layer adds support-type metadata |
| Sprint 53 (DEC-071) | `/reference/source-confidence/` | Concept page exists; Sprint 88 layer is page-role labeling, not redefinition of evidence dimension |

## Next Phase

Candidate next work (not authorized by Sprint 88):

- Source-confidence components on twelve legacy `/reference/` pages and language layer
- Governed support-type index across full twenty-nine-URL surface without route inflation
- Next reference production batch per PUBLIC_REFERENCE_PRODUCTION_PLAN_V1.md — requires separate sprint, registry, and gate approval

Until then, the eleven-page source-confidence layer is the embodied support-type declaration system for homepage, utilities, and Sprint 85 reference routes at twenty-nine URLs.

## Validation

`validators/validate_all.py` — **PASS** required  
Internal prototype harnesses — **PASS** required  
Source confidence audit — **PASS** (see PUBLIC_SOURCE_CONFIDENCE_AUDIT_V1.md)
