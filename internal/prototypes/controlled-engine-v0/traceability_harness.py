"""Local traceability and interpretability harness for Controlled Internal Prototype v0."""

from __future__ import annotations

import sys
from pathlib import Path

PROTOTYPE_ROOT = Path(__file__).resolve().parent
if str(PROTOTYPE_ROOT) not in sys.path:
    sys.path.insert(0, str(PROTOTYPE_ROOT))

from interpretability_auditor import audit_result  # noqa: E402
from prototype_core import run_prototype  # noqa: E402


def main() -> int:
    results = run_prototype()
    if not results:
        return 1
    for result in results:
        audit = audit_result(result)
        if audit["audit_status"] != "pass":
            return 1
    print("controlled internal traceability validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
