#!/usr/bin/env python3
"""Validate Sprint 127 — Public Reference Acquisition Language Boundary Audit v1."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

from public_surface_checks import PUBLIC_SITEMAP_URL_COUNT  # noqa: E402

AUDIT_MD = "PUBLIC_REFERENCE_ACQUISITION_LANGUAGE_BOUNDARY_AUDIT_V1.md"
SPRINT = "SPRINT_127_PUBLIC_REFERENCE_ACQUISITION_LANGUAGE_BOUNDARY_AUDIT_V1.md"
JSON_PATH = "data/public-reference-acquisition-language-boundary-audit-v1.json"
SCHEMA_PATH = "data/public-reference-acquisition-language-boundary-audit-v1.schema.json"

EXTERNAL_USE = [
    ("/reading-sequences/", "reading-sequences/index.html"),
    ("/retrieval-index/", "retrieval-index/index.html"),
    ("/citation-orientation/", "citation-orientation/index.html"),
    ("/source-use-orientation/", "source-use-orientation/index.html"),
]

PATCHED_PAGES = [
    "acquisition-readiness/index.html",
    "acquisition-readiness/governance-traceability/index.html",
    "acquisition-readiness/category-asset/index.html",
    "acquisition-readiness/public-reference-surface/index.html",
    "index.html",
    "strategic-review/index.html",
]

REQUIRED_LANGUAGE_FIELDS = [
    "language_id",
    "language_text",
    "public_page",
    "anchor_or_section",
    "language_category",
    "boundary_risk",
    "expected_safe_interpretation",
    "actual_interpretation",
    "status",
    "observed_issue",
    "repair_applied",
    "boundary_check",
    "ai_agent_note",
]

REQUIRED_SCENARIO_FIELDS = [
    "scenario_id",
    "acquisition_language_intent",
    "expected_pages_checked",
    "expected_safe_interpretation",
    "actual_interpretation",
    "supporting_routes_or_artifacts",
    "result",
    "observed_issue",
    "repair_applied",
    "boundary_check",
    "ai_agent_note",
]

DRIFT_FLAGS = [
    "route_count_drift_found",
    "stale_copy_found",
    "unsafe_acquisition_language_found",
    "sales_page_drift_found",
    "pitch_deck_drift_found",
    "acquisition_solicitation_drift_found",
    "buyer_solicitation_drift_found",
    "pricing_or_valuation_drift_found",
    "transaction_readiness_drift_found",
    "due_diligence_room_drift_found",
    "private_data_room_drift_found",
    "buyer_packet_drift_found",
    "investor_packet_drift_found",
    "legal_or_financial_representation_drift_found",
    "investment_claim_drift_found",
    "authority_claim_drift_found",
    "verification_drift_found",
    "proof_drift_found",
    "detector_drift_found",
    "score_or_verdict_drift_found",
    "case_conclusion_drift_found",
    "audit_as_certification_drift_found",
    "source_as_proof_drift_found",
]

UNSAFE_TERMS = [
    "for sale",
    "acquire this asset",
    "buy this asset",
    "buyer opportunity",
    "investment opportunity",
    "acquisition opportunity",
    "valuation",
    "pricing page",
    "offer page",
    "escrow",
    "closing",
    "transaction-ready",
    "due diligence ready",
    "legal review ready",
    "financial review ready",
    "investor-ready",
    "acquisition proof",
    "sales proof",
    "buyer packet",
    "official certification",
    "guaranteed authority",
    "private data room",
    "downloadable report",
    "consultation form",
    "contact-to-acquire",
    "contact to acquire",
    "contact-to-buy",
    "contact to buy",
]

NEGATION_PATTERN = re.compile(
    r"(?:must not|does not|do not|not a|not an|no |without|forbidden|prohibited|is not|are not|cannot|not)\s+[\w\s\-/]{0,120}",
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
        if term == "valuation" and "not valuation" in lower:
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
        "acquisition_language_boundary_confirmed": True,
        "acquisition_readability_without_solicitation_confirmed": True,
        "strategic_readiness_as_reference_maturity_confirmed": True,
        "unsafe_language_count": 0,
    }
    for k, v in expected.items():
        if data.get(k) != v:
            error(f"{JSON_PATH}: {k} must be {v!r}")
            ok = False
    for flag in DRIFT_FLAGS:
        if data.get(flag) is not False:
            error(f"{JSON_PATH}: {flag} must be false")
            ok = False
    inventory = data.get("acquisition_language_inventory", [])
    if len(inventory) < 25:
        error(f"{JSON_PATH}: must include at least 25 language records")
        ok = False
    if data.get("total_language_inventory_count") != len(inventory):
        error(f"{JSON_PATH}: total_language_inventory_count mismatch")
        ok = False
    safe = sum(1 for x in inventory if x.get("status") == "safe")
    repaired = sum(1 for x in inventory if x.get("status") == "repaired")
    if data.get("safe_language_count") != safe:
        error(f"{JSON_PATH}: safe_language_count mismatch")
        ok = False
    if data.get("repaired_language_count") != repaired:
        error(f"{JSON_PATH}: repaired_language_count mismatch")
        ok = False
    for rec in inventory:
        for field in REQUIRED_LANGUAGE_FIELDS:
            if field not in rec:
                error(f"{rec.get('language_id', '?')}: missing field {field}")
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
    ext = data.get("external_use_layers_checked", {})
    for route, _ in EXTERNAL_USE:
        if not ext.get(route):
            error(f"{JSON_PATH}: external_use_layers_checked missing {route}")
            ok = False
    return ok


def validate_no_expansion() -> bool:
    ok = True
    reg = load_json("data/route-registry.json").get("routes", [])
    if len(reg) != 104:
        error(f"route registry must have exactly 104 entries, found {len(reg)}")
        ok = False
    files = load_json("data/public-file-registry.json").get("files", [])
    if any(f.get("public_file_id") == "PUB-FILE-0105" for f in files):
        error("PUB-FILE-0105 must not exist after Sprint 127 audit-only sprint")
        ok = False
    sitemap = ET.parse(ROOT / "sitemap.xml").getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = sitemap.findall("sm:url", ns) or sitemap.findall("url")
    if len(urls) != PUBLIC_SITEMAP_URL_COUNT:
        error(f"sitemap must have {PUBLIC_SITEMAP_URL_COUNT} URLs, found {len(urls)}")
        ok = False
    for route, rel in EXTERNAL_USE:
        if not (ROOT / rel).is_file():
            error(f"{rel} missing for {route}")
            ok = False
    for rel in (
        "acquisition-readiness/index.html",
        "acquisition-readiness/governance-traceability/index.html",
        "strategic-review/index.html",
        "reviewer-packet/index.html",
    ):
        if not (ROOT / rel).is_file():
            error(f"acquisition/strategic page missing: {rel}")
            ok = False
    return ok


def validate_boundary_hardening() -> bool:
    ok = True
    hub = (ROOT / "acquisition-readiness/index.html").read_text(encoding="utf-8")
    gt = (ROOT / "acquisition-readiness/governance-traceability/index.html").read_text(encoding="utf-8")
    cat = (ROOT / "acquisition-readiness/category-asset/index.html").read_text(encoding="utf-8")
    prs = (ROOT / "acquisition-readiness/public-reference-surface/index.html").read_text(encoding="utf-8")
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    sri = (ROOT / "strategic-review/index.html").read_text(encoding="utf-8")

    if 'id="acquisition-language-boundary"' not in hub:
        error("acquisition-readiness hub missing acquisition-language-boundary hardening")
        ok = False
    if "acquisition-readability as reviewability" not in hub:
        error("acquisition-readiness hub missing acquisition-readability framing")
        ok = False
    if 'id="acquisition-language-boundary"' not in gt:
        error("governance-traceability missing acquisition-language-boundary hardening")
        ok = False
    if "Category asset diligence pairs" in cat:
        error("category-asset still contains buyer-diligence phrasing in nav intro")
        ok = False
    if "hard to diligence" in prs:
        error("public-reference-surface still contains diligence phrasing")
        ok = False
    if "/acquisition-readiness/#acquisition-language-boundary" not in home:
        error("homepage missing acquisition language boundary link")
        ok = False
    if "/acquisition-readiness/#acquisition-language-boundary" not in sri:
        error("strategic-review index missing acquisition language boundary cross-link")
        ok = False

    for rel in PATCHED_PAGES + [p for _, p in EXTERNAL_USE]:
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
        if "DEC-143" not in dlog:
            error("new_decision_created true but DEC-143 missing from DECISION_LOG.md")
            ok = False
    elif "DEC-143" in dlog and "DEC-143 " in dlog:
        error("DEC-143 present but audit JSON says new_decision_created false")
        ok = False
    sprint_md = (ROOT / SPRINT).read_text(encoding="utf-8")
    for term in UNSAFE_TERMS:
        if unnegated(sprint_md, term):
            error(f"{SPRINT}: unnegated unsafe term {term!r}")
            ok = False
    return ok


def validate_governance_wiring() -> bool:
    ok = True
    if not any(c.get("claim_id") == "CLAIM-0128" for c in load_json("data/evidence-ledger.json").get("claims", [])):
        error("CLAIM-0128 missing")
        ok = False
    if not any(g.get("gate_id") == "PUB-GATE-0121" for g in load_json("data/publisher-quality-gates.json").get("gates", [])):
        error("PUB-GATE-0121 missing")
        ok = False
    val_all = (ROOT / "validators/validate_all.py").read_text(encoding="utf-8")
    if "validate_public_reference_acquisition_language_boundary_audit_v1.py" not in val_all:
        error("validate_all.py missing Sprint 127 validator wiring")
        ok = False
    return ok


def main() -> int:
    checks = [
        validate_artifacts(),
        validate_audit_json(),
        validate_no_expansion(),
        validate_boundary_hardening(),
        validate_terms_and_decision(),
        validate_governance_wiring(),
    ]
    if all(checks):
        print("PASS: Public Reference Acquisition Language Boundary Audit v1")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
