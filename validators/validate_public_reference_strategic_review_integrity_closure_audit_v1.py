#!/usr/bin/env python3
"""Validate Sprint 128 — Public Reference Strategic Review Integrity Closure Audit v1."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

from public_surface_checks import PUBLIC_SITEMAP_URL_COUNT  # noqa: E402

AUDIT_MD = "PUBLIC_REFERENCE_STRATEGIC_REVIEW_INTEGRITY_CLOSURE_AUDIT_V1.md"
SPRINT = "SPRINT_128_PUBLIC_REFERENCE_STRATEGIC_REVIEW_INTEGRITY_CLOSURE_AUDIT_V1.md"
JSON_PATH = "data/public-reference-strategic-review-integrity-closure-audit-v1.json"
SCHEMA_PATH = "data/public-reference-strategic-review-integrity-closure-audit-v1.schema.json"

EXTERNAL_USE = [
    ("/reading-sequences/", "reading-sequences/index.html"),
    ("/retrieval-index/", "retrieval-index/index.html"),
    ("/citation-orientation/", "citation-orientation/index.html"),
    ("/source-use-orientation/", "source-use-orientation/index.html"),
]

PATCHED_PAGES = [
    "strategic-review/index.html",
    "reviewer-packet/index.html",
    "system-map/index.html",
    "acquisition-readiness/index.html",
    "index.html",
]

REQUIRED_SCENARIO_FIELDS = [
    "scenario_id",
    "strategic_review_intent",
    "expected_pages_checked",
    "expected_safe_interpretation",
    "actual_interpretation",
    "supporting_routes_or_artifacts",
    "result",
    "observed_issue",
    "repair_applied",
    "strategic_integrity_check",
    "boundary_check",
    "ai_agent_note",
]

DRIFT_FLAGS = [
    "route_count_drift_found",
    "stale_copy_found",
    "role_confusion_found",
    "link_imbalance_found",
    "unsupported_claim_found",
    "overclaim_found",
    "trace_gap_found",
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
    "certified source",
    "verified authority",
    "proof engine",
    "detector evidence",
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
    for sprint_artifact in (
        "PUBLIC_REFERENCE_STRATEGIC_REVIEWER_SURFACE_AUDIT_V1.md",
        "PUBLIC_REFERENCE_STRATEGIC_CLAIM_TRACEABILITY_AUDIT_V1.md",
        "PUBLIC_REFERENCE_ACQUISITION_LANGUAGE_BOUNDARY_AUDIT_V1.md",
    ):
        if not (ROOT / sprint_artifact).is_file():
            error(f"Phase 3 prerequisite artifact missing: {sprint_artifact}")
            ok = False
    return ok


def validate_audit_json() -> bool:
    ok = True
    data = load_json(JSON_PATH)
    load_json(SCHEMA_PATH)
    expected = {
        "audit_only": True,
        "phase": "Phase 3",
        "phase_closure_candidate": True,
        "production_route_added": False,
        "public_route_count_before": 104,
        "public_route_count_after": 104,
        "sitemap_url_count_expected": 104,
        "route_registry_changed": False,
        "public_file_registry_changed": False,
        "no_new_routes": True,
        "new_decision_created": False,
        "boundary_regressions_found": False,
        "strategic_review_integrity_confirmed": True,
        "reviewer_legibility_confirmed": True,
        "strategic_claim_traceability_confirmed": True,
        "acquisition_language_boundary_confirmed": True,
        "phase_2_support_confirmed": True,
        "phase_3_closure_recommended": True,
        "ai_agent_strategic_interpretation_confirmed": True,
        "human_reviewer_strategic_interpretation_confirmed": True,
    }
    for k, v in expected.items():
        if data.get(k) != v:
            error(f"{JSON_PATH}: {k} must be {v!r}")
            ok = False
    for flag in DRIFT_FLAGS:
        if data.get(flag) is not False:
            error(f"{JSON_PATH}: {flag} must be false")
            ok = False
    p3 = data.get("phase_3_components_checked", {})
    for key in (
        "strategic_reviewer_surface_integrity",
        "strategic_claim_traceability",
        "acquisition_language_boundary",
    ):
        if not p3.get(key):
            error(f"{JSON_PATH}: phase_3_components_checked.{key} must be true")
            ok = False
    scenarios = data.get("walkthrough_scenarios", [])
    if len(scenarios) < 28:
        error(f"{JSON_PATH}: must include at least 28 scenarios")
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
    ext = data.get("phase_2_support_layers_checked", {})
    for route, _ in EXTERNAL_USE:
        if not ext.get(route):
            error(f"{JSON_PATH}: phase_2_support_layers_checked missing {route}")
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
        error("PUB-FILE-0105 must not exist after Sprint 128 audit-only sprint")
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
        "strategic-review/index.html",
        "reviewer-packet/index.html",
        "acquisition-readiness/index.html",
        "acquisition-readiness/governance-traceability/index.html",
    ):
        if not (ROOT / rel).is_file():
            error(f"strategic/reviewer page missing: {rel}")
            ok = False
    return ok


def validate_closure_hardening() -> bool:
    ok = True
    sri = (ROOT / "strategic-review/index.html").read_text(encoding="utf-8")
    rpi = (ROOT / "reviewer-packet/index.html").read_text(encoding="utf-8")
    smap = (ROOT / "system-map/index.html").read_text(encoding="utf-8")
    arh = (ROOT / "acquisition-readiness/index.html").read_text(encoding="utf-8")
    home = (ROOT / "index.html").read_text(encoding="utf-8")

    if 'id="phase-3-strategic-review-integrity"' not in sri:
        error("strategic-review index missing phase-3-strategic-review-integrity hardening")
        ok = False
    if 'id="strategic-claim-traceability"' not in sri:
        error("strategic-review index missing strategic-claim-traceability section")
        ok = False
    if "phase-3-strategic-review-integrity" not in rpi:
        error("reviewer-packet hub missing Phase 3 integrity hardening")
        ok = False
    if "phase-3-strategic-review-integrity" not in smap:
        error("system-map missing Phase 3 integrity link")
        ok = False
    if "phase-3-strategic-review-integrity" not in arh:
        error("acquisition-readiness hub missing Phase 3 integrity cross-link")
        ok = False
    if "phase-3-strategic-review-integrity" not in home:
        error("homepage missing Phase 3 integrity orientation")
        ok = False
    if "diligence notes do not overclaim" in sri:
        error("strategic-review index still contains diligence-notes phrasing in index-depth")
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
        if "DEC-144" not in dlog:
            error("new_decision_created true but DEC-144 missing from DECISION_LOG.md")
            ok = False
    elif "DEC-144" in dlog and "DEC-144 " in dlog:
        error("DEC-144 present but audit JSON says new_decision_created false")
        ok = False
    sprint_md = (ROOT / SPRINT).read_text(encoding="utf-8")
    for term in UNSAFE_TERMS:
        if unnegated(sprint_md, term):
            error(f"{SPRINT}: unnegated unsafe term {term!r}")
            ok = False
    return ok


def validate_governance_wiring() -> bool:
    ok = True
    if not any(c.get("claim_id") == "CLAIM-0129" for c in load_json("data/evidence-ledger.json").get("claims", [])):
        error("CLAIM-0129 missing")
        ok = False
    if not any(g.get("gate_id") == "PUB-GATE-0122" for g in load_json("data/publisher-quality-gates.json").get("gates", [])):
        error("PUB-GATE-0122 missing")
        ok = False
    val_all = (ROOT / "validators/validate_all.py").read_text(encoding="utf-8")
    if "validate_public_reference_strategic_review_integrity_closure_audit_v1.py" not in val_all:
        error("validate_all.py missing Sprint 128 validator wiring")
        ok = False
    return ok


def main() -> int:
    checks = [
        validate_artifacts(),
        validate_audit_json(),
        validate_no_expansion(),
        validate_closure_hardening(),
        validate_terms_and_decision(),
        validate_governance_wiring(),
    ]
    if all(checks):
        print("PASS: Public Reference Strategic Review Integrity Closure Audit v1")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
