# Targeted Fixture Expansion Admission Log v1

## Admission Log Statement

Every Sprint 76 fixture was admitted only after referencing a named Sprint 75 coverage gap and completing required metadata fields.

## Fixture Admission Table

| Fixture ID | Coverage Gap Reference | Expansion Reason | Posture | Admission |
|------------|---------------------|------------------|---------|-----------|
| SYN-FIX-011-TRACEABILITY-CAVEAT | traceability_caveat family has no dedicated fixture activation | Close traceability_caveat gap | Qualified | Admitted |
| SYN-FIX-012-PROVENANCE-CONTEXT-COMPOUND | compound boundary interactions are absent | Provenance + context compound stress | Limited | Admitted |
| SYN-FIX-013-DRIFT-LIMITATION-COMPOUND | compound boundary interactions are absent | Drift + limitation compound stress | Limited | Admitted |
| SYN-FIX-014-ATTRIBUTION-OUTPUT-BOUNDARY | output_boundary stress beyond single out-of-scope fixture is partial | Attribution/output interaction | Qualified | Admitted |
| SYN-FIX-015-SOURCE-TRACEABILITY-CHAIN | source/traceability/chain caveat gap | Combined source/traceability/chain weakness | Limited | Admitted |
| SYN-FIX-016-NOT-ASSESSABLE-MULTI | not-assessable posture has limited variety beyond limitation-not-falsehood | Multi-reason not-assessable | Not Assessable | Admitted |

## Required Metadata Per Fixture

- coverage_gap_ref
- expansion_reason
- expected_allowed_posture_states
- expected_required_caveats
- expected_boundary_checks
- expected_forbidden_transformations_blocked
- expected_traceability_fields
- fixture-policy flags (all prohibited flags false, synthetic true)

## Rejection Rule

Any fixture missing required metadata or referencing a non-named gap is rejected and must not be merged.
