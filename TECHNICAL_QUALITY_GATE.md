# Hoax.ai Technical Quality Gate

**Version:** v1.0.0  
**Status:** governed_internal_technical_quality_gate  
**Maturity:** pre_expansion_static_quality_gate  
**Decision:** DEC-027

## A. Purpose

This gate defines the minimum technical quality requirements for Hoax.ai's public static surface.

## B. Non-Purpose

This gate does **not**:

- create new routes;
- create public reference pages;
- create SEO expansion;
- create public deployment readiness;
- create DNS or Cloudflare work;
- create a classifier;
- create a public tool;
- create upload functionality;
- create forms;
- create analytics;
- create tracking;
- certify perfect security or perfect performance.

## C. Governing Principle

**Reference quality fails if technical quality is not enforceable.**

**No known unresolved critical security, privacy, technical, accessibility, or performance issues after validation.**

Do not use: perfectly secure; fully secure; no security gaps; unhackable; guaranteed safe; perfect performance.

## D. Public HTML Requirements

- valid root index.html exists;
- exactly one H1;
- html lang attribute present;
- charset meta present;
- viewport meta present;
- title present and non-empty;
- meta description present and non-empty;
- canonical link present;
- no duplicate canonical links;
- no empty href;
- no javascript: href;
- no placeholder anchors;
- no broken fragment links;
- semantic structure where practical;
- no unresolved TODO/FIXME/placeholder production text;
- no unsupported superiority claims;
- no public tool implication outside negation/prohibition context.

## E. Metadata Requirements

- title aligns with thesis surface;
- meta description does not imply an active tool;
- canonical aligns with route registry;
- Open Graph tags must not imply active tool, classifier, upload, scoring, or deployment completion;
- Twitter card tags, if present, must not overclaim;
- JSON-LD, if present, must not overclaim SoftwareApplication/Product/Service without approval.

## F. Robots and Sitemap Requirements

- robots.txt exists;
- sitemap.xml exists;
- sitemap entries map to route registry;
- sitemap must not include future or blocked routes;
- robots must not expose placeholder routes.

## G. Accessibility Requirements

- readable text structure;
- logical headings;
- no more than one H1;
- links have visible text where present;
- images have alt text or are decorative;
- no core meaning hidden in decorative visuals;
- no motion-dependent meaning;
- mobile-safe layout;
- semantic HTML where practical.

## H. Performance and Dependency Requirements

- static-first;
- readable without JavaScript;
- no external JavaScript;
- no external CSS;
- no remote fonts;
- no tracking pixels;
- no iframe embeds;
- local CSS only unless future decision approves otherwise;
- public files remain lightweight before expansion.

## I. Static Security Requirements

- no forms;
- no inputs;
- no upload fields;
- no inline event handlers;
- no script tags unless explicitly approved later;
- no external script src;
- no iframe;
- no fetch/XMLHttpRequest;
- no localStorage/sessionStorage/cookie-setting behavior;
- no payment widgets;
- no login/account code;
- no API interaction.

## J. Public Asset Reference Requirements

- all linked local CSS/assets exist;
- no missing local assets;
- no references to non-existent public routes.

## K. Technical Gate Maturity

| Field | Value |
|-------|-------|
| Version | v1.0.0 |
| Status | governed_internal_technical_quality_gate |
| Maturity | pre_expansion_static_quality_gate |

## Machine-Readable Sources

- Gate: `data/technical-quality-gate.json`
- Public files: `data/public-file-registry.json`
- Metadata: `data/html-metadata-registry.json`
- Validator: `validators/validate_technical_quality_gate.py`
