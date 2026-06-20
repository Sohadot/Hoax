"""Local validation harness for Controlled Internal Prototype v0."""

from __future__ import annotations

import sys
from pathlib import Path

PROTOTYPE_ROOT = Path(__file__).resolve().parent
if str(PROTOTYPE_ROOT) not in sys.path:
    sys.path.insert(0, str(PROTOTYPE_ROOT))

from prototype_core import ALLOWED_RESULT_KEYS, run_prototype  # noqa: E402

REQUIRED_POSTURES = {"Supported", "Qualified", "Limited", "Not Assessable", "Out of Scope"}
REQUIRED_TRACE_FIELDS = {
    "trace_id",
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
}


def main() -> int:
    results = run_prototype()
    if len(results) < 16:
        return 1
    seen_postures: set[str] = set()
    for result in results:
        if set(result.keys()) - ALLOWED_RESULT_KEYS:
            return 1
        if not REQUIRED_TRACE_FIELDS.issubset(result.keys()):
            return 1
        if result.get("validation_status") != "pass":
            return 1
        boundaries = result.get("active_boundary_checks", {})
        if not isinstance(boundaries, dict) or not boundaries:
            return 1
        posture = result.get("posture_state_candidate")
        if posture:
            seen_postures.add(str(posture))
    if not REQUIRED_POSTURES.issubset(seen_postures):
        return 1
    print("controlled internal prototype validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
