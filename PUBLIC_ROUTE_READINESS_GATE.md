# Hoax.ai Public Route Readiness Gate

**Version:** v1.0.0  
**Status:** governed_public_route_readiness_gate  
**Maturity:** readiness_gate_only_no_routes_no_sitemap_no_publication  
**Decision:** DEC-041

## A. Purpose

This document governs whether reviewed internal drafts may become eligible for future controlled public route conversion.

## B. Non-Purpose

This gate does **not**:

- create public pages;
- create route files;
- activate routes;
- add candidate paths to the active route registry;
- expand sitemap.xml;
- create public metadata;
- create public navigation links;
- create public schema;
- create SEO expansion;
- create public classifier functionality;
- create a public tool;
- create upload functionality;
- create scoring;
- create forms;
- create analytics;
- deploy anything;
- enable DNS or Cloudflare;
- authorize publication.

## C. Governing Principle

**Route readiness is not route creation.**

**A draft may become eligible for public conversion only when its boundaries are stronger than its visibility.**

## D. Route Readiness Definition

Public route readiness is a non-public governance state indicating that a reviewed internal draft has passed the structural, boundary, claim/source, semantic SEO, public-surface, route-path, and non-authorization checks required before a later sprint may convert it into a public reference page.

## E. Route Readiness Is Not

Route readiness is not route creation, sitemap eligibility, public metadata approval, public navigation approval, publication approval, deployment approval, source verification, truth certification, external factual validation, engine/tool readiness, classifier readiness, upload workflow readiness, or monetization readiness.

## F. Scope

| Draft ID | Candidate | Inactive Proposed Path |
|----------|-----------|------------------------|
| DRAFT-0001 | REF-CAND-0001 Evidence Posture | `/reference/evidence-posture/` |
| DRAFT-0002 | REF-CAND-0002 Artifact–Subject Separation | `/reference/artifact-subject-separation/` |

Proposed paths remain inactive and are not added to route-registry or sitemap.xml in Sprint 23.

**Excluded:** Output Boundary, Claim and Source Traceability, Synthetic Fragility, unreviewed drafts, tool/classifier routes.

## G. Required Readiness Dimensions

1. Reviewed Draft Status  
2. Candidate Eligibility  
3. Blueprint Alignment  
4. Section Contract Compliance  
5. Reference Substance Readiness  
6. Definition and Scope Stability  
7. Governance Boundary Strength  
8. Claim Scope Discipline  
9. Source Scope Discipline  
10. Semantic SEO Restraint  
11. Proposed Route Path Safety  
12. Active Route Registry Non-Conflict  
13. Sitemap Non-Expansion  
14. Public Metadata Non-Creation  
15. Public Navigation Non-Creation  
16. Structured Data Boundary  
17. Internal Link Plan Readiness  
18. Forbidden Language Safety  
19. Public Surface Safety  
20. Non-Authorization Strength  

## H. Readiness Outcomes

Allowed outcomes: `route_readiness_passed_internal`, `route_readiness_passed_with_conditions`, `needs_minor_route_preparation`, `needs_major_route_preparation`, `blocked_for_boundary_issue`, `blocked_for_claim_source_issue`, `blocked_for_public_implication`, `blocked_for_route_conflict`.

No outcome may create routes, sitemap entries, public metadata, public navigation, publication, deployment, or public classifier/tool creation.

## I. Expected Sprint 23 Outcome

Both drafts: **route_readiness_passed_with_conditions** — eligible for a future controlled public reference pilot; public route files, metadata, sitemap, navigation, and publication require a later explicit sprint.

## J. Candidate Route Path Rule

- `proposed_route_status`: inactive_candidate_path  
- `route_status`: not_route_created  
- `sitemap_status`: not_sitemap_eligible  
- `public_metadata_status`: not_created  
- `public_navigation_status`: not_linked  
- `publication_status`: publication_blocked  
- `deployment_status`: not_deployed  

## K. Metadata Rule

Sprint 23 must not create public title, meta description, canonical, schema, Open Graph, or Twitter metadata. Internal future requirements may be described only.

## L. Post-Sprint Status

Readiness records and inactive route candidates may exist. No public pages, routes, sitemap expansion, public metadata, or navigation links. Publication and deployment remain blocked.

## Machine-Readable Sources

- Policy: `data/public-route-readiness-policy.json`
- Criteria: `data/public-route-readiness-criteria.json`
- Results: `data/public-route-readiness-v1.json`
- Route candidates: `data/public-route-candidate-registry.json`
- Validator: `validators/validate_public_route_readiness_gate.py`
