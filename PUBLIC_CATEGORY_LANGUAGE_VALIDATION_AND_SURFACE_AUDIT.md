# Hoax.ai Public Category Language Validation and Surface Audit

**Version:** v1.0.0  
**Status:** governed_public_category_language_validation  
**Maturity:** language_validation_only_no_engine_no_classifier_no_tool  
**Decision:** DEC-045

## A. Purpose

This document validates Hoax.ai’s first public category language layer after Sprint 26.

## B. Non-Purpose

This sprint does **not** create new public pages, individual term pages, new reference pages, public engine, public classifier, public tool, upload functionality, scoring, fake/real outputs, forms, analytics, API, monetization, DNS/Cloudflare changes, custom domain launch, or broader publication authorization.

## C. Governing Principle

**A public language layer must make the category legible without making the tool appear present.**

**The language surface may prepare future engine governance, but it must not imply engine capability.**

## D. Language Surface Definition

The public category language surface is the visible public route and supporting governance records that explain Hoax.ai’s vocabulary, term statuses, relation logic, and non-verdict boundaries before any public engine, classifier, upload workflow, or scoring system exists.

## E. Language Surface Is Not

The language surface is not:

- a public engine;
- a classifier;
- a detector;
- an upload workflow;
- a scoring interface;
- a fake/real verdict system;
- a fact-checking service;
- a software product;
- a public API;
- a monetized service;
- a launch of the custom domain.

## F. Audit Scope

Audit exactly:

- `/language/`
- homepage root (link integrity to `/language/` only)
- `/reference/evidence-posture/` (link integrity to `/language/` only)
- `/reference/artifact-subject-separation/` (link integrity to `/language/` only)
- `sitemap.xml`
- route registry
- internal link graph
- category language term registry
- category language relation map
- public category language layer record
- metadata and JSON-LD boundary
- visible language boundary
- forbidden capability implications

No additional page or route may enter audit scope.

## G. Required Validation Dimensions

Twenty-five validation dimensions are recorded in `data/public-category-language-validation-results-v1.json`, including Hoax-Specific Language Ownership Integrity.

## H. Allowed Audit Outcomes

- public_category_language_validated
- public_category_language_validated_with_minor_corrections
- needs_minor_language_surface_correction
- needs_major_language_surface_correction
- blocked_for_engine_implication
- blocked_for_classifier_implication
- blocked_for_metadata_overclaim
- blocked_for_route_or_sitemap_mismatch
- blocked_for_term_status_drift
- blocked_for_relation_boundary_issue

No outcome may authorize engine, classifier, tool, upload, scoring, DNS, Cloudflare, custom domain launch, monetization, or broader publication.

## I. Expected Sprint 27 Outcome

**public_category_language_validated**

## J. Post-Sprint Status

After Sprint 27:

- `/language/` remains public;
- homepage and reference links remain valid;
- term registry and relation map remain governed;
- public engine remains blocked;
- public classifier remains blocked;
- public tool remains blocked;
- upload/scoring/API/forms/analytics remain blocked;
- DNS/Cloudflare/custom domain launch remain blocked;
- next phase may become Evidence Posture Workbench Governance v1.

## K. Maturity

- version: v1.0.0
- status: governed_public_category_language_validation
- maturity: language_validation_only_no_engine_no_classifier_no_tool

## Hoax-Specific Language Ownership Test

The language layer must make Hoax.ai’s way of thinking recognizable, not merely list common trust-related terms.

A term belongs to Hoax.ai’s category language only when it has a governed definition, a system function, a boundary, a relation role, and a future output implication.

This test asks whether the language layer is merely descriptive or whether it creates a recognizable Hoax.ai conceptual grammar.

A term passes the ownership test only if:

1. It has a definition that is sharper than ordinary public usage.
2. It performs a role inside Hoax.ai’s system.
3. It constrains what Hoax.ai may and may not say.
4. It relates to at least one other Hoax.ai term.
5. It prevents a specific misuse or false implication.
6. It can later shape workbench output without becoming a verdict.
7. It remains non-engine, non-classifier, non-upload, and non-scoring.
8. It strengthens category ownership rather than behaving like a generic glossary entry.

Expected result: **hoax_governed_language_validated**

Not yet classified as:

- hoax_owned_language_final
- category_language_complete
- engine_language_ready_final

Sprint 27 validates that Hoax.ai’s public language layer has begun to express a proprietary conceptual grammar. It does not claim that the language is final, impossible to imitate, or ready for public engine outputs.

## Machine-Readable Sources

- Policy: `data/public-category-language-validation-policy.json`
- Audit: `data/public-category-language-surface-audit-v1.json`
- Results: `data/public-category-language-validation-results-v1.json`
- Validator: `validators/validate_public_category_language_validation.py`
