#!/usr/bin/env python3
"""Validate Sprint 121 — Public Reference Citation Walkthrough Audit v1."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

from public_surface_checks import PUBLIC_SITEMAP_URL_COUNT  # noqa: E402

AUDIT_MD = "PUBLIC_REFERENCE_CITATION_WALKTHROUGH_AUDIT_V1.md"
SPRINT = "SPRINT_121_PUBLIC_REFERENCE_CITATION_WALKTHROUGH_AUDIT_V1.md"
JSON_PATH = "data/public-reference-citation-walkthrough-audit-v1.json"
SCHEMA_PATH = "data/public-reference-citation-walkthrough-audit-v1.schema.json"
PAGE = "citation-orientation/index.html"
PAGE_ROUTE = "/citation-orientation/"

REQUIRED_SCENARIO_FIELDS = [
    "scenario_id",
    "citation_intent",
    "expected_reference_destination",
    "actual_reference_destination",
    "supporting_routes",
    "result",
    "observed_issue",
    "repair_applied",
    "boundary_check",
    "ai_citation_note",
]

UNSAFE_TERMS = [
    "citation generator",
    "generated citation",
    "legal citation",
    "academic endorsement",
    "authoritative proof",
    "verification claim",
    "best source",
    "approved source",
    "verified source",
    "investigation procedure",
    "operational procedure",
    "case review procedure",
    "due diligence",
    "dashboard",
    "graph tool",
    "scorecard",
    "downloadable report",
    "sales page",
    "consulting offer",
    "service funnel",
    "pricing",
    "transaction page",
    "legal representation",
    "financial representation",
]

NEGATION_PATTERN = re.compile(
    r"(?:must not|does not|do not|not a|not an|no |without|forbidden|prohibited|is not|are not|cannot)\s+[\w\s\-/]{0,120}",
    re.IGNORECASE,
)


def error(msg: str) -> None:
    print(f"ERROR: {msg}")


def load_json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def unnegated(text: str, term: str) -> bool:
    lower = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text)).lower()
    pos = 0
    while True:
        idx = lower.find(term, pos)
        if idx < 0:
            return False
        prefix = lower[max(0, idx - 160):idx]
        if NEGATION_PATTERN.search(prefix + term) or "what this page does not claim" in lower:
            pos = idx + len(term)
            continue
        if term == "sales page" and "sales-page" in lower[max(0, idx - 4): idx + 12]:
            pos = idx + len(term)
            continue
        return True


def validate_artifacts() -> bool:
    ok = True
    for rel in (AUDIT_MD, SPRINT, JSON_PATH, SCHEMA_PATH):
        if not (ROOT / rel).is_file():
            error(f"{rel} missing")
            ok = False
    return ok


def validate_audit_json() -> bool:
    ok = True
    data = load_json(JSON_PATH)
    load_json(SCHEMA_PATH)
    expected = {
        "audit_only": True,
        "production_route_added": False,
        "public_route_count_before": 103,
        "public_route_count_after": 103,
        "sitemap_url_count_expected": 103,
        "primary_route_under_audit": PAGE_ROUTE,
        "route_registry_changed": False,
        "public_file_registry_changed": False,
        "no_new_routes": True,
        "new_decision_created": False,
        "authority_overreach_found": False,
        "verification_drift_found": False,
        "detector_drift_found": False,
        "score_or_verdict_drift_found": False,
        "generated_citation_drift_found": False,
        "legal_or_academic_citation_drift_found": False,
        "transaction_or_sales_drift_found": False,
    }
    for k, v in expected.items():
        if data.get(k) != v:
            error(f"{JSON_PATH}: {k} must be {v!r}")
            ok = False
    scenarios = data.get("walkthrough_scenarios", [])
    if len(scenarios) < 20:
        error(f"{JSON_PATH}: must include at least 20 scenarios")
        ok = False
    if data.get("total_scenarios") != len(scenarios):
        error(f"{JSON_PATH}: total_scenarios mismatch")
        ok = False
    passed = sum(1 for s in scenarios if s.get("result") == "pass")
    failed = sum(1 for s in scenarios if s.get("result") == "fail")
    if data.get("scenarios_passed") != passed or data.get("scenarios_failed") != failed:
        error(f"{JSON_PATH}: pass/fail counts mismatch")
        ok = False
    for sc in scenarios:
        for field in REQUIRED_SCENARIO_FIELDS:
            if field not in sc:
                error(f"{sc.get('scenario_id', '?')}: missing field {field}")
                ok = False
        if sc.get("result") not in ("pass", "fail"):
            error(f"{sc.get('scenario_id')}: invalid result")
            ok = False
        if sc.get("result") == "fail" and not (sc.get("repair_applied") or sc.get("deferred_reason")):
            error(f"{sc.get('scenario_id')}: failed scenario needs repair_applied or deferred_reason")
            ok = False
    return ok


def validate_no_expansion() -> bool:
    ok = True
    data = load_json(JSON_PATH)
    if data.get("production_route_added") is not False:
        error("audit JSON must declare production_route_added false for Sprint 121")
        ok = False
    if data.get("public_route_count_after") != 103:
        error("audit JSON public_route_count_after must remain 103 for Sprint 121")
        ok = False
    if data.get("sitemap_url_count_expected") != 103:
        error("audit JSON sitemap_url_count_expected must remain 103 for Sprint 121")
        ok = False
    reg = load_json("data/route-registry.json").get("routes", [])
    r103 = next((r for r in reg if r.get("route_id") == "ROUTE-0103"), None)
    if r103 is None or r103.get("path") != PAGE_ROUTE:
        error("ROUTE-0103 must remain present for audited citation-orientation route")
        ok = False
    return ok


def validate_citation_orientation_links() -> bool:
    ok = True
    if not (ROOT / PAGE).is_file():
        error(f"{PAGE} missing")
        return False
    html = (ROOT / PAGE).read_text(encoding="utf-8")
    for rel in (
        "index.html",
        "system-map/index.html",
        "reading-sequences/index.html",
        "retrieval-index/index.html",
    ):
        if PAGE_ROUTE not in (ROOT / rel).read_text(encoding="utf-8"):
            error(f"{rel} must link to {PAGE_ROUTE}")
            ok = False
    if "/executive-overview/category-thesis/" not in html:
        error("citation-orientation missing category-thesis hardening link")
        ok = False
    for anchor in ("#reference-answer", "#source-confidence", "#cite-this-reference", "#retrieval-capsule"):
        if f'href="{anchor}"' not in html:
            error(f"citation-orientation how-to-use missing self-block anchor {anchor}")
            ok = False
    ri = (ROOT / "retrieval-index/index.html").read_text(encoding="utf-8")
    if "/citation-orientation/#reference-answer" not in ri:
        error("retrieval-index missing citation-orientation block anchor hardening")
        ok = False
    for bad in ("<script", "<form", "<input", "<textarea", "<select"):
        if bad in html.lower():
            error(f"{PAGE}: prohibited element {bad}")
            ok = False
    return ok


def validate_terms_and_decision() -> bool:
    ok = True
    dlog = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")
    data = load_json(JSON_PATH)
    source_use_live = any(
        r.get("route_id") == "ROUTE-0104" and r.get("path") == "/source-use-orientation/"
        for r in load_json("data/route-registry.json").get("routes", [])
    )
    if data.get("new_decision_created"):
        if "DEC-138" not in dlog:
            error("DEC-138 required when new_decision_created is true")
            ok = False
        if PAGE_ROUTE not in dlog:
            error("DEC-138 must govern visible production issue on citation-orientation route")
            ok = False
    elif "DEC-138" in dlog and not source_use_live:
        error("DEC-138 present but audit declares no new decision and source-use-orientation route is absent")
        ok = False
    for rel in (SPRINT,):
        text = (ROOT / rel).read_text(encoding="utf-8")
        for term in UNSAFE_TERMS:
            if unnegated(text, term):
                error(f"{rel}: unnegated unsafe term {term!r}")
                ok = False
    for rel in (PAGE, "retrieval-index/index.html"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        for term in UNSAFE_TERMS:
            if unnegated(text, term):
                error(f"{rel}: unnegated unsafe term {term!r}")
                ok = False
    return ok


def validate_governance_wiring() -> bool:
    ok = True
    if not any(c.get("claim_id") == "CLAIM-0122" for c in load_json("data/evidence-ledger.json").get("claims", [])):
        error("CLAIM-0122 missing")
        ok = False
    if not any(g.get("gate_id") == "PUB-GATE-0115" for g in load_json("data/publisher-quality-gates.json").get("gates", [])):
        error("PUB-GATE-0115 missing")
        ok = False
    locs = {s.get("location") for s in load_json("data/source-registry.json").get("sources", [])}
    for rel in (
        AUDIT_MD,
        SPRINT,
        JSON_PATH,
        SCHEMA_PATH,
        "validators/validate_public_reference_citation_walkthrough_audit_v1.py",
    ):
        if rel not in locs:
            error(f"source-registry missing {rel}")
            ok = False
    if "validate_public_reference_citation_walkthrough_audit_v1.py" not in (
        ROOT / "validators/validate_all.py"
    ).read_text(encoding="utf-8"):
        error("validate_all.py missing Sprint 121 validator")
        ok = False
    names = subprocess.run(["git", "ls-files"], cwd=ROOT, text=True, capture_output=True).stdout.splitlines()
    names += subprocess.run(
        ["git", "diff", "--cached", "--name-only"], cwd=ROOT, text=True, capture_output=True
    ).stdout.splitlines()
    for rel in names:
        if "__pycache__" in rel or rel.endswith(".pyc"):
            error(f"python cache tracked or staged: {rel}")
            ok = False
    return ok


def main() -> int:
    ok = True
    for fn in (
        validate_artifacts,
        validate_audit_json,
        validate_no_expansion,
        validate_citation_orientation_links,
        validate_terms_and_decision,
        validate_governance_wiring,
    ):
        if not fn():
            ok = False
    if not ok:
        print("FAIL")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
