"""Local public exposure prerequisite map harness for Controlled Internal Prototype v0."""

from __future__ import annotations

import sys
from pathlib import Path

PROTOTYPE_ROOT = Path(__file__).resolve().parent
if str(PROTOTYPE_ROOT) not in sys.path:
    sys.path.insert(0, str(PROTOTYPE_ROOT))

from public_exposure_prerequisite_map import (  # noqa: E402
    REQUIRED_PREREQUISITE_COUNT,
    evaluate_public_exposure_prerequisite_map,
)


def main() -> int:
    result = evaluate_public_exposure_prerequisite_map()
    if result.get("prerequisite_count", 0) < REQUIRED_PREREQUISITE_COUNT:
        return 1
    if result.get("unmapped_prerequisite_count", 0) < REQUIRED_PREREQUISITE_COUNT:
        return 1
    if result.get("prerequisite_map_validation_status") != "pass":
        return 1
    if result.get("public_exposure_authorized") is not False:
        return 1
    if result.get("blocker_clearance_authorized") is not False:
        return 1

    print("controlled internal public exposure prerequisite map validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
