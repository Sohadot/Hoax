"""Structured interpretability auditing for Controlled Internal Prototype v0."""

from __future__ import annotations

from typing import Any

REQUIRED_FIELDS = [
    "trace_id",
    "fixture_id",
    "posture_basis",
    "protocol_step_refs",
    "standard_principle_refs",
    "evidence_condition_refs",
    "boundary_check_refs",
    "caveat_trigger_refs",
    "guardrail_rule_refs",
    "forbidden_transformation_refs",
    "no_verdict_confirmation",
    "no_score_confirmation",
    "no_subject_accusation_confirmation",
    "non_public_confirmation",
]


def audit_result(result: dict[str, Any]) -> dict[str, Any]:
    """Return structured audit status only."""
    missing_fields = [field for field in REQUIRED_FIELDS if field not in result]
    failures: list[str] = []

    if missing_fields:
        failures.extend(f"missing:{field}" for field in missing_fields)

    if not result.get("posture_basis"):
        failures.append("missing_posture_basis")
    if not result.get("protocol_step_refs"):
        failures.append("missing_protocol_step_refs")
    if not result.get("standard_principle_refs"):
        failures.append("missing_standard_principle_refs")
    if not result.get("evidence_condition_refs"):
        failures.append("missing_evidence_condition_refs")
    if not result.get("boundary_check_refs"):
        failures.append("missing_boundary_check_refs")
    if not result.get("caveat_trigger_refs"):
        failures.append("missing_caveat_trigger_refs")
    if not result.get("traceability_map"):
        failures.append("missing_traceability_map")
    else:
        traceability_map = result["traceability_map"]
        if not traceability_map.get("boundary_to_caveat_map"):
            failures.append("missing_boundary_to_caveat_map")
        if not traceability_map.get("condition_source_refs"):
            failures.append("missing_condition_source_refs")
        if result.get("guardrail_failure_flags") and not result.get("guardrail_rule_refs"):
            failures.append("missing_guardrail_rule_refs")
        if result.get("required_output_constraints") and not result.get("forbidden_transformation_refs"):
            failures.append("missing_forbidden_transformation_refs")

    if not result.get("no_verdict_confirmation", False):
        failures.append("missing_no_verdict_confirmation")
    if not result.get("no_score_confirmation", False):
        failures.append("missing_no_score_confirmation")
    if not result.get("no_subject_accusation_confirmation", False):
        failures.append("missing_no_subject_accusation_confirmation")
    if not result.get("non_public_confirmation", False):
        failures.append("missing_non_public_confirmation")

    if result.get("posture_state_candidate") == "Not Assessable" and not result.get("limitation_reason_refs"):
        failures.append("missing_not_assessable_reason_refs")
    if result.get("posture_state_candidate") == "Out of Scope" and not result.get("out_of_scope_reason_refs"):
        failures.append("missing_out_of_scope_reason_refs")

    audit_status = "pass" if not failures else "fail"
    return {
        "audit_status": audit_status,
        "missing_fields": missing_fields,
        "failures": failures,
    }
