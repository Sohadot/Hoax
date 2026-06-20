# Targeted Synthetic Fixture Expansion v1

## 1. Expansion Statement

Targeted Synthetic Fixture Expansion v1 adds only gap-justified synthetic fixtures to strengthen controlled internal prototype coverage. Fixture expansion is not fixture volume; it is coverage closure.

## 2. Expansion Scope

- internal-only
- non-public
- synthetic-fixture-bound
- no public benchmark
- no public report
- no model score
- no performance ranking
- no public route
- no sitemap entry
- no real-world evaluation
- no external data
- no public explanation

## 3. Named Gap Basis

Sprint 75 gaps addressed in Sprint 76:

- traceability_caveat coverage gap
- compound boundary interaction gap
- source/traceability/chain caveat gap
- attribution/output boundary interaction gap
- not-assessable multi-reason gap
- forbidden transformation regression gap

## 4. Added Fixture Classes

| Class | Fixture ID | Gap | Posture | Key Caveats |
|-------|------------|-----|---------|-------------|
| traceability_caveat_gap_closer | SYN-FIX-011 | traceability_caveat | Qualified | traceability_caveat, source_caveat |
| provenance_context_compound_boundary | SYN-FIX-012 | compound boundary | Limited | provenance, context, limitation |
| claim_drift_limitation_compound_boundary | SYN-FIX-013 | compound boundary | Limited | drift, limitation, interpretation_risk |
| attribution_output_boundary_compound | SYN-FIX-014 | output_boundary interaction | Qualified | attribution_boundary, output_boundary |
| source_traceability_chain_weakness | SYN-FIX-015 | source/traceability/chain | Limited | source, traceability, provenance |
| not_assessable_multi_reason | SYN-FIX-016 | not-assessable variety | Not Assessable | limitation, traceability, interpretation_risk, attribution_boundary |

Each fixture declares expected boundary checks, forbidden transformations blocked, and traceability fields. Disallowed interpretations include verdict, score, fake/real label, and public report conclusions.

## 5. Coverage Delta

After Sprint 76:

- traceability_caveat family has dedicated fixture activation
- compound provenance/context and drift/limitation boundaries are tested
- attribution/output boundary interaction is strengthened
- source/traceability/chain weakness is covered
- not-assessable multi-reason variety is expanded
- guardrail regression includes forbidden-transformation vector for detection-result language

## 6. Non-Expansion Boundaries

This sprint does not authorize public benchmark, public report, public engine, output generator, score, UI, API, upload, real-world claim evaluation, or fixture use on real cases.

## 7. Future Fixture Rule

Future fixtures must cite a named coverage gap and must pass fixture-admission policy before being added.
