# Hoax.ai Public Reference Validation and Live Surface Audit

**Version:** v1.0.0  
**Status:** governed_public_reference_live_surface_audit  
**Maturity:** live_surface_validation_only_no_engine_no_classifier_no_broader_publication  
**Decision:** DEC-043

## A. Purpose

This document validates the first two controlled public reference pages after publication to the GitHub Pages preview surface.

## B. Non-Purpose

This sprint does **not** create new public pages, new routes, sitemap expansion beyond the existing controlled pilot, public engine, public classifier, public tool, upload, scoring, forms, analytics, API, monetization, DNS/Cloudflare changes, custom domain launch, or broader publication authorization.

## C. Governing Principle

**A public reference page must remain a reference surface, not become a tool surface.**

**Live visibility increases responsibility; it does not loosen governance.**

## D. Live Surface Definition

The live surface is the publicly visible GitHub Pages preview of Hoax.ai's current controlled reference layer, including homepage, two public reference pages, sitemap, metadata, internal links, and visible public claims.

## E. Live Surface Is Not

Live surface is not official custom-domain launch, DNS launch, Cloudflare launch, production tool deployment, classifier deployment, upload workflow, scoring workflow, public engine release, monetization launch, or broader publication approval.

## F. Audit Scope

- Homepage root
- `/reference/evidence-posture/`
- `/reference/artifact-subject-separation/`
- `sitemap.xml`
- Route registry
- Internal link graph
- Public metadata
- JSON-LD boundary
- Visible boundary language
- Forbidden public-tool implications

No additional route or page may enter audit scope.

## G. Required Validation Dimensions

Twenty validation dimensions are recorded in `data/public-reference-validation-results-v1.json`.

## H. Allowed Outcomes

- live_surface_validated_controlled_reference_pilot
- live_surface_validated_with_minor_corrections
- needs_minor_surface_correction
- needs_major_surface_correction
- blocked_for_public_tool_implication
- blocked_for_metadata_overclaim
- blocked_for_route_or_sitemap_mismatch
- blocked_for_boundary_issue

No outcome authorizes engine, classifier, upload, scoring, DNS, Cloudflare, custom domain launch, or broader publication.

## I. Expected Sprint 25 Outcome

**live_surface_validated_controlled_reference_pilot**

## J. Post-Sprint Status

The two reference pages remain public. Broader publication, public engine, public classifier, upload/scoring/API/forms/analytics, and DNS/Cloudflare/custom domain launch remain blocked. Next phase may become Public Category Language Layer v1.

## K. GitHub Pages Preview

Canonical URLs use `https://hoax.ai/` policy. GitHub Pages preview may resolve at `https://sohadot.github.io/Hoax/` when enabled. Live network verification is documented in the sprint audit; deterministic local validation does not require network access.

## Machine-Readable Sources

- Policy: `data/public-reference-live-surface-policy.json`
- Audit: `data/public-reference-live-surface-audit-v1.json`
- Results: `data/public-reference-validation-results-v1.json`
- Validator: `validators/validate_public_reference_live_surface.py`
