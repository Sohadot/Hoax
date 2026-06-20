"""Structured traceability mapping for Controlled Internal Prototype v0."""

from __future__ import annotations

import hashlib
from typing import Any

from boundary_evaluator import evaluate_boundaries
from caveat_mapper import map_caveats
from protocol_mapper import PROTOCOL_FIELD_MAP, map_protocol_steps

FIXTURE_TO_DIMENSION_MAP = {
    "artifact_condition": "artifact_condition",
    "claim_condition": "claim_condition",
    "source_basis": "source_basis",
    "source_confidence": "source_confidence",
    "provenance_status": "provenance_status",
    "context_status": "context_status",
    "traceability_status": "traceability_status",
    "chain_status": "chain_status",
    "drift_status": "drift_status",
    "limitation_status": "limitation_status",
    "interpretation_risk_status": "interpretation_risk_status",
    "attribution_boundary_status": "attribution_boundary_status",
    "output_boundary_status": "output_boundary_status",
}

PROTOCOL_TO_STANDARD_MAP = {
    "EP-P01": ["EPS-001", "EPS-002"],
    "EP-P02": ["EPS-001", "EPS-007"],
    "EP-P03": ["EPS-003", "EPS-007"],
    "EP-P04": ["EPS-003", "EPS-012"],
    "EP-P05": ["EPS-004", "EPS-012"],
    "EP-P06": ["EPS-009", "EPS-012"],
    "EP-P07": ["EPS-007", "EPS-012"],
    "EP-P08": ["EPS-010", "EPS-012"],
    "EP-P09": ["EPS-008", "EPS-012"],
    "EP-P10": ["EPS-009", "EPS-013"],
    "EP-P11": ["EPS-011", "EPS-013"],
    "EP-P12": ["EPS-012"],
    "EP-P13": ["EPS-013"],
    "EP-P14": ["EPS-002", "EPS-014"],
    "EP-P15": ["EPS-006", "EPS-014"],
    "EP-P16": ["EPS-005", "EPS-006", "EPS-012"],
    "EP-P17": ["EPS-006", "EPS-013", "EPS-014"],
}

BOUNDARY_TO_CAVEAT_MAP = {
    "artifact_subject_separation_check": ["attribution_boundary_caveat"],
    "source_confidence_not_certification_check": ["source_caveat"],
    "provenance_gap_not_manipulation_check": ["provenance_caveat"],
    "context_collapse_not_motive_check": ["context_caveat"],
    "claim_drift_not_deception_check": ["drift_caveat"],
    "evidence_limitation_not_falsehood_check": ["limitation_caveat"],
    "interpretation_risk_not_verdict_check": ["interpretation_risk_caveat"],
    "attribution_boundary_no_subject_transfer_check": ["attribution_boundary_caveat"],
    "output_boundary_no_forbidden_language_check": ["output_boundary_caveat"],
}

GUARDRAIL_RULE_MAP = {
    "fake/real verdict": {
        "guardrail_rule_refs": ["GL-FAKE-REAL-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-fake-real-output"],
    },
    "truth/falsity verdict": {
        "guardrail_rule_refs": ["GL-TRUTH-FALSITY-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-truth-certification"],
    },
    "deception finding": {
        "guardrail_rule_refs": ["GL-DECEPTION-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-deception-default"],
    },
    "manipulation proof": {
        "guardrail_rule_refs": ["GL-MANIPULATION-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-manipulation-proof"],
    },
    "fraud accusation": {
        "guardrail_rule_refs": ["GL-FRAUD-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-fraud-accusation"],
    },
    "subject guilt": {
        "guardrail_rule_refs": ["GL-SUBJECT-GUILT-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-subject-transfer"],
    },
    "responsibility assignment": {
        "guardrail_rule_refs": ["GL-RESPONSIBILITY-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-responsibility-assignment"],
    },
    "legal conclusion": {
        "guardrail_rule_refs": ["GL-LEGAL-CONCLUSION-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-legal-conclusion"],
    },
    "moderation action": {
        "guardrail_rule_refs": ["GL-MODERATION-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-moderation-action"],
    },
    "numeric score": {
        "guardrail_rule_refs": ["GL-SCORE-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-numeric-score"],
    },
    "confidence percentage": {
        "guardrail_rule_refs": ["GL-CONFIDENCE-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-confidence-percentage"],
    },
    "upload classification result": {
        "guardrail_rule_refs": ["GL-UPLOAD-CLASSIFICATION-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-upload-classification"],
    },
    "automated result card": {
        "guardrail_rule_refs": ["GL-RESULT-CARD-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-result-card"],
    },
    "detector-style language": {
        "guardrail_rule_refs": ["GL-DETECTOR-STYLE-BLOCK"],
        "forbidden_transformation_refs": ["FT-no-detector-style-output"],
    },
}


