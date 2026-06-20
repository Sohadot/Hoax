"""Public exposure prerequisite map for Controlled Internal Prototype v0."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

MAP_REL = "data/public-exposure-prerequisite-map-v1.json"
REQUIRED_PREREQUISITE_COUNT = 24

AUTHORIZATION_FLAGS = [
    "public_exposure_authorized",
    "blocker_clearance_authorized",
    "release_authorized",
    "public_route_authorized",
    "public_benchmark_authorized",
    "public_report_authorized",
    "output_generator_authorized",
    "input_system_authorized",
    "upload_authorized",
    "scoring_authorized",
    "api_authorized",
    "javascript_authorized",
    "monetization_authorized",
]

REQUIRED_PREREQUISITE_FIELDS = [
    "prerequisite_id",
    "prerequisite_domain",
    "prerequisite_statement",
    "related_blocker_id",
    "required_evidence",
    "required_validator",
    "required_decision_log_entry",
    "required_rollback_condition",
    "clearance_authority",
    "current_status",
    "public_exposure_authorized",
]

CLEARED_STATUSES = frozenset({"cleared", "satisfied", "public_authorized"})


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def load_public_exposure_prerequisite_map(root: Path | None = None) -> dict[str, Any]:
    """Load public exposure prerequisite map JSON from repository data."""
    map_path = (root or _repo_root()) / MAP_REL
    with map_path.open(encoding="utf-8") as fh:
        return json.load(fh)


def evaluate_public_exposure_prerequisite_map(root: Path | None = None) -> dict[str, Any]:
    """Verify prerequisites remain unmapped and public authorization remains false."""
    data = load_public_exposure_prerequisite_map(root)
    prerequisites = data.get("prerequisites", [])
    failures: list[str] = []

    if data.get("prerequisite_map_id") != "public-exposure-prerequisite-map-v1":
        failures.append("prerequisite_map_id_mismatch")
    if len(prerequisites) < REQUIRED_PREREQUISITE_COUNT:
        failures.append("prerequisite_count_drift")

    for flag in AUTHORIZATION_FLAGS:
        if data.get(flag) is not False:
            failures.append(f"{flag}_not_false")

    if not data.get("prohibited_shortcuts"):
        failures.append("prohibited_shortcuts_missing")

    pathway = " ".join(data.get("clearance_pathway_rules", [])).lower()
    if "explicit" not in pathway and "future" not in pathway:
        failures.append("clearance_pathway_requires_explicit_authorization")

    unmapped = 0
    for item in prerequisites:
        for field in REQUIRED_PREREQUISITE_FIELDS:
            if field not in item:
                failures.append(f"missing_{field}_{item.get('prerequisite_id', 'unknown')}")
        status = str(item.get("current_status", "")).lower()
        if status in CLEARED_STATUSES or item.get("public_exposure_authorized") is True:
            failures.append(f"prerequisite_cleared_{item.get('prerequisite_id', 'unknown')}")
        if status == "unmapped":
            unmapped += 1
        authority = str(item.get("clearance_authority", "")).lower()
        if "future" not in authority and "explicit" not in authority:
            failures.append(f"clearance_authority_not_explicit_{item.get('prerequisite_id', 'unknown')}")

    if unmapped < REQUIRED_PREREQUISITE_COUNT:
        failures.append("unmapped_prerequisite_drift")

    return {
        "prerequisite_map_id": data.get("prerequisite_map_id"),
        "prerequisite_count": len(prerequisites),
        "unmapped_prerequisite_count": unmapped,
        "prerequisite_map_validation_status": "pass" if not failures else "fail",
        "validation_failures": failures,
        "public_exposure_authorized": False,
        "blocker_clearance_authorized": False,
        "non_public_confirmation": True,
    }
