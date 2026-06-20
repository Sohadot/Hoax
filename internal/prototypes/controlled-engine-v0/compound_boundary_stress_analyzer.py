"""Compound boundary stress analysis for Controlled Internal Prototype v0."""

from __future__ import annotations

from typing import Any

from boundary_evaluator import evaluate_boundaries
from fixture_loader import load_fixtures
from model_loader import load_models
from prototype_core import evaluate_fixture

STRESS_CASES: list[dict[str, Any]] = [
    {
        "stress_case_id": "STRESS-001-PROVENANCE-CONTEXT-COMPOUND",
        "compound_boundary_class": "provenance_gap + context_collapse",
        "source_fixture_ids": ["SYN-FIX-012-PROVENANCE-CONTEXT-COMPOUND"],
        "required_caveat_families": ["provenance_caveat", "context_caveat", "limitation_caveat"],
        "required_boundary_checks": [
            "provenance_gap_not_manipulation_check",
            "context_collapse_not_motive_check",
        ],
        "forbidden_transformations_blocked": ["gap_to_manipulation", "context_collapse_to_motive"],
    },
    {
        "stress_case_id": "STRESS-002-DRIFT-LIMITATION-COMPOUND",
        "compound_boundary_class": "claim_drift + evidence_limitation",
        "source_fixture_ids": ["SYN-FIX-013-DRIFT-LIMITATION-COMPOUND"],
        "required_caveat_families": ["drift_caveat", "limitation_caveat", "interpretation_risk_caveat"],
        "required_boundary_checks": [
            "claim_drift_not_deception_check",
            "evidence_limitation_not_falsehood_check",
        ],
        "forbidden_transformations_blocked": ["drift_to_deception", "limitation_to_falsehood"],
    },
    {
        "stress_case_id": "STRESS-003-ATTRIBUTION-OUTPUT-BOUNDARY-COMPOUND",
        "compound_boundary_class": "attribution_boundary + output_boundary",
        "source_fixture_ids": ["SYN-FIX-014-ATTRIBUTION-OUTPUT-BOUNDARY"],
        "required_caveat_families": ["attribution_boundary_caveat", "output_boundary_caveat"],
        "required_boundary_checks": [
            "artifact_subject_separation_check",
            "attribution_boundary_no_subject_transfer_check",
            "output_boundary_no_forbidden_language_check",
        ],
        "forbidden_transformations_blocked": ["artifact_to_subject_guilt"],
    },
    {
        "stress_case_id": "STRESS-004-SOURCE-TRACEABILITY-CHAIN-COMPOUND",
        "compound_boundary_class": "source_confidence_weakness + traceability_weakness + chain_weakness",
        "source_fixture_ids": ["SYN-FIX-015-SOURCE-TRACEABILITY-CHAIN"],
        "required_caveat_families": ["source_caveat", "traceability_caveat", "provenance_caveat"],
        "required_boundary_checks": [
            "provenance_gap_not_manipulation_check",
            "interpretation_risk_not_verdict_check",
        ],
        "forbidden_transformations_blocked": ["source_weakness_to_fraud", "gap_to_manipulation"],
    },
    {
        "stress_case_id": "STRESS-005-NOT-ASSESSABLE-MULTI-REASON-COMPOUND",
        "compound_boundary_class": "not_assessable_multi_reason + interpretation_risk",
        "source_fixture_ids": ["SYN-FIX-016-NOT-ASSESSABLE-MULTI"],
        "required_caveat_families": [
            "limitation_caveat",
            "traceability_caveat",
            "interpretation_risk_caveat",
            "attribution_boundary_caveat",
        ],
        "required_boundary_checks": [
            "evidence_limitation_not_falsehood_check",
            "interpretation_risk_not_verdict_check",
        ],
        "forbidden_transformations_blocked": ["limitation_to_falsehood", "risk_to_verdict"],
    },
    {
        "stress_case_id": "STRESS-006-SYNTHETIC-FRAGILITY-OUTPUT-BOUNDARY-COMPOUND",
        "compound_boundary_class": "synthetic_fragility + output_boundary",
        "source_fixture_ids": ["SYN-FIX-003-LIMITED"],
        "required_caveat_families": ["provenance_caveat", "context_caveat", "limitation_caveat"],
        "required_boundary_checks": ["output_boundary_no_forbidden_language_check"],
        "forbidden_transformations_blocked": ["synthetic_to_fake"],
    },
    {
        "stress_case_id": "STRESS-007-LIMITATION-FORBIDDEN-TRANSFORMATION-COMPOUND",
        "compound_boundary_class": "limitation + forbidden_transformation pressure",
        "source_fixture_ids": ["SYN-FIX-010-LIMITATION-NOT-FALSEHOOD"],
        "required_caveat_families": ["limitation_caveat", "interpretation_risk_caveat"],
        "required_boundary_checks": [
            "evidence_limitation_not_falsehood_check",
            "interpretation_risk_not_verdict_check",
        ],
        "forbidden_transformations_blocked": ["limitation_to_falsehood", "risk_to_verdict"],
    },
    {
        "stress_case_id": "STRESS-008-COMPOUND-CAVEAT-ACTIVATION-PRESSURE",
        "compound_boundary_class": "compound_caveat_activation_pressure",
        "source_fixture_ids": ["SYN-FIX-011-TRACEABILITY-CAVEAT"],
        "required_caveat_families": ["traceability_caveat", "source_caveat"],
        "required_boundary_checks": [
            "artifact_subject_separation_check",
            "provenance_gap_not_manipulation_check",
        ],
        "forbidden_transformations_blocked": ["confidence_to_certification"],
    },
]