def build_trace_id(fixture_id: str, posture_state: str) -> str:
    """Create deterministic trace IDs from fixture and posture."""
    seed = f"{fixture_id}|{posture_state}".encode("utf-8")
    digest = hashlib.sha1(seed).hexdigest()[:12]
    return f"trace-{digest}"


def build_traceability_map(
    fixture: dict[str, Any],
    posture_state: str,
    prohibited_families: list[str],
) -> dict[str, Any]:
    """Return internal traceability structures only."""
    protocol_map = map_protocol_steps(fixture)
    boundary_checks = evaluate_boundaries(fixture)
    caveats = map_caveats(fixture)

    protocol_step_refs = list(PROTOCOL_FIELD_MAP.keys())
    standard_refs: list[str] = []
    for step_id in protocol_step_refs:
        for ref in PROTOCOL_TO_STANDARD_MAP[step_id]:
            if ref not in standard_refs:
                standard_refs.append(ref)

    evidence_refs = [
        dimension
        for field, dimension in FIXTURE_TO_DIMENSION_MAP.items()
        if fixture.get(field) is not None
    ]

    boundary_refs = [name for name, active in boundary_checks.items() if active]

    guardrail_rule_refs: list[str] = []
    forbidden_transformation_refs: list[str] = []
    for family in prohibited_families:
        mapping = GUARDRAIL_RULE_MAP.get(family, {})
        for ref in mapping.get("guardrail_rule_refs", []):
            if ref not in guardrail_rule_refs:
                guardrail_rule_refs.append(ref)
        for ref in mapping.get("forbidden_transformation_refs", []):
            if ref not in forbidden_transformation_refs:
                forbidden_transformation_refs.append(ref)

    condition_source_refs = {
        name: {
            "fixture_fields": [
                field
                for field in FIXTURE_TO_DIMENSION_MAP
                if fixture.get(field) is not None
            ],
            "protocol_steps": protocol_step_refs,
        }
        for name in boundary_refs
    }

    return {
        "trace_id": build_trace_id(fixture["fixture_id"], posture_state),
        "traceability_chain": [
            "fixture_field",
            "evidence_condition_dimension",
            "EP-P_protocol_step",
            "EPS_standard_principle",
            "boundary_check",
            "caveat_trigger",
            "guardrail_rule",
            "forbidden_transformation_block",
            "internal_structured_result",
        ],
        "fixture_to_protocol_map": protocol_map,
        "protocol_step_refs": protocol_step_refs,
        "standard_principle_refs": standard_refs,
        "evidence_condition_refs": evidence_refs,
        "boundary_check_refs": boundary_refs,
        "boundary_to_caveat_map": {
            name: BOUNDARY_TO_CAVEAT_MAP[name] for name in boundary_refs if name in BOUNDARY_TO_CAVEAT_MAP
        },
        "caveat_trigger_refs": caveats,
        "guardrail_rule_refs": guardrail_rule_refs,
        "forbidden_transformation_refs": forbidden_transformation_refs,
        "condition_source_refs": condition_source_refs,
    }
