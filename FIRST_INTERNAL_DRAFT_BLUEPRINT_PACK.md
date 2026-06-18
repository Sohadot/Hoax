# Hoax.ai First Internal Draft Blueprint Pack

**Version:** v1.0.0  
**Status:** governed_internal_draft_blueprint_pack  
**Maturity:** blueprint_records_only_no_drafts_no_routes_no_publication  
**Decision:** DEC-038

## A. Purpose

This document introduces the first internal draft blueprint records for future Hoax.ai reference drafts.

## B. Non-Purpose

This blueprint pack does **not**:

- create draft prose;
- create internal draft files;
- create public pages;
- create route files;
- activate routes;
- expand sitemap.xml;
- create public metadata;
- create public navigation links;
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

**A draft blueprint may authorize structure. It must not become prose.**

**The first blueprint pack must define what may be written before anything is written.**

## D. Blueprint Record Definition

An internal draft blueprint record is a non-public structured governance record that maps an evaluated reference candidate to a future draft structure. It defines required sections, claim scope, source scope, semantic SEO boundary, internal link plan, prohibited misreadings, structured data boundary, required gates, and non-authorization status before any draft language exists.

## E. Blueprint Record Is Not

A blueprint record is not:

- a draft;
- a page;
- prose;
- a route;
- a sitemap entry;
- public metadata;
- a URL;
- publication approval;
- SEO expansion;
- source verification;
- truth certification;
- deployment readiness.

## F. Pack Scope

First pack: **4 blueprint records**

| Blueprint ID | Candidate | Rationale |
|--------------|-----------|-----------|
| DRAFT-BLUEPRINT-0001 | REF-CAND-0001 Evidence Posture | Foundational vocabulary anchor |
| DRAFT-BLUEPRINT-0002 | REF-CAND-0002 Artifact–Subject Separation | Foundational governance boundary |
| DRAFT-BLUEPRINT-0003 | REF-CAND-0006 Output Boundary | High-dependency boundary unit |
| DRAFT-BLUEPRINT-0004 | REF-CAND-0007 Claim and Source Traceability | High-dependency traceability unit |

**Excluded:** REF-CAND-0008 Synthetic Fragility (`needs_boundary_refinement`). REF-CAND-0003, 0004, 0005 deferred to later packs.

## G. Required Blueprint Fields

See `data/internal-draft-blueprint-pack-v1.json` and `INTERNAL_DRAFT_BLUEPRINT_GOVERNANCE.md`.

## H. Required Status Values

Every blueprint record preserves:

- blueprint_status: `blueprint_created_internal`
- draft_status: `not_draft_created`
- route_status: `not_route_created`
- sitemap_status: `not_sitemap_eligible`
- publication_status: `publication_blocked`

## I. Section Contract Rule

Blueprint records reference DRAFT-SECTION-0001 through DRAFT-SECTION-0010. Draft sections are not written in this sprint.

## J–M. Boundary Rules

Semantic SEO role, internal link plan, and claim/source scope remain internal planning only. No public metadata, public links, external factual claims, or invented sources.

## N. Pack Maturity

| Field | Value |
|-------|-------|
| Version | v1.0.0 |
| Status | governed_internal_draft_blueprint_pack |
| Maturity | blueprint_records_only_no_drafts_no_routes_no_publication |

## Machine-Readable Sources

- Policy: `data/internal-draft-blueprint-pack-policy.json`
- Pack: `data/internal-draft-blueprint-pack-v1.json`
- Registry: `data/internal-draft-blueprint-registry.json`
- Validator: `validators/validate_internal_draft_blueprint_pack.py`