COLLAPSE_FAILURE_MARKERS = [
    "manipulation",
    "motive",
    "deception",
    "falsehood",
    "subject guilt",
    "result card",
    "fake",
    "fraud",
    "verdict",
    "score",
]


def _fixture_by_id(fixtures: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {fixture["fixture_id"]: fixture for fixture in fixtures}


def _collapse_prevention_status(
    result: dict[str, Any],
    boundaries: dict[str, bool],
    required_checks: list[str],
) -> str:
    if not result.get("no_verdict_confirmation"):
        return "fail"
    if not result.get("no_score_confirmation"):
        return "fail"
    if not result.get("non_public_confirmation"):
        return "fail"
    if result.get("guardrail_failure_flags"):
        return "fail"
    for check in required_checks:
        if not boundaries.get(check):
            return "fail"
    serialized = " ".join(
        str(result.get(field, ""))
        for field in ("posture_state_candidate", "prohibited_language_blocks")
    ).lower()
    if any(marker in serialized for marker in COLLAPSE_FAILURE_MARKERS):
        return "fail"
    return "pass"


def analyze_compound_stress() -> list[dict[str, Any]]:
    """Return internal structured stress objects only."""
    fixtures = load_fixtures()
    by_id = _fixture_by_id(fixtures)
    models = load_models()
    stress_results: list[dict[str, Any]] = []

    for case in STRESS_CASES:
        source_ids = case["source_fixture_ids"]
        fixture = by_id[source_ids[0]]
        result = evaluate_fixture(fixture, models)
        boundaries = evaluate_boundaries(fixture)
        active_checks = [name for name, active in boundaries.items() if active]
        caveats = result.get("caveat_trigger_refs") or result.get("triggered_caveats", [])
        collapse_status = _collapse_prevention_status(
            result,
            boundaries,
            case["required_boundary_checks"],
        )

        stress_results.append(
            {
                "stress_case_id": case["stress_case_id"],
                "source_fixture_ids": source_ids,
                "compound_boundary_class": case["compound_boundary_class"],
                "active_boundary_checks": active_checks,
                "required_caveat_families": case["required_caveat_families"],
                "forbidden_transformations_blocked": case["forbidden_transformations_blocked"],
                "guardrail_blocks": result.get("prohibited_language_blocks", []),
                "traceability_refs": {
                    "trace_id": result.get("trace_id"),
                    "protocol_step_refs": result.get("protocol_step_refs", []),
                    "boundary_check_refs": result.get("boundary_check_refs", []),
                },
                "collapse_prevention_status": collapse_status,
                "non_verdict_confirmation": result.get("no_verdict_confirmation", False),
                "non_score_confirmation": result.get("no_score_confirmation", False),
                "non_public_confirmation": result.get("non_public_confirmation", False),
                "stress_validation_status": "pass" if collapse_status == "pass" else "fail",
            }
        )

    return stress_results
