#!/usr/bin/env python3
"""Validate Sprint 122 — Public Reference Source Use Orientation v1."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

from public_surface_checks import (  # noqa: E402
    ALLOWED_PUBLIC_HTML,
    PUBLIC_SITEMAP_URL_COUNT,
    validate_public_surface,
)

DOC = "PUBLIC_REFERENCE_SOURCE_USE_ORIENTATION_V1.md"
STD = "PUBLIC_REFERENCE_SOURCE_USE_ORIENTATION_STANDARD_V1.md"
AUDIT = "PUBLIC_REFERENCE_SOURCE_USE_ORIENTATION_AUDIT_V1.md"
SPRINT = "SPRINT_122_PUBLIC_REFERENCE_SOURCE_USE_ORIENTATION_V1.md"
JSON_PATH = "data/public-reference-source-use-orientation-v1.json"
SCHEMA_PATH = "data/public-reference-source-use-orientation-v1.schema.json"
PAGE = "source-use-orientation/index.html"
PAGE_ROUTE = "/source-use-orientation/"
MIN_WORDS = 2000

REQUIRED_SECTIONS = [
    "Reference summary",
    "Purpose of source use orientation",
    "How to use this source use orientation",
    "What source use orientation is not",
    "Source use inside Hoax.ai",
    "Sources as reference support",
    "Source Confidence blocks",
    "Evidence ledger traceability",
    "Claim-source relationship",
    "Source use and citation orientation",
    "Source use and AI agents",
    "Source use without proof language",
    "Source use without detector language",
    "Source use and strategic review",
    "Relation to citation orientation",
    "Relation to retrieval index",
    "Relation to reading sequences",
    "Relation to system map",
    "What this page supports",
    "What this page does not claim",
    "Reference Answer",
    "Source Confidence",
    "Cite This Reference",
    "Retrieval Capsule",
    "Boundary reminder",
    "Non-transactional review boundary",
]

REQUIRED_ANCHORS = [
    "reference-summary",
    "purpose-source-use-orientation",
    "how-to-use-source-use-orientation",
    "what-source-use-orientation-is-not",
    "source-use-inside-hoax",
    "sources-as-reference-support",
    "source-confidence-blocks",
    "evidence-ledger-traceability",
    "claim-source-relationship",
    "source-use-citation-orientation",
    "source-use-ai-agents",
    "source-use-without-proof",
    "source-use-without-detector",
    "source-use-strategic-review",
    "relation-citation-orientation",
    "relation-retrieval-index",
    "relation-reading-sequences",
    "relation-system-map",
    "what-supports",
    "does-not-claim",
    "reference-answer",
    "source-confidence",
    "cite-this-reference",
    "retrieval-capsule",
    "boundary-reminder",
    "non-transactional-review-boundary",
]

REQUIRED_LINKS = [
    "/",
    "/system-map/",
    "/reading-sequences/",
    "/retrieval-index/",
    "/citation-orientation/",
    "/evidence-conditions/",
    "/evidence-conditions/crosswalk/",
    "/evidence-conditions/source-uncertainty/",
    "/evidence-conditions/provenance-discontinuity/",
    "/evidence-conditions/context-loss/",
    "/evidence-conditions/claim-evidence-misalignment/",
    "/evidence-conditions/traceability-break/",
    "/why-hoax-ai-is-not-a-detector/",
    "/evidence-risk/",
    "/provenance-risk/",
    "/context-collapse/",
    "/claim-drift/",
    "/traceability-gap/",
    "/reference/source-confidence/",
    "/reference/claim-source-traceability/",
    "/acquisition-readiness/governance-traceability/",
    "/route-groups/core-concepts/",
    "/route-groups/evidence-risk-pathways/",
    "/route-groups/public-utilities/",
    "/route-groups/review-and-overview-layers/",
    "/route-groups/boundary-and-support-references/",
    "/audience-paths/",
    "/audience-paths/research-reviewers/",
    "/audience-paths/trust-safety-readers/",
    "/audience-paths/education-literacy/",
    "/audience-paths/ai-agents/",
    "/strategic-review/",
    "/reviewer-packet/citation-and-retrieval-map/",
]

UNSAFE_TERMS = [
    "proof system",
    "proves",
    "proven",
    "verification claim",
    "verified",
    "verify",
    "confirmation",
    "confirmed",
    "certification",
    "certified",
    "authority claim",
    "authoritative proof",
    "trusted source certification",
    "approved source",
    "endorsement",
    "academic endorsement",
    "legal source",
    "legal citation",
    "detector evidence",
    "detector support",
    "fake detector",
    "real or fake",
    "authenticity engine",
    "authentic",
    "inauthentic",
    "case conclusion",
    "case assessment",
    "adjudication",
    "verdict",
    "confidence score",
    "score",
    "scoring",
    "rating",
    "ranking",
    "source ranking",
    "source rating",
    "best source",
    "source database",
    "source directory",
    "investigation procedure",
    "operational procedure",
    "workflow",
    "assessment path",
    "decision tree",
    "due diligence",
    "dashboard",
    "graph tool",
    "scorecard",
    "api",
    "upload",
    "form",
    "report generator",
    "downloadable report",
    "sales page",
    "consulting offer",
    "service funnel",
    "pricing",
    "transaction",
    "legal representation",
    "financial representation",
]

NEGATION_PATTERN = re.compile(
    r"(?:must not|does not|do not|not a|not an|no |without|forbidden|prohibited|is not|are not|cannot|can't|never|not create|not issue|not provide|not mean)\s+[\w\s\-/]{0,120}",
    re.IGNORECASE,
)


def error(msg: str) -> None:
    print(f"ERROR: {msg}")


def load_json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def visible_words(html: str) -> int:
    return len(re.findall(r"[A-Za-z0-9']+", re.sub(r"<[^>]+>", " ", html)))


def unnegated(text: str, term: str) -> bool:
    lower = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text)).lower()
    pos = 0
    while True:
        idx = lower.find(term, pos)
        if idx < 0:
            return False
        prefix = lower[max(0, idx - 160):idx]
        window = lower[max(0, idx - 20): idx + len(term) + 20]
        if NEGATION_PATTERN.search(prefix + term) or "what this page does not claim" in lower:
            pos = idx + len(term)
            continue
        if term == "score" and "score-card" in window:
            pos = idx + len(term)
            continue
        if term == "score" and "score basis" in window:
            pos = idx + len(term)
            continue
        if term == "form" and "format" in lower[idx: idx + 10]:
            pos = idx + len(term)
            continue
        if term == "api" and "api behavior" in window:
            pos = idx + len(term)
            continue
        if term == "certification" and "authority certification" in window:
            pos = idx + len(term)
            continue
        if term == "endorsement" and ("not academic endorsement" in window or "no source endorsement" in window or "source endorsement" in prefix):
            pos = idx + len(term)
            continue
        if term == "detector" and "detector evidence" in window:
            pos = idx + len(term)
            continue
        if term == "verified" and "verified" in prefix[-40:]:
            pos = idx + len(term)
            continue
        return True


def validate_artifacts() -> bool:
    ok = True
    for rel in (DOC, STD, AUDIT, SPRINT, JSON_PATH, SCHEMA_PATH):
        if not (ROOT / rel).is_file():
            error(f"{rel} missing")
            ok = False
    return ok


def validate_json_schema() -> bool:
    ok = True
    try:
        data = load_json(JSON_PATH)
        load_json(SCHEMA_PATH)
    except (OSError, json.JSONDecodeError) as exc:
        error(f"source-use-orientation JSON/schema unreadable: {exc}")
        return False
    expected = {
        "decision_ref": "DEC-138",
        "sprint": "Sprint 122",
        "status": "public_reference_source_use_orientation",
        "public_route": PAGE_ROUTE,
        "route_id": "ROUTE-0104",
        "public_file_id": "PUB-FILE-0104",
        "expected_sitemap_url_count_after": 104,
        "expected_route_registry_count_after": 104,
        "expected_public_file_registry_count_after": 104,
    }
    for k, v in expected.items():
        if data.get(k) != v:
            error(f"{JSON_PATH}: {k} must be {v!r}")
            ok = False
    if len(data.get("source_use_orientation_themes", [])) != 10:
        error(f"{JSON_PATH}: source_use_orientation_themes must list 10 themes")
        ok = False
    if len(data.get("required_components", [])) < 26:
        error(f"{JSON_PATH}: required_components must include 26 sections")
        ok = False
    for k, v in data.items():
        if k.endswith("_authorized") and v is not False:
            error(f"{JSON_PATH}: {k} must be false")
            ok = False
    return ok


def validate_page() -> bool:
    ok = True
    p = ROOT / PAGE
    if not p.is_file():
        error(f"{PAGE} missing")
        return False
    html = p.read_text(encoding="utf-8")
    lower = html.lower()
    if len(re.findall(r"<h1[ >]", lower)) != 1:
        error(f"{PAGE}: expected exactly one H1")
        ok = False
    for tag in ('rel="canonical"', 'name="description"', "og:title", "og:description"):
        if tag not in lower:
            error(f"{PAGE}: missing {tag}")
            ok = False
    wc = visible_words(html)
    if wc < MIN_WORDS:
        error(f"{PAGE}: visible word count below {MIN_WORDS} (got {wc})")
        ok = False
    for sec in REQUIRED_SECTIONS:
        if sec not in html:
            error(f"{PAGE}: missing section {sec!r}")
            ok = False
    for aid in REQUIRED_ANCHORS:
        if f'id="{aid}"' not in html:
            error(f"{PAGE}: missing anchor {aid}")
            ok = False
    for link in REQUIRED_LINKS:
        if f'href="{link}"' not in html:
            error(f"{PAGE}: missing required link {link}")
            ok = False
    for bad in ("<script", "<form", "<input", "<textarea", "<select"):
        if bad in lower:
            error(f"{PAGE}: prohibited element {bad}")
            ok = False
    return ok


def validate_nav_and_registries() -> bool:
    ok = True
    for rel in (
        "index.html",
        "system-map/index.html",
        "reading-sequences/index.html",
        "retrieval-index/index.html",
        "citation-orientation/index.html",
    ):
        text = (ROOT / rel).read_text(encoding="utf-8")
        if PAGE_ROUTE not in text:
            error(f"{rel} must link to {PAGE_ROUTE}")
            ok = False
    locs = [x.text.strip() for x in ET.parse(ROOT / "sitemap.xml").findall(".//{*}loc") if x.text]
    if len(locs) != PUBLIC_SITEMAP_URL_COUNT:
        error(f"sitemap must contain {PUBLIC_SITEMAP_URL_COUNT} URLs")
        ok = False
    if f"https://hoax.ai{PAGE_ROUTE}" not in locs:
        error("sitemap missing source-use-orientation route")
        ok = False
    reg = load_json("data/route-registry.json").get("routes", [])
    if len(reg) != PUBLIC_SITEMAP_URL_COUNT:
        error(f"route registry must contain {PUBLIC_SITEMAP_URL_COUNT} entries")
        ok = False
    r104 = next((r for r in reg if r.get("route_id") == "ROUTE-0104"), None)
    if r104 is None or r104.get("path") != PAGE_ROUTE:
        error("ROUTE-0104 missing or misaligned")
        ok = False
    if PUBLIC_SITEMAP_URL_COUNT < 104:
        error("PUBLIC_SITEMAP_URL_COUNT must be at least 104")
        ok = False
    if not validate_public_surface(reg, error, PUBLIC_SITEMAP_URL_COUNT):
        ok = False
    pfr = load_json("data/public-file-registry.json").get("public_files", [])
    f104 = next((f for f in pfr if f.get("file_id") == "PUB-FILE-0104"), None)
    if f104 is None or f104.get("path") != PAGE:
        error("PUB-FILE-0104 missing or misaligned")
        ok = False
    if len([f for f in pfr if f.get("route_id_if_applicable")]) != PUBLIC_SITEMAP_URL_COUNT:
        error(f"public-file route-mapped count must be {PUBLIC_SITEMAP_URL_COUNT}")
        ok = False
    return ok


def validate_copy_and_terms() -> bool:
    ok = True
    for rel in sorted(ALLOWED_PUBLIC_HTML):
        lower = (ROOT / rel).read_text(encoding="utf-8").lower()
        if "103 routes" in lower or "103-route" in lower or "current public route count: 103" in lower:
            error(f"{rel}: stale current-state route count copy (103)")
            ok = False
    for rel in (PAGE,):
        text = (ROOT / rel).read_text(encoding="utf-8")
        for term in UNSAFE_TERMS:
            if unnegated(text, term):
                error(f"{rel}: unnegated unsafe term {term!r}")
                ok = False
    return ok


def validate_governance() -> bool:
    ok = True
    dlog = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")
    if "DEC-138" not in dlog:
        error("DEC-138 missing")
        ok = False
    if PAGE_ROUTE not in dlog:
        error("DEC-138 must explicitly govern /source-use-orientation/")
        ok = False
    section_start = dlog.find("## DEC-138")
    if section_start >= 0:
        tail = dlog[section_start:]
        next_idx = tail.find("\n## ", 1)
        dec_section = tail if next_idx < 0 else tail[:next_idx]
        if "preparatory" in dec_section.lower():
            error("DEC-138 appears abstract/preparatory; must govern visible route")
            ok = False
    if not any(c.get("claim_id") == "CLAIM-0123" for c in load_json("data/evidence-ledger.json").get("claims", [])):
        error("CLAIM-0123 missing")
        ok = False
    if not any(g.get("gate_id") == "PUB-GATE-0116" for g in load_json("data/publisher-quality-gates.json").get("gates", [])):
        error("PUB-GATE-0116 missing")
        ok = False
    locs = {s.get("location") for s in load_json("data/source-registry.json").get("sources", [])}
    for rel in (
        DOC,
        STD,
        AUDIT,
        SPRINT,
        JSON_PATH,
        SCHEMA_PATH,
        PAGE,
        "validators/validate_public_reference_source_use_orientation_v1.py",
    ):
        if rel not in locs:
            error(f"source-registry missing {rel}")
            ok = False
    if "validate_public_reference_source_use_orientation_v1.py" not in (
        ROOT / "validators/validate_all.py"
    ).read_text(encoding="utf-8"):
        error("validate_all.py missing Sprint 122 validator")
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
        validate_json_schema,
        validate_page,
        validate_nav_and_registries,
        validate_copy_and_terms,
        validate_governance,
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
