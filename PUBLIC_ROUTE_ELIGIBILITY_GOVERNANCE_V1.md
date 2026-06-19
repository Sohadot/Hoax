# Public Route Eligibility Governance v1

## A. Purpose

This document defines the governance conditions required before a future public route may be considered eligible.

## B. Non-Purpose

This sprint does not:

- create a public route;
- create a public workbench;
- add a sitemap URL;
- add public navigation;
- modify the internal prototype;
- create an engine;
- create a classifier;
- create a detector;
- create upload functionality;
- create scoring;
- create fake/real outputs;
- create forms;
- create user inputs;
- create analytics;
- create an API;
- create monetization;
- modify DNS or Cloudflare;
- launch the Hoax.ai custom domain;
- authorize deployment;
- authorize public release.

## C. Governing Principle

Public route eligibility governance defines the conditions for future consideration. It does not create public routes.

A route can become eligible only after its boundary, purpose, risk, sitemap status, navigation status, and non-operational claims are governed.

## D. Eligibility Definition

Public route eligibility is a pre-route governance state where a future route may be evaluated for public suitability only after its purpose, claim boundary, audience, sitemap status, navigation status, source posture, risk posture, non-operational constraints, accessibility baseline, SEO boundary, and public-surface implications are explicitly governed.

## E. Eligibility Is Not

Eligibility is not:

- route creation;
- route approval;
- sitemap inclusion;
- navigation inclusion;
- public workbench launch;
- engine readiness;
- classifier readiness;
- tool readiness;
- deployment readiness;
- DNS readiness;
- Cloudflare readiness;
- custom domain readiness;
- monetization readiness;
- public release readiness.

## F. Required Route Eligibility Questions

Any future public route must answer:

1. What is the route's public purpose?
2. What is the route not allowed to imply?
3. Is the route informational, reference, governance, diagnostic, tool, or operational?
4. Does the route require source-backed claims?
5. Does the route require structured data?
6. Does the route create public-surface risk?
7. Does the route imply engine, classifier, upload, scoring, fake/real, API, analytics, or public tool behavior?
8. Is the route sitemap-eligible?
9. Is the route navigation-eligible?
10. Is the route internally linked only after governance?
11. Does the route require public-route readiness validation?
12. Does the route require deployment, DNS, or Cloudflare governance?
13. Does the route depend on the locked internal prototype?
14. Does the route expose or link the internal prototype?
15. Does the route preserve artifact-subject separation?
16. Does the route preserve evidence posture rather than verdict framing?
17. Does the route avoid detector, scanner, upload, score, and fake/real language?

## G. Route Eligibility States

- not_considered
- governance_required
- boundary_defined
- eligibility_candidate
- eligibility_under_review
- eligibility_validated
- eligible_for_route_creation_sprint
- blocked_for_public_surface_risk
- blocked_for_operational_implication
- blocked_for_source_gap
- blocked_for_sitemap_or_navigation_gap
- blocked_for_engine_classifier_upload_scoring_implication

No state may create a route. Even eligibility_validated may only allow a future route creation sprint, not automatic creation.

## H. Route Types

1. Reference Route
2. Governance Route
3. Language Route
4. Methodology Route
5. Static Explanatory Route
6. Public Workbench Route
7. Diagnostic Route
8. Tool Route
9. Engine Route
10. Upload Route
11. API Route

Reference, governance, language, methodology, and static explanatory routes may be eligible only after route-specific boundary review.

Public workbench, diagnostic, tool, engine, upload, and API routes remain blocked until separate governance exists.

No route type is created in Sprint 44.

## I. Public Workbench Route Boundary

A public workbench route is not eligible by default. It requires separate public workbench governance, engine/classifier non-authorization review, upload/scoring prohibition or governance, public safety audit, privacy review, accessibility review, source/claim review, route readiness validation, sitemap governance, navigation governance, and deployment governance.

## J. Internal Prototype Boundary

The internal static prototype remains:

- internal;
- static;
- non-public;
- non-operational;
- not route-registered;
- not sitemap-listed;
- not publicly linked;
- not a route candidate by default;
- not a public workbench;
- not a launch surface.

Public route eligibility governance must not expose, route, index, or link the internal prototype.

## K. Sitemap Eligibility Boundary

A route is not sitemap-eligible unless:

- it exists;
- it is public by governance;
- it has exactly one canonical purpose;
- it has no blocked capability implication;
- it has sufficient substance;
- it has approved metadata;
- it has source/claim policy compliance where needed;
- it has route registry approval;
- it has public link governance;
- it has passed route readiness validation.

Sprint 44 does not add sitemap URLs.

## L. Navigation Eligibility Boundary

A route is not navigation-eligible unless:

- it has passed public route eligibility validation;
- it has passed route creation governance;
- it has passed public route readiness validation;
- it has a safe public purpose;
- it does not imply engine/classifier/upload/scoring/API behavior unless separately governed;
- it preserves Hoax.ai's evidence posture boundary.

Sprint 44 does not add navigation links.

## M. Maturity

version: v1.0.0  
status: public_route_eligibility_governance_created  
maturity: eligibility_governance_only_no_route_no_sitemap_no_public_release_no_engine_no_classifier
