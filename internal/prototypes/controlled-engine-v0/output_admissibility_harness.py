"""Local output admissibility harness for Controlled Internal Prototype v0."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

PROTOTYPE_ROOT = Path(__file__).resolve().parent
if str(PROTOTYPE_ROOT) not in sys.path:
    sys.path.insert(0, str(PROTOTYPE_ROOT))

from compound_boundary_stress_analyzer import analyze_compound_stress  # noqa: E402
from fixture_loader import load_fixtures  # noqa: E402
from guardrail_red_team_pack import analyze_red_team_pack  # noqa: E402
from model_loader import load_models  # noqa: E402
from output_admissibility_contract import evaluate_output_admissibility  # noqa: E402
from prototype_core import evaluate_fixture  # noqa: E402

MAX_FIXTURE_COUNT = 16


def _mutated(base: dict, **updates) -> dict:
    sample = copy.deepcopy(base)
    sample.update(updates)
    return sample


def main() -> int:
    fixtures = load_fixtures()
    if len(fixtures) != MAX_FIXTURE_COUNT:
        return 1

    models = load_models()
    fixture_results = [evaluate_fixture(fixture, models) for fixture in fixtures]

    for result in fixture_results:
        admissibility = evaluate_output_admissibility(result)
        if admissibility["admissibility_status"] != "admissible_internal":
            return 1
        if admissibility["admissibility_validation_status"] != "pass":
            return 1

    if not fixture_results:
        return 1
    base = fixture_results[0]

    negative_cases = [
        (_mutated(base, posture_basis=[]), "inadmissible_missing_basis"),
        (_mutated(base, triggered_caveats=[], caveat_trigger_refs=[]), "inadmissible_missing_caveat"),
        (
            _mutated(base, active_boundary_checks={}, boundary_check_refs=[]),
            "inadmissible_boundary_collapse",
        ),
        (_mutated(base, guardrail_failure_flags=["blocked"], validation_status="guardrail_blocked"), "inadmissible_guardrail_failure"),
        (_mutated(base, trace_id=None, traceability_map=None), "inadmissible_traceability_gap"),
        (_mutated(base, posture_state_candidate="result card output envelope stub"), "inadmissible_report_shape"),
        (_mutated(base, out_of_scope_reason="public report generation stub"), "inadmissible_report_shape"),
        (_mutated(base, non_public_confirmation=False), "inadmissible_public_output_risk"),
        (_mutated(base, no_verdict_confirmation=False), "inadmissible_guardrail_failure"),
        (_mutated(base, not_assessable_reason="confidence score output stub"), "inadmissible_guardrail_failure"),
    ]

    for sample, expected_status in negative_cases:
        admissibility = evaluate_output_admissibility(sample)
        if admissibility["admissibility_status"] != expected_status:
            return 1
        if admissibility["admissibility_validation_status"] != "fail":
            return 1

    stress_results = analyze_compound_stress()
    if not stress_results or any(r.get("stress_validation_status") != "pass" for r in stress_results):
        return 1

    red_team_results = analyze_red_team_pack()
    if not red_team_results or any(r.get("red_team_validation_status") != "pass" for r in red_team_results):
        return 1

    referenced_ids = {f["fixture_id"] for f in fixtures}
    for result in fixture_results:
        if result["fixture_id"] not in referenced_ids:
            return 1

    print("controlled internal output admissibility validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
