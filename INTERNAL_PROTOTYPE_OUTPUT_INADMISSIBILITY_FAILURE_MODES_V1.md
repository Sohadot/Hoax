# Internal Prototype Output Inadmissibility Failure Modes v1

## Failure Mode Statement

Inadmissibility failure modes define how internal structured results fail output admissibility when structural basis, guardrails, traceability, or output shape requirements are not intact.

## Missing Basis Failure

Occurs when posture_basis, protocol refs, or standard refs are absent. Status: inadmissible_missing_basis.

## Missing Caveat Failure

Occurs when triggered_caveats and caveat_trigger_refs are both absent. Status: inadmissible_missing_caveat.

## Boundary Collapse Failure

Occurs when active_boundary_checks or boundary_check_refs are absent. Status: inadmissible_boundary_collapse.

## Guardrail Failure

Occurs when validation_status is guardrail_blocked, guardrail_failure_flags are raised, or prohibited language appears in output candidate fields. Status: inadmissible_guardrail_failure.

## Traceability Gap Failure

Occurs when trace_id or traceability_map is missing. Status: inadmissible_traceability_gap.

## Report-Shape Failure

Occurs when output candidate fields contain result-card or public-report shape language. Status: inadmissible_report_shape.

## Public-Output-Risk Failure

Occurs when non_public_confirmation is false. Status: inadmissible_public_output_risk.

## Certification-Language Failure

Occurs when output candidate fields contain certification or proven-conclusion language. Status: repair_required or inadmissible_guardrail_failure.

## Detector-Language Failure

Occurs when output candidate fields contain detection-result or classifier language. Status: repair_required or inadmissible_guardrail_failure.

## Score Leakage Failure

Occurs when score or confidence-percentage language appears in output candidate fields. Status: inadmissible_guardrail_failure.

## Verdict Leakage Failure

Occurs when fake/real or verified-true/false language appears in output candidate fields, or no_verdict_confirmation is false. Status: inadmissible_guardrail_failure.

## Accusation-Transfer Failure

Occurs when subject-guilt or accusation language appears in output candidate fields, or no_subject_accusation_confirmation is false. Status: inadmissible_guardrail_failure.

## Required Response to Each Failure

Restore missing structural basis through repair policy. Re-run output admissibility harness and all internal prototype harnesses before commit. No public exposure is permitted.
