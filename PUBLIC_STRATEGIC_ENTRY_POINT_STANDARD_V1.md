# Public Strategic Entry Point Standard v1

## Purpose

Define minimum requirements for Hoax.ai strategic entry-point public routes.

## Route Count

Sprint 96 adds exactly six routes. Sitemap and route registry increase from 41 to 47 URLs and entries.

## Page Components

Each entry-point page must include: Reference summary, Entry purpose, Start here, Recommended path, Reference Answer, Source Confidence, Cite This Reference, Retrieval Capsule, page-end reference navigation, and Boundary reminder.

## Stable Anchors

`reference-summary`, `entry-purpose`, `start-here`, `recommended-path`, `reference-answer`, `source-confidence`, `cite-this-reference`, `retrieval-capsule`, `boundary`.

## Depth

Minimum 800 visible words per new route.

## Linking

Each page links to `/entry-points/`, homepage, at least three utility or pathway routes, and at least five reference routes.

## Prohibited Behaviors

Upload, scoring, verdict, detector claim, public API, automated report, JavaScript, forms, chatbot, generator, and real-world case evaluation remain unauthorized.

## Enforcement

`validators/validate_public_reference_strategic_entry_points_v1.py`
