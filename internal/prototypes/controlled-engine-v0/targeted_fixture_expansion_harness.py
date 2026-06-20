"""Targeted fixture expansion validation for Controlled Internal Prototype v0."""

from __future__ import annotations

import sys
from pathlib import Path

PROTOTYPE_ROOT = Path(__file__).resolve().parent
if str(PROTOTYPE_ROOT) not in sys.path:
    sys.path.insert(0, str(PROTOTYPE_ROOT))

from fixture_loader import REQUIRED_FLAGS, load_fixtures  # noqa: E402

MIN_FIXTURE_COUNT = 10
MAX_FIXTURE_COUNT = 16
BASE_FIXTURE_COUNT = 10

REQUIRED_EXPANSION_FIELDS = [
    "coverage_gap_ref",
    "expansion_reason",
    "expected_allowed_posture_states",
    "expected_required_caveats",
    "expected_boundary_checks",
    "expected_forbidden_transformations_blocked",
    "expected_traceability_fields",
    "forbidden_output_expectations",
]

REQUIRED_GAP_MARKERS = [
    "traceability_caveat",
    "compound boundary",
    "source/traceability/chain",
    "output_boundary",
    "not-assessable",
]

EXPANSION_FIXTURE_IDS = [
    "SYN-FIX-011-TRACEABILITY-CAVEAT",
    "SYN-FIX-012-PROVENANCE-CONTEXT-COMPOUND",
    "SYN-FIX-013-DRIFT-LIMITATION-COMPOUND",
    "SYN-FIX-014-ATTRIBUTION-OUTPUT-BOUNDARY",
    "SYN-FIX-015-SOURCE-TRACEABILITY-CHAIN",
    "SYN-FIX-016-NOT-ASSESSABLE-MULTI",
]


def _gap_markers_satisfied(expansion_fixtures: list[dict]) -> bool:
    combined = " ".join(f.get("coverage_gap_ref", "") for f in expansion_fixtures).lower()
    return all(marker.lower() in combined for marker in REQUIRED_GAP_MARKERS)


def main() -> int:
    fixtures = load_fixtures()
    count = len(fixtures)
    if count <= MIN_FIXTURE_COUNT or count > MAX_FIXTURE_COUNT:
        return 1

    expansion = [f for f in fixtures if f.get("coverage_gap_ref")]
    if len(expansion) != count - BASE_FIXTURE_COUNT:
        return 1

    ids = {f["fixture_id"] for f in expansion}
    if ids != set(EXPANSION_FIXTURE_IDS):
        return 1

    for fixture in expansion:
        for field in REQUIRED_EXPANSION_FIELDS:
            if not fixture.get(field):
                return 1
        for flag, expected in REQUIRED_FLAGS.items():
            if fixture.get(flag) is not expected:
                return 1

    if not _gap_markers_satisfied(expansion):
        return 1

    print("controlled internal targeted fixture expansion validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
