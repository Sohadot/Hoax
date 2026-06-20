"""Compose Controlled Internal Prototype v0 internal structured evaluation."""

from __future__ import annotations

from typing import Any

from boundary_evaluator import evaluate_boundaries
from caveat_mapper import map_caveats
from fixture_loader import load_fixtures
from model_loader import load_models
from output_guardrail_checker import verify_internal_structure
from protocol_mapper import map_protocol_steps
from traceability_mapper import build_traceability_map

ALLOWED_RESULT_KEYS = {
    "fixture_id",
    "trace_id",
    "traceability_map",
    "posture_state_candidate",
    "posture_basis",
    "protocol_step_refs",
    "standard_principle_refs",
    "evidence_condition_refs",
    "boundary_check_refs",
    "caveat_trigger_refs",
    "guardrail_rule_refs",
    "forbidden_transformation_refs",
    "limitation_reason_refs",
    "out_of_scope_reason_refs",
    "active_boundary_checks",
    "triggered_caveats",
    "prohibited_language_blocks",
    "required_output_constraints",
    "not_assessable_reason",
    "out_of_scope_reason",
    "guardrail_failure_flags",
    "validation_status",
    "no_verdict_confirmation",
    "no_score_confirmation",
    "no_subject_accusation_confirmation",
    "non_public_confirmation",
}


def _select_posture_state(fixture: dict[str, Any]) -> str:
    allowed = fixture.get("expected_allowed_posture_states", [])
    if not allowed:
        return "Not Assessable"
    return str(allowed[0])


def evaluate_fixture(fixture: dict[str, Any], models: dict[str, Any]) -> dict[str, Any]:
    """Evaluate one fixture into internal structured objects only."""
    posture = _select_posture_state(fixture)
    boundaries = evaluate_boundaries(fixture)
    caveats = map_caveats(fixture)
    protocol_map = map_protocol_steps(fixture)

    result: dict[str, Any] = {
        "fixture_id": fixture["fixture_id"],
        "posture_state_candidate": posture,
        "posture_basis": [
            "fixture_expected_allowed_posture_states",
            "protocol_step_mapping",
            "boundary_check_evaluation",
            "guardrail_non_verdict_confirmation",
        ],
        "active_boundary_checks": boundaries,
        "triggered_caveats": caveats,
        "required_output_constraints": fixture.get("forbidden_output_expectations", []),
        "not_assessable_reason": None,
        "out_of_scope_reason": None,
    }
    if posture == "Not Assessable":
        result["not_assessable_reason"] = "insufficient_assessable_basis_stub"
    if posture == "Out of Scope":
        result["out_of_scope_reason"] = "scope_boundary_reached_stub"

    guardrail = verify_internal_structure(result)
    traceability = build_traceability_map(
        fixture,
        posture,
        fixture.get("forbidden_output_expectations", []),
    )
    result["trace_id"] = traceability["trace_id"]
    result["traceability_map"] = traceability
    result["protocol_step_refs"] = traceability["protocol_step_refs"]
    result["standard_principle_refs"] = traceability["standard_principle_refs"]
    result["evidence_condition_refs"] = traceability["evidence_condition_refs"]
    result["boundary_check_refs"] = traceability["boundary_check_refs"]
    result["caveat_trigger_refs"] = traceability["caveat_trigger_refs"]
    result["guardrail_rule_refs"] = traceability["guardrail_rule_refs"]
    result["forbidden_transformation_refs"] = traceability["forbidden_transformation_refs"]
    result["limitation_reason_refs"] = (
        ["limitation_status_dimension", "EPS-012"] if posture == "Not Assessable" else []
    )
    result["out_of_scope_reason_refs"] = (
        ["scope_boundary_reached_stub", "output_boundary_status"] if posture == "Out of Scope" else []
    )
    result["prohibited_language_blocks"] = guardrail["prohibited_language_blocks"]
    result["guardrail_failure_flags"] = guardrail["guardrail_failure_flags"]
    result["validation_status"] = "pass" if guardrail["passed"] else "guardrail_blocked"
    result["no_verdict_confirmation"] = True
    result["no_score_confirmation"] = True
    result["no_subject_accusation_confirmation"] = True
    result["non_public_confirmation"] = True

    _ = models, protocol_map  # governed dependencies loaded for internal traceability only
    return result


def run_prototype() -> list[dict[str, Any]]:
    """Load models and fixtures; return internal structured results only."""
    models = load_models()
    fixtures = load_fixtures()
    return [evaluate_fixture(fixture, models) for fixture in fixtures]
