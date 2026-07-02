#!/usr/bin/env python3
"""Validate Sprint 117 — Public Reference Reading Sequences v1."""

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

DOC = "PUBLIC_REFERENCE_READING_SEQUENCES_V1.md"
STD = "PUBLIC_REFERENCE_READING_SEQUENCE_STANDARD_V1.md"
AUDIT = "PUBLIC_REFERENCE_READING_SEQUENCES_AUDIT_V1.md"
SPRINT = "SPRINT_117_PUBLIC_REFERENCE_READING_SEQUENCES_V1.md"
JSON_PATH = "data/public-reference-reading-sequences-v1.json"
SCHEMA_PATH = "data/public-reference-reading-sequences-v1.schema.json"

PAGE = "reading-sequences/index.html"
PAGE_ROUTE = "/reading-sequences/"
MIN_WORDS = 2000

REQUIRED_SECTIONS = [
    "Reference summary",
    "Purpose of reading sequences",
    "How to use this page",
    "What reading sequences are not",
    "First-time reader sequence",
    "Evidence condition sequence",
    "AI agent retrieval sequence",
    "Research reviewer sequence",
    "Trust and safety reader sequence",
    "Education and literacy sequence",
    "Strategic reviewer sequence",
    "Relation to the system map",
    "Relation to the evidence condition crosswalk",
    "Relation to route groups",
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
    "purpose-reading-sequences",
    "how-to-use-page",
    "what-not",
    "first-time-reader-sequence",
    "evidence-condition-sequence",
    "ai-agent-retrieval-sequence",
    "research-reviewer-sequence",
    "trust-safety-sequence",
    "education-literacy-sequence",
    "strategic-reviewer-sequence",
    "relation-system-map",
    "relation-crosswalk",
    "relation-route-groups",
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
    "/evidence-conditions/",
    "/evidence-conditions/crosswalk/",
    "/why-hoax-ai-is-not-a-detector/",
    "/evidence-risk/",
    "/provenance-risk/",
    "/context-collapse/",
    "/claim-drift/",
    "/traceability-gap/",
    "/route-groups/core-concepts/",
    "/route-groups/evidence-risk-pathways/",
    "/audience-paths/research-reviewers/",
    "/audience-paths/trust-safety-readers/",
    "/audience-paths/education-literacy/",
    "/audience-paths/ai-agents/",
]

UNSAFE_TERMS = [
    "workflow",
    "assessment path",
    "decision path",
    "decision tree",
    "investigation procedure",
    "operational procedure",
    "risk ranking",
    "severity order",
    "confidence order",
    "verification workflow",
    "due diligence sequence",
    "case review process",
]

BEHAVIOR_TERMS = [
    "upload a file",
    "submit evidence",
    "scorecard",
    "rating system",
    "dashboard",
    "graph tool",
    "public api",
    "transaction page",
    "sales page",
    "consulting offer",
    "service funnel",
    "legal representation",
    "financial representation",
]

NEGATION_PATTERN = re.compile(
    r"(?:does not|do not|not a|not an|never|no |cannot|can't|without|not|prohibition|prohibited|forbidden)\s+[\w\s\-/]{0,80}",
    re.IGNORECASE,
)


def error(msg: str) -> None:
    print(f"ERROR: {msg}")


def load_json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def visible_words(html: str) -> int:
    text = re.sub(r"<[^>]+>", " ", html)
    return len(re.findall(r"[A-Za-z0-9']+", text))


def unnegated_term_present(text: str, term: str) -> bool:
    lower = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text)).lower()
    pos = 0
    while True:
        idx = lower.find(term, pos)
        if idx < 0:
            return False
        if any(
            marker in lower
            for marker in (
                "must not",
                "does not",
                "do not",
                "not a",
                "not an",
                "forbidden",
                "prohibition",
                "what this page does not claim",
                "non-transactional review boundary",
            )
        ):
            pos = idx + len(term)
            continue
        prefix = lower[max(0, idx - 140):idx]
        if NEGATION_PATTERN.search(prefix + term):
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


def validate_data_json() -> bool:
    ok = True
    try:
        data = load_json(JSON_PATH)
        load_json(SCHEMA_PATH)
    except (OSError, json.JSONDecodeError) as exc:
        error(f"reading-sequences JSON/schema unreadable: {exc}")
        return False

    expected = {
        "decision_ref": "DEC-135",
        "sprint": "Sprint 117",
        "status": "public_reference_reading_sequences",
        "public_route": PAGE_ROUTE,
        "route_id": "ROUTE-0101",
        "public_file_id": "PUB-FILE-0101",
        "expected_sitemap_url_count_after": 101,
        "expected_route_registry_count_after": 101,
        "expected_public_file_registry_count_after": 101,
    }
    for k, v in expected.items():
        if data.get(k) != v:
            error(f"{JSON_PATH}: {k} must be {v!r}")
            ok = False

    if len(data.get("reading_sequences", [])) != 7:
        error(f"{JSON_PATH}: reading_sequences must list 7 sequences")
        ok = False
    if len(data.get("required_components", [])) < 22:
        error(f"{JSON_PATH}: required_components must contain 22 entries")
        ok = False

    for key in data:
        if key.endswith("_authorized") and data[key] is not False:
            error(f"{JSON_PATH}: {key} must be false")
            ok = False
    return ok


