"""Output admissibility contract for Controlled Internal Prototype v0."""

from __future__ import annotations

from typing import Any

from output_guardrail_checker import scan_text_for_prohibited

ADMISSIBILITY_REQUIREMENTS = [
    "posture_basis_present",
    "evidence_condition_refs_present",
    "protocol_refs_present",
    "standard_refs_present",
    "boundary_checks_complete",
    "caveats_preserved",
    "guardrail_blocks_present",
    "forbidden_transformations_blocked",
    "traceability_refs_present",
    "non_verdict_confirmation_present",
    "non_score_confirmation_present",
    "non_public_confirmation_present",
    "no_subject_accusation",
    "no_report_shape",
    "no_result_card_shape",
    "no_public_action_recommendation",
    "no_certification_language",
    "no_detector_language",
]

ADMISSIBILITY_STATUS_VOCABULARY = [
    "admissible_internal",
    "inadmissible_missing_basis",
    "inadmissible_missing_caveat",
    "inadmissible_boundary_collapse",
    "inadmissible_guardrail_failure",
    "inadmissible_traceability_gap",
    "inadmissible_report_shape",
    "inadmissible_public_output_risk",
    "repair_required",
    "not_assessable_for_output",
]

FORBIDDEN_OUTPUT_SHAPES = [
    "result card",
    "public report",
    "report output",
    "report-shape",
    "result-card",
]

REPORT_SHAPE_MARKERS = ("result card", "public report", "report output", "report-shape")
DETECTOR_MARKERS = ("detection result", "detector-style", "classifier result", "scanner result")
CERTIFICATION_MARKERS = ("certified", "verification complete", "proven conclusion")
ACCUSATION_MARKERS = ("subject guilt", "guilty", "accusation transfer", "fraud accusation")


def _output_candidate_text(result: dict[str, Any]) -> str:
    parts = [
        result.get("posture_state_candidate"),
        result.get("not_assessable_reason"),
        result.get("out_of_scope_reason"),
    ]
    return " ".join(str(part) for part in parts if part is not None).lower()


def _requirement_checks(result: dict[str, Any]) -> dict[str, bool]:
    output_text = _output_candidate_text(result)
    boundary_checks = result.get("active_boundary_checks") or {}
    checks = {
        "posture_basis_present": bool(result.get("posture_basis")),
        "evidence_condition_refs_present": bool(result.get("evidence_condition_refs")),
        "protocol_refs_present": bool(result.get("protocol_step_refs")),
        "standard_refs_present": bool(result.get("standard_principle_refs")),
        "boundary_checks_complete": bool(boundary_checks) and bool(result.get("boundary_check_refs")),
        "caveats_preserved": bool(result.get("triggered_caveats") or result.get("caveat_trigger_refs")),
        "guardrail_blocks_present": result.get("validation_status") != "guardrail_blocked",
        "forbidden_transformations_blocked": bool(result.get("forbidden_transformation_refs")),
        "traceability_refs_present": bool(result.get("trace_id")) and bool(result.get("traceability_map")),
        "non_verdict_confirmation_present": bool(result.get("no_verdict_confirmation")),
        "non_score_confirmation_present": bool(result.get("no_score_confirmation")),
        "non_public_confirmation_present": bool(result.get("non_public_confirmation")),
        "no_subject_accusation": bool(result.get("no_subject_accusation_confirmation", True)),
        "no_report_shape": not any(marker in output_text for marker in ("public report", "report output", "report-shape")),
        "no_result_card_shape": "result card" not in output_text,
        "no_public_action_recommendation": "public action" not in output_text and "moderation action" not in output_text,
        "no_certification_language": not any(marker in output_text for marker in CERTIFICATION_MARKERS),
        "no_detector_language": not any(marker in output_text for marker in DETECTOR_MARKERS),
    }
    if scan_text_for_prohibited(output_text):
        checks["guardrail_blocks_present"] = False
    if result.get("guardrail_failure_flags"):
        checks["guardrail_blocks_present"] = False
    return checks


def _resolve_status(checks: dict[str, bool], result: dict[str, Any]) -> str:
    output_text = _output_candidate_text(result)
    if any(marker in output_text for marker in ("result card", "public report", "report output")):
        return "inadmissible_report_shape"
    if not checks.get("non_public_confirmation_present"):
        return "inadmissible_public_output_risk"
    if not checks.get("non_verdict_confirmation_present") or not checks.get("non_score_confirmation_present"):
        return "inadmissible_guardrail_failure"
    if not checks.get("guardrail_blocks_present"):
        return "inadmissible_guardrail_failure"
    if not checks.get("traceability_refs_present"):
        return "inadmissible_traceability_gap"
    if not checks.get("posture_basis_present"):
        return "inadmissible_missing_basis"
    if not checks.get("caveats_preserved"):
        return "inadmissible_missing_caveat"
    if not checks.get("boundary_checks_complete"):
        return "inadmissible_boundary_collapse"
    if not all(checks.values()):
        return "repair_required"
    return "admissible_internal"


def evaluate_output_admissibility(result: dict[str, Any]) -> dict[str, Any]:
    """Evaluate whether an internal structured result satisfies the admissibility contract."""
    checks = _requirement_checks(result)
    status = _resolve_status(checks, result)
    failed = [name for name, passed in checks.items() if not passed]
    return {
        "fixture_id": result.get("fixture_id"),
        "trace_id": result.get("trace_id"),
        "admissibility_status": status,
        "requirement_checks": checks,
        "failed_requirements": failed,
        "repair_required": status not in ("admissible_internal", "not_assessable_for_output"),
        "non_verdict_confirmation": bool(result.get("no_verdict_confirmation")),
        "non_score_confirmation": bool(result.get("no_score_confirmation")),
        "non_public_confirmation": bool(result.get("non_public_confirmation")),
        "admissibility_validation_status": "pass" if status == "admissible_internal" else "fail",
    }


def evaluate_results_batch(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Evaluate admissibility for a batch of internal structured results."""
    return [evaluate_output_admissibility(result) for result in results]
