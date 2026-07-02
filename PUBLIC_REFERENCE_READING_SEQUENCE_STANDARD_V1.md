# Public Reference Reading Sequence Standard v1

**Decision:** DEC-135  
**Sprint:** Sprint 117  
**Status:** Active standard

## Standard statement

Public reading sequences may guide reference navigation across Hoax.ai, but must not create workflows, rankings, assessments, procedures, verdicts, scores, detections, operational instructions, case evaluations, or transaction surfaces.

## Route constraints

- Exactly one route for Sprint 117: `/reading-sequences/`.
- No child routes under `/reading-sequences/`.
- Static HTML only; no JavaScript, forms, upload behavior, API behavior, dashboards, graph tools, scorecards, or rating behavior.

## Required depth and metadata

- Minimum visible word count: 2,000 words.
- Exactly one H1.
- Canonical URL required.
- Meta description required.
- Open Graph title and description required.

## Required sections

The reading-sequence route must include:

1. Reference summary
2. Purpose of reading sequences
3. How to use this page
4. What reading sequences are not
5. First-time reader sequence
6. Evidence condition sequence
7. AI agent retrieval sequence
8. Research reviewer sequence
9. Trust and safety reader sequence
10. Education and literacy sequence
11. Strategic reviewer sequence
12. Relation to the system map
13. Relation to the evidence condition crosswalk
14. Relation to route groups
15. What this page supports
16. What this page does not claim
17. Reference Answer
18. Source Confidence
19. Cite This Reference
20. Retrieval Capsule
21. Boundary reminder
22. Non-transactional review boundary

## Required sequence model

All seven required reading sequences must appear and must use reference navigation language only.

Allowed navigation wording:

- reading sequence
- reference order
- orientation path
- companion reading
- retrieval-safe path
- citation-safe reading
- boundary-safe navigation
- suggested reading order
- reference navigation

Forbidden unsafe wording unless explicitly negated/prohibitive:

- workflow
- assessment path
- decision path
- decision tree
- investigation procedure
- operational procedure
- risk ranking
- severity order
- confidence order
- verification workflow
- due diligence sequence
- case review process

## Linking requirements

The route must link to homepage, system map, evidence-condition hub, evidence-condition crosswalk, core concept routes, route-group routes, audience-path routes, and strategic/reviewer routes as navigation companions only.

## Boundary requirements

Reading-sequence pages must preserve:

- non-verdict behavior
- non-scoring behavior
- non-detector behavior
- non-workflow behavior
- non-operational behavior
- non-transactional review behavior

## Closure requirements

Sprint 117 is complete only when the route is live, registries and sitemap are aligned at 101 routes, validator wiring is complete, and all validation/harness checks pass.