def validate_page_structure() -> bool:
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

    if visible_words(html) < MIN_WORDS:
        error(f"{PAGE}: visible word count below {MIN_WORDS}")
        ok = False

    for sec in REQUIRED_SECTIONS:
        if sec not in html:
            error(f"{PAGE}: missing section {sec!r}")
            ok = False
    for anchor in REQUIRED_ANCHORS:
        if f'id="{anchor}"' not in html:
            error(f"{PAGE}: missing anchor {anchor}")
            ok = False
    for route in REQUIRED_LINKS:
        if f'href="{route}"' not in html:
            error(f"{PAGE}: missing required link {route}")
            ok = False

    for bad in ("<script", "<form", "<input", "<textarea", "<select"):
        if bad in lower:
            error(f"{PAGE}: contains prohibited interactive element {bad}")
            ok = False
    return ok


def validate_navigation_and_registries() -> bool:
    ok = True
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    smap = (ROOT / "system-map/index.html").read_text(encoding="utf-8")
    cross = (ROOT / "evidence-conditions/crosswalk/index.html").read_text(encoding="utf-8")
    for rel, text in (
        ("index.html", home),
        ("system-map/index.html", smap),
        ("evidence-conditions/crosswalk/index.html", cross),
    ):
        if PAGE_ROUTE not in text:
            error(f"{rel} must link to {PAGE_ROUTE}")
            ok = False

    locs = [x.text.strip() for x in ET.parse(ROOT / "sitemap.xml").findall(".//{*}loc") if x.text]
    if len(locs) != PUBLIC_SITEMAP_URL_COUNT:
        error(f"sitemap must contain {PUBLIC_SITEMAP_URL_COUNT} URLs")
        ok = False
    if f"https://hoax.ai{PAGE_ROUTE}" not in locs:
        error("sitemap missing reading-sequences route")
        ok = False

    reg = load_json("data/route-registry.json").get("routes", [])
    if len(reg) != PUBLIC_SITEMAP_URL_COUNT:
        error(f"route registry must contain {PUBLIC_SITEMAP_URL_COUNT} entries")
        ok = False
    r101 = next((r for r in reg if r.get("route_id") == "ROUTE-0101"), None)
    if r101 is None or r101.get("path") != PAGE_ROUTE:
        error("ROUTE-0101 missing or misaligned")
        ok = False

    if not validate_public_surface(reg, error, PUBLIC_SITEMAP_URL_COUNT):
        ok = False

    pfr = load_json("data/public-file-registry.json").get("public_files", [])
    f101 = next((f for f in pfr if f.get("file_id") == "PUB-FILE-0101"), None)
    if f101 is None or f101.get("path") != PAGE:
        error("PUB-FILE-0101 missing or misaligned")
        ok = False

    route_mapped = [f for f in pfr if f.get("route_id_if_applicable")]
    if len(route_mapped) != PUBLIC_SITEMAP_URL_COUNT:
        error(f"public-file registry route-mapped count must be {PUBLIC_SITEMAP_URL_COUNT}")
        ok = False
    return ok


def validate_copy_and_boundary_terms() -> bool:
    ok = True
    for rel in sorted(ALLOWED_PUBLIC_HTML):
        text = (ROOT / rel).read_text(encoding="utf-8")
        lower = text.lower()
        if "100-route" in lower or "100 routes" in lower:
            error(f"{rel}: stale current-state route count copy (100)")
            ok = False

    check_files = [
        PAGE,
        DOC,
        STD,
    ]
    for rel in check_files:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for term in UNSAFE_TERMS + BEHAVIOR_TERMS:
            if unnegated_term_present(text, term):
                error(f"{rel}: unnegated unsafe term {term!r}")
                ok = False
    return ok


def validate_governance_wiring() -> bool:
    ok = True
    dlog = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")
    if "DEC-135" not in dlog:
        error("DEC-135 missing")
        ok = False
    if dlog.find("DEC-134") > dlog.find("DEC-135"):
        error("DECISION_LOG chronology invalid (DEC-135 before DEC-134)")
        ok = False

    if not any(c.get("claim_id") == "CLAIM-0118" for c in load_json("data/evidence-ledger.json").get("claims", [])):
        error("CLAIM-0118 missing")
        ok = False
    if not any(g.get("gate_id") == "PUB-GATE-0111" for g in load_json("data/publisher-quality-gates.json").get("gates", [])):
        error("PUB-GATE-0111 missing")
        ok = False

    locs = {s.get("location") for s in load_json("data/source-registry.json").get("sources", [])}
    for rel in (
        DOC,
        STD,
        AUDIT,
        SPRINT,
        JSON_PATH,
        SCHEMA_PATH,
        "validators/validate_public_reference_reading_sequences_v1.py",
    ):
        if rel not in locs:
            error(f"source-registry missing {rel}")
            ok = False

    if "validate_public_reference_reading_sequences_v1.py" not in (
        ROOT / "validators/validate_all.py"
    ).read_text(encoding="utf-8"):
        error("validate_all.py missing Sprint 117 validator")
        ok = False

    if (ROOT / ".nojekyll").exists():
        error(".nojekyll exists")
        ok = False

    names = subprocess.run(["git", "ls-files"], cwd=ROOT, text=True, capture_output=True).stdout.splitlines()
    names += subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=ROOT, text=True, capture_output=True).stdout.splitlines()
    for rel in names:
        if "__pycache__" in rel or rel.endswith(".pyc"):
            error(f"python cache file tracked or staged: {rel}")
            ok = False
    return ok


def main() -> int:
    ok = True
    for check in (
        validate_artifacts,
        validate_data_json,
        validate_page_structure,
        validate_navigation_and_registries,
        validate_copy_and_boundary_terms,
        validate_governance_wiring,
    ):
        if not check():
            ok = False
    if not ok:
        print("FAIL")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
