# Hoax.ai Link and Route Integrity Policy

**Version:** v1.0.0  
**Status:** governed_internal_route_link_policy  
**Maturity:** pre_expansion_hardening  
**Decision:** DEC-025

## A. Purpose

This policy governs route, sitemap, canonical, and internal link integrity for Hoax.ai before reference expansion or SEO work.

## B. Non-Purpose

This policy does **not**:

- create new routes;
- create public reference pages;
- create SEO expansion;
- create public deployment readiness;
- create a classifier;
- create a tool;
- create upload functionality;
- create monetization;
- create DNS or Cloudflare work.

## C. Governing Principle

**A reference asset cannot scale until its routes and links are governed.**

**No route without registry. No link without target. No sitemap without live eligibility.**

## D. Route Integrity Rules

- Every public route must exist in `data/route-registry.json`.
- Every route must have a unique `route_id`.
- Every route must have a path, route_type, status, index_policy, canonical_url, sitemap eligibility, and deployment status.
- Future routes must not appear in `sitemap.xml`.
- Blocked routes must not appear in public navigation.
- Planned routes must not appear as live routes.

## E. Sitemap Integrity Rules

- `sitemap.xml` may include only registered routes.
- `sitemap.xml` may include only sitemap-eligible routes.
- `sitemap.xml` may not include planned, blocked, future, draft, or internal-only routes.
- `sitemap.xml` must not contain placeholder URLs.
- `sitemap.xml` must not imply external deployment completion if deployment is deferred.
- Current sitemap may contain only the homepage route until further route governance is adopted.

## F. Canonical Integrity Rules

- Each public route must have one canonical URL.
- Canonical must align with `data/route-registry.json`.
- Canonical must not point to a future or unapproved route.
- Canonical must not imply deployment completion beyond current deployment status.
- Canonical policy must remain consistent until external deployment gate is passed.

## G. Internal Link Integrity Rules

- No internal link may point to a missing route.
- No internal link may point to a planned route unless explicitly marked as non-public/internal documentation.
- No public navigation may contain future routes.
- No orphan public route is allowed after multi-route expansion begins.
- No route may be indexable without internal linking policy.
- Internal governance markdown links should point to existing files where practical.

## H. Anchor and Fragment Rules

- Public HTML fragment links must target existing IDs.
- Empty hash links are prohibited unless explicitly justified.
- Placeholder anchors are prohibited.
- Navigation anchors must resolve inside the same page or to a registered route.

## I. Deployment Status Rules

- `external_deployment_deferred` remains valid.
- Deployment-deferred route status must not be treated as validation failure.
- Deployment-ready status may not be set until a later deployment readiness gate.
- No DNS or Rick-domain instruction is allowed through this policy.

## J. Maturity

| Field | Value |
|-------|-------|
| Version | v1.0.0 |
| Status | governed_internal_route_link_policy |
| Maturity | pre_expansion_hardening |

## Machine-Readable Sources

- Policy: `data/link-route-integrity-policy.json`
- Link graph: `data/internal-link-graph.json`
- Validator: `validators/validate_link_route_integrity.py`

## Related Governance

- DEC-025
- `data/route-registry.json`
- `validators/validate_all.py` includes route/link validation
