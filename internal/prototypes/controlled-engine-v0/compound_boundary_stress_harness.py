"""Local compound boundary stress harness for Controlled Internal Prototype v0."""

from __future__ import annotations

import sys
from pathlib import Path

PROTOTYPE_ROOT = Path(__file__).resolve().parent
if str(PROTOTYPE_ROOT) not in sys.path:
    sys.path.insert(0, str(PROTOTYPE_ROOT))

from compound_boundary_stress_analyzer import STRESS_CASES, analyze_compound_stress  # noqa: E402
from fixture_loader import load_fixtures  # noqa: E402

MIN_STRESS_CASES = 8
MAX_FIXTURE_COUNT = 16


def main() -> int:
    fixtures = load_fixtures()
    if len(fixtures) != MAX_FIXTURE_COUNT:
        return 1

    results = analyze_compound_stress()
    if len(results) < MIN_STRESS_CASES:
        return 1
    if len(results) != len(STRESS_CASES):
        return 1

    for result in results:
        if result.get("stress_validation_status") != "pass":
            return 1
        if result.get("collapse_prevention_status") != "pass":
            return 1
        if not result.get("non_verdict_confirmation"):
            return 1
        if not result.get("non_score_confirmation"):
            return 1
        if not result.get("non_public_confirmation"):
            return 1

    print("controlled internal compound boundary stress validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
