# Public Reference Reading Sequences v1

**Decision:** DEC-135  
**Sprint:** Sprint 117  
**Status:** Adopted — visible production route

## Reading sequences statement

Public Reference Reading Sequences v1 introduces one public route at `/reading-sequences/` that guides humans and AI agents through citation-safe, retrieval-safe, and boundary-safe reference navigation across Hoax.ai's 101-route public reference surface.

Governing sentence: Reading sequences guide reference navigation across Hoax.ai; they do not create workflows, judgments, rankings, scores, detections, operational procedures, or case assessments.

## Why this layer is needed after 100 routes

At 100 routes, reference depth creates navigation ambiguity risk. Readers can still misunderstand the surface even if each route is individually valid. Reading Sequences v1 solves orientation ambiguity by publishing seven governed reading sequences that connect existing pages by intent without adding operational behavior.

## Route created

- `/reading-sequences/` (ROUTE-0101, PUB-FILE-0101)

Public surface moves from 100 to 101 routes.

## Reading-sequence role

The route is a reference navigation surface only. It proposes suggested reading order and companion reading paths for:

1. First-time reader sequence
2. Evidence condition sequence
3. AI agent retrieval sequence
4. Research reviewer sequence
5. Trust and safety reader sequence
6. Education and literacy sequence
7. Strategic reviewer sequence

## Human usefulness

Humans can choose sequence-by-purpose instead of route-by-guessing. This reduces interpretation drift while preserving non-verdict and non-transactional boundaries.

## AI retrieval usefulness

AI agents can cite stable sequence orientation without inventing procedural or judgmental behavior. The page is retrieval-safe because it contains explicit boundary language, reference answer blocks, and clear route companions.

## Non-workflow boundary

Reading sequences are not workflows, assessment paths, decision trees, investigation procedures, operational procedures, or case-review processes.

## Non-verdict and non-transactional boundary

The page creates no score, rating, verdict, detector output, dashboard, graph tool, upload path, API behavior, report generation behavior, due-diligence room, sales page, consulting funnel, service funnel, pricing statement, transaction page, legal representation, or financial representation.

## Why this is production-first

This decision governs a visible route added in this sprint and connected to homepage, system map, crosswalk, route-group pages, and audience-path pages. It is not abstract pre-governance.
