# Hoax.ai Publisher Dry-Run Harness

**Version:** v1.0.0  
**Status:** governed_internal_publisher_dry_run_harness  
**Maturity:** candidate_logic_test_only_no_publication  
**Decision:** DEC-034

## A. Purpose

The Publisher Dry-Run Harness validates publisher logic using internal dry-run cases before any actual candidate pack, draft generation, route creation, sitemap expansion, or public release.

## B. Non-Purpose

The dry-run harness does **not**:

- publish content;
- create public pages;
- create draft pages;
- create candidate registry entries;
- create public routes;
- expand sitemap;
- generate SEO pages;
- deploy anything;
- enable DNS or Cloudflare;
- create public classifier functionality;
- create upload, scoring, forms, analytics, APIs, or monetization;
- create external factual claims.

## C. Governing Principle

**The dry-run may test publisher logic. It must not create publishable content.**

**A publisher is not trusted because it can generate. It is trusted because it can refuse.**

## D. Dry-Run Scope

The dry-run may test:

- candidate packet shape;
- page family assignment;
- reference thesis presence;
- claim scope presence;
- source scope presence;
- semantic SEO role presence;
- prohibited content rejection;
- route request rejection;
- sitemap request rejection;
- draft request rejection;
- publication request rejection;
- state transition rules;
- required gate dependencies;
- pass/fail expected outcomes.

The dry-run may not:

- write page files;
- write draft files;
- add real candidates;
- mutate route registry;
- mutate sitemap;
- approve publication;
- generate long-form content;
- generate public SEO metadata for actual routes.

## E. Candidate Packet Definition

A dry-run candidate packet is an internal test object that resembles a future publisher candidate enough to test governance logic, but is not a real candidate, not a draft, not a route, not a page, and not publishable.

## F. Required Candidate Packet Fields

Each dry-run packet must include:

- dry_run_case_id;
- fictional;
- candidate_shape_only;
- page_family;
- reference_thesis;
- purpose_statement;
- definition_scope_summary;
- governance_boundary_summary;
- claim_scope_summary;
- source_scope_summary;
- semantic_seo_role;
- prohibited_misreading_notes;
- requested_route_action;
- requested_sitemap_action;
- requested_draft_action;
- expected_result;
- expected_state;
- expected_failure_reason if expected_result is fail.

## G. Required Failure Classes

The harness must reject candidate packets that:

- request route creation;
- request sitemap expansion;
- request draft creation before approval;
- lack reference thesis;
- lack claim scope;
- lack source scope;
- lack governance boundary;
- use keyword-only SEO logic;
- use search-volume-first logic;
- imply active detector/tool/public classifier/upload/scoring;
- contain fake/real verdict framing;
- contain subject accusation;
- contain unsupported external factual claim;
- claim first-in-world or impossible-to-copy authority;
- request publication directly;
- bypass validation gates;
- use schema/tool/service/product language before gates.

## H. Required Passing Case Meaning

A passing dry-run case means only:

- the candidate packet shape satisfies internal dry-run logic;
- the packet would be eligible for future human/governance review as a candidate-shaped object.

A passing dry-run case does not mean:

- a candidate is approved;
- a draft can be generated;
- a page can be created;
- a route can be added;
- a sitemap can be expanded;
- publication is allowed;
- SEO expansion is allowed.

## I. Publisher Status After Sprint 16

After this sprint:

- publisher dry-run harness exists;
- publisher remains blocked from public output;
- future candidate pack may be considered in a later sprint;
- direct publishing remains blocked;
- draft generation remains blocked unless a later sprint explicitly permits internal drafts.

## J. Maturity

| Field | Value |
|-------|-------|
| Version | v1.0.0 |
| Status | governed_internal_publisher_dry_run_harness |
| Maturity | candidate_logic_test_only_no_publication |

## Machine-Readable Sources

- Policy: `data/publisher-dry-run-policy.json`
- Cases: `data/publisher-dry-run-cases.json`
- Expected results: `data/publisher-dry-run-expected-results.json`
- Validator: `validators/validate_publisher_dry_run.py`
