#!/usr/bin/env python3
"""Validate Sprint 124 — Public Reference External Use Integrity Audit v1."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

from public_surface_checks import PUBLIC_SITEMAP_URL_COUNT  # noqa: E402

AUDIT_MD = "PUBLIC_REFERENCE_EXTERNAL_USE_INTEGRITY_AUDIT_V1.md"
SPRINT = "SPRINT_124_PUBLIC_REFERENCE_EXTERNAL_USE_INTEGRITY_AUDIT_V1.md"
JSON_PATH = "data/public-reference-external-use-integrity-audit-v1.json"
SCHEMA_PATH = "data/public-reference-external-use-integrity-audit-v1.schema.json"

LAYERS = [
    ("/reading-sequences/", "reading-sequences/index.html"),
    ("/retrieval-index/", "retrieval-index/index.html"),
    ("/citation-orientation/", "citation-orientation/index.html"),
    ("/source-use-orientation/", "source-use-orientation/index.html"),
]

REQUIRED_SCENARIO_FIELDS = [
    "scenario_id",
    "external_use_intent",
    "expected_layer_sequence",
    "expected_reference_destinations",
    "actual_layer_sequence",
    "actual_reference_destinations",
    "supporting_routes",
    "result",
    "observed_issue",
    "repair_applied",
    "boundary_check",
    "ai_agent_note",
]

UNSAFE_TERMS = [
    "citation generator",
    "generated citation",
    "generated answer",
    "search box",
    "source database",
    "source index",
    "source directory",
    "best route",
    "best source",
    "approved source",
    "source ranking",
    "source rating",
    "proof claim",
    "verification claim",
    "authority claim",
    "detector evidence",
    "score basis",
    "case conclusion",
    "investigation procedure",
    "operational procedure",
    "case review procedure",
    "due diligence",
    "dashboard",
    "graph tool",
    "scorecard",
    "rating system",
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
        "public_route_count_before": 104,
        "public_route_count_after": 104,
        "sitemap_url_count_expected": 104,
        "route_registry_changed": False,
        "public_file_registry_changed": False,
        "no_new_routes": True,
        "new_decision_created": False,
        "boundary_regressions_found": False,
        "external_use_layer_coherence_confirmed": True,
        "reading_layer_integrity_confirmed": True,
        "retrieval_layer_integrity_confirmed": True,
        "citation_layer_integrity_confirmed": True,
        "source_use_layer_integrity_confirmed": True,
        "cross_layer_link_integrity_confirmed": True,
        "route_count_drift_found": False,
        "stale_copy_found": False,
        "role_confusion_found": False,
        "link_imbalance_found": False,
        "authority_claim_drift_found": False,
        "verification_drift_found": False,
        "proof_drift_found": False,
        "detector_drift_found": False,
        "score_or_verdict_drift_found": False,
        "case_conclusion_drift_found": False,
        "generated_output_drift_found": False,
        "workflow_or_operational_drift_found": False,
        "transaction_or_sales_drift_found": False,
        "legal_or_financial_representation_drift_found": False,
    }
    for k, v in expected.items():
        if data.get(k) != v:
            error(f"{JSON_PATH}: {k} must be {v!r}")
            ok = False
    layers = data.get("primary_layers_under_audit", [])
    for route, _ in LAYERS:
        if route not in layers:
            error(f"{JSON_PATH}: primary_layers_under_audit missing {route}")
            ok = False
    scenarios = data.get("walkthrough_scenarios", [])
    if len(scenarios) < 24:
        error(f"{JSON_PATH}: must include at least 24 scenarios")
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
        error("audit JSON must declare production_route_added false for Sprint 124")
        ok = False
    reg = load_json("data/route-registry.json").get("routes", [])
    if len(reg) != 104:
        error(f"route registry must have exactly 104 entries, found {len(reg)}")
        ok = False
    files = load_json("data/public-file-registry.json").get("files", [])
    if any(f.get("public_file_id") == "PUB-FILE-0105" for f in files):
        error("PUB-FILE-0105 must not exist after Sprint 124 audit-only sprint")
        ok = False
    sitemap = ET.parse(ROOT / "sitemap.xml").getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = sitemap.findall("sm:url", ns) or sitemap.findall("url")
    if len(urls) != PUBLIC_SITEMAP_URL_COUNT:
        error(f"sitemap must have {PUBLIC_SITEMAP_URL_COUNT} URLs, found {len(urls)}")
        ok = False
    for route, rel in LAYERS:
        if not (ROOT / rel).is_file():
            error(f"{rel} missing for {route}")
            ok = False
    return ok


def validate_external_use_cross_links() -> bool:
    ok = True
    rs = (ROOT / "reading-sequences/index.html").read_text(encoding="utf-8")
    ri = (ROOT / "retrieval-index/index.html").read_text(encoding="utf-8")
    co = (ROOT / "citation-orientation/index.html").read_text(encoding="utf-8")
    su = (ROOT / "source-use-orientation/index.html").read_text(encoding="utf-8")
    homepage = (ROOT / "index.html").read_text(encoding="utf-8")
    smap = (ROOT / "system-map/index.html").read_text(encoding="utf-8")
    crosswalk = (ROOT / "evidence-conditions/crosswalk/index.html").read_text(encoding="utf-8")

    for route, _ in LAYERS:
        if route not in homepage:
            error(f"homepage must link to {route}")
            ok = False
        if route not in smap:
            error(f"system-map must link to {route}")
            ok = False

    for other_route, _ in [x for x in LAYERS if x[0] != "/reading-sequences/"]:
        if other_route not in rs:
            error(f"reading-sequences must link to {other_route}")
            ok = False
    for other_route in ("/reading-sequences/", "/citation-orientation/", "/source-use-orientation/"):
        if other_route not in ri:
            error(f"retrieval-index must link to {other_route}")
            ok = False
    for other_route in ("/retrieval-index/", "/reading-sequences/", "/source-use-orientation/"):
        if other_route not in co:
            error(f"citation-orientation must link to {other_route}")
            ok = False
    for other_route in ("/citation-orientation/", "/retrieval-index/", "/reading-sequences/"):
        if other_route not in su:
            error(f"source-use-orientation must link to {other_route}")
            ok = False

    if 'id="external-use-layer-sequence"' not in rs:
        error("reading-sequences missing external-use layer sequence hardening")
        ok = False
    if "/retrieval-index/" not in rs or "/citation-orientation/" not in rs:
        error("reading-sequences AI agent sequence missing retrieval/citation hardening")
        ok = False
    if "/source-use-orientation/" not in co.split("reference-answer", 1)[-1][:800]:
        error("citation-orientation Reference Answer missing source-use hardening")
        ok = False
    if "/citation-orientation/" not in ri.split("reference-answer", 1)[-1][:800]:
        error("retrieval-index Reference Answer missing citation-orientation hardening")
        ok = False
    if 'id="external-use-layer"' not in smap:
        error("system-map missing external-use layer summary hardening")
        ok = False
    for route in ("/reading-sequences/", "/retrieval-index/", "/citation-orientation/", "/source-use-orientation/"):
        if route not in crosswalk:
            error(f"evidence-condition crosswalk must link to {route}")
            ok = False

    for rel in ("reading-sequences/index.html", "retrieval-index/index.html", "citation-orientation/index.html", "source-use-orientation/index.html"):
        html = (ROOT / rel).read_text(encoding="utf-8").lower()
        for bad in ("<script", "<form", "<input", "<textarea", "<select"):
            if bad in html:
                error(f"{rel}: prohibited element {bad}")
                ok = False
    return ok


def validate_terms_and_decision() -> bool:
    ok = True
    dlog = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")
    data = load_json(JSON_PATH)
    if data.get("new_decision_created"):
        if "DEC-140" not in dlog:
            error("DEC-140 required when new_decision_created is true")
            ok = False
    elif re.search(r"\bDEC-140\b", dlog):
        error("DEC-140 present but audit declares no new decision was required")
        ok = False
    for rel in (SPRINT,):
        text = (ROOT / rel).read_text(encoding="utf-8")
        for term in UNSAFE_TERMS:
            if unnegated(text, term):
                error(f"{rel}: unnegated unsafe term {term!r}")
                ok = False
    for rel in (
        "reading-sequences/index.html",
        "retrieval-index/index.html",
        "citation-orientation/index.html",
        "source-use-orientation/index.html",
    ):
        text = (ROOT / rel).read_text(encoding="utf-8")
        for term in UNSAFE_TERMS:
            if unnegated(text, term):
                error(f"{rel}: unnegated unsafe term {term!r}")
                ok = False
    return ok


def validate_governance_wiring() -> bool:
    ok = True
    if not any(c.get("claim_id") == "CLAIM-0125" for c in load_json("data/evidence-ledger.json").get("claims", [])):
        error("CLAIM-0125 missing")
        ok = False
    if not any(g.get("gate_id") == "PUB-GATE-0118" for g in load_json("data/publisher-quality-gates.json").get("gates", [])):
        error("PUB-GATE-0118 missing")
        ok = False
    locs = {s.get("location") for s in load_json("data/source-registry.json").get("sources", [])}
    for rel in (
        AUDIT_MD,
        SPRINT,
        JSON_PATH,
        SCHEMA_PATH,
        "validators/validate_public_reference_external_use_integrity_audit_v1.py",
    ):
        if rel not in locs:
            error(f"source-registry missing {rel}")
            ok = False
    if "validate_public_reference_external_use_integrity_audit_v1.py" not in (
        ROOT / "validators/validate_all.py"
    ).read_text(encoding="utf-8"):
        error("validate_all.py missing Sprint 124 validator")
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
        validate_external_use_cross_links,
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
