#!/usr/bin/env python3
"""Validate Sprint 116 — Public Reference 100-Route Surface Integrity Audit v1."""

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

AUDIT_DOC = "PUBLIC_REFERENCE_100_ROUTE_SURFACE_INTEGRITY_AUDIT_V1.md"
STANDARD_DOC = "PUBLIC_REFERENCE_100_ROUTE_SURFACE_INTEGRITY_STANDARD_V1.md"
SPRINT_DOC = "SPRINT_116_PUBLIC_REFERENCE_100_ROUTE_SURFACE_INTEGRITY_AUDIT_V1.md"
AUDIT_JSON = "data/public-reference-100-route-surface-integrity-audit-v1.json"
AUDIT_SCHEMA = "data/public-reference-100-route-surface-integrity-audit-v1.schema.json"

INDEX = "index.html"
MAP_HUB = "system-map/index.html"
ROUTE_GROUP_HUB = "route-groups/public-utilities/index.html"
AUDIENCE_HUB = "audience-paths/index.html"
EVIDENCE_HUB = "evidence-conditions/index.html"
CROSSWALK = "evidence-conditions/crosswalk/index.html"

REQUIRED_HUBS = [INDEX, MAP_HUB, ROUTE_GROUP_HUB, AUDIENCE_HUB, EVIDENCE_HUB, CROSSWALK]

STALE_ROUTE_COUNTS = [
    "58-route", "58 routes", "63-route", "63 routes", "68-route", "68 routes",
    "73-route", "73 routes", "78-route", "78 routes", "83-route", "83 routes",
    "88-route", "88 routes", "93-route", "93 routes", "99-route", "99 routes",
]

FORBIDDEN_CLAIMS = [
    "real or fake", "fake detector", "ai detector", "detects fake", "verifies truth",
    "scores authenticity", "confidence score", "upload a file", "submit evidence",
    "analyze your file", "generate report", "for sale", "asking price", "valuation",
    "term sheet", "private data room", "downloadable report", "pitch deck",
    "sales page", "scorecard", "rating system", "dashboard", "graph tool",
]

NEGATION_PATTERN = re.compile(
    r"(?:does not|do not|not a|not an|never|no |cannot|can't|without|not|prohibition|prohibited)\s+[\w\s\-/]{0,80}",
    re.IGNORECASE,
)


def error(msg: str) -> None:
    print(f"ERROR: {msg}")


def load_json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def strip_tags(html: str) -> str:
    return re.sub(r"<[^>]+>", " ", html)


def text_has_unnegated_claim(text: str, claim: str) -> bool:
    lower = re.sub(r"\s+", " ", strip_tags(text)).lower()
    pos = 0
    while True:
        idx = lower.find(claim, pos)
        if idx < 0:
            return False
        if claim == "valuation" and idx > 0 and lower[idx - 1] == "e":
            pos = idx + len(claim)
            continue
        prefix = lower[max(0, idx - 140):idx]
        if any(
            marker in lower
            for marker in (
                "does not support",
                "what this path does not",
                "what this group does not",
                "what the map does not",
                "non-transactional review boundary",
            )
        ):
            pos = idx + len(claim)
            continue
        if claim == "dashboard" and re.search(r"detector[\s-]dashboard", lower):
            pos = idx + len(claim)
            continue
        if NEGATION_PATTERN.search(prefix + claim):
            pos = idx + len(claim)
            continue
        return True


def route_to_file(path: str) -> str:
    p = path.strip("/")
    return "index.html" if not p else f"{p}/index.html"


def validate_docs() -> bool:
    ok = True
    for rel in (AUDIT_DOC, STANDARD_DOC, SPRINT_DOC):
        if not (ROOT / rel).is_file():
            error(f"{rel} missing")
            ok = False
    if ok:
        content = (ROOT / AUDIT_DOC).read_text(encoding="utf-8")
        for needle in (
            "100-route",
            "route integrity",
            "boundary integrity",
            "registry integrity",
            "retrieval integrity",
        ):
            if needle not in content:
                error(f"{AUDIT_DOC}: missing {needle!r}")
                ok = False
    return ok


def validate_data() -> bool:
    ok = True
    try:
        data = load_json(AUDIT_JSON)
        load_json(AUDIT_SCHEMA)
    except (OSError, json.JSONDecodeError) as exc:
        error(f"audit data/schema unreadable: {exc}")
        return False

    expected = {
        "decision_ref": "DEC-134",
        "sprint": "Sprint 116",
        "status": "public_reference_100_route_surface_integrity_audit",
        "audit_only": True,
        "expansion_paused": True,
        "major_milestone_route_count": 100,
        "expected_sitemap_url_count": 100,
        "expected_route_registry_count": 100,
        "expected_max_route_id": "ROUTE-0100",
        "new_public_routes_added": False,
    }
    for k, v in expected.items():
        if data.get(k) != v:
            error(f"{AUDIT_JSON}: {k} must be {v!r}")
            ok = False

    for key in data:
        if key.endswith("_authorized") and data[key] is not False:
            error(f"{AUDIT_JSON}: {key} must be false")
            ok = False
    return ok


def validate_counts_and_alignment() -> bool:
    ok = True
    locs = [x.text.strip() for x in ET.parse(ROOT / "sitemap.xml").findall(".//{*}loc") if x.text]
    if len(locs) != PUBLIC_SITEMAP_URL_COUNT:
        error(f"sitemap must contain {PUBLIC_SITEMAP_URL_COUNT} URLs")
        ok = False

    reg = load_json("data/route-registry.json").get("routes", [])
    if len(reg) != PUBLIC_SITEMAP_URL_COUNT:
        error(f"route registry must contain {PUBLIC_SITEMAP_URL_COUNT} entries")
        ok = False

    if not validate_public_surface(reg, error, PUBLIC_SITEMAP_URL_COUNT):
        ok = False

    route_ids = [r.get("route_id", "") for r in reg]
    if len(route_ids) != len(set(route_ids)):
        error("duplicate route_id entries in route registry")
        ok = False
    if "ROUTE-0100" not in route_ids:
        error("ROUTE-0100 missing")
        ok = False
    if any(rid > "ROUTE-0100" for rid in route_ids):
        error("route_id beyond ROUTE-0100 found")
        ok = False

    route_paths = {r.get("path") for r in reg}
    sitemap_paths = {"/" + loc.split("https://hoax.ai/", 1)[1] for loc in locs if loc.startswith("https://hoax.ai/")}
    if route_paths != sitemap_paths:
        error("sitemap and route-registry path sets mismatch")
        ok = False

    files = load_json("data/public-file-registry.json").get("public_files", [])
    route_file_paths = {route_to_file(p) for p in route_paths}
    pf_route_files = {f.get("path") for f in files if f.get("route_id_if_applicable")}
    missing_pf = sorted(route_file_paths - pf_route_files)
    if missing_pf:
        error(f"public-file-registry missing route files: {missing_pf[:5]}")
        ok = False

    return ok


def validate_public_html_integrity() -> bool:
    ok = True
    for rel in sorted(ALLOWED_PUBLIC_HTML):
        content = (ROOT / rel).read_text(encoding="utf-8")
        lower = content.lower()

        if len(re.findall(r"<h1[ >]", lower)) != 1:
            error(f"{rel}: expected exactly one H1")
            ok = False

        for needle in ('<title>', 'rel="canonical"', 'name="description"', "og:title", "og:description"):
            if needle not in lower:
                error(f"{rel}: missing {needle}")
                ok = False

        for stale in STALE_ROUTE_COUNTS:
            if stale in lower:
                error(f"{rel}: stale route-count language {stale!r}")
                ok = False

        for claim in FORBIDDEN_CLAIMS:
            if text_has_unnegated_claim(content, claim):
                error(f"{rel}: forbidden claim {claim!r} outside negation")
                ok = False

        for bad in ("<form", "<input", "<textarea", "<select"):
            if bad in lower:
                error(f"{rel}: prohibited interactive element {bad}")
                ok = False
    return ok


def validate_internal_links() -> bool:
    ok = True
    route_paths = {r.get("path") for r in load_json("data/route-registry.json").get("routes", [])}
    href_pat = re.compile(r'href="(/[^"#?]+/?)"')
    for rel in sorted(ALLOWED_PUBLIC_HTML):
        content = (ROOT / rel).read_text(encoding="utf-8")
        for target in href_pat.findall(content):
            if target in ("/", "/#public-release-integrity-snapshot", "/#navigation-backbone-snapshot"):
                continue
            norm = target if target.endswith("/") else target + "/"
            if norm not in route_paths:
                error(f"{rel}: broken internal route link {target}")
                ok = False
    return ok


def validate_hubs_and_retrieval() -> bool:
    ok = True
    for rel in REQUIRED_HUBS:
        content = (ROOT / rel).read_text(encoding="utf-8")
        if "Reference summary" not in content and rel != INDEX:
            error(f"{rel}: missing reference summary wording")
            ok = False
    if "Current public route count: 100" not in (ROOT / INDEX).read_text(encoding="utf-8"):
        error("index.html must include Current public route count: 100")
        ok = False
    return ok


def validate_governance_and_wiring() -> bool:
    ok = True
    log = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")
    if "DEC-134" not in log:
        error("DEC-134 missing")
        ok = False
    if log.find("DEC-133") > log.find("DEC-134"):
        error("DECISION_LOG chronology invalid: DEC-134 must follow DEC-133")
        ok = False

    if "validate_public_reference_100_route_surface_integrity_audit_v1.py" not in (
        ROOT / "validators/validate_all.py"
    ).read_text(encoding="utf-8"):
        error("validate_all.py must include the Sprint 116 validator")
        ok = False

    locs = {s.get("location") for s in load_json("data/source-registry.json").get("sources", [])}
    for rel in (AUDIT_DOC, STANDARD_DOC, SPRINT_DOC, AUDIT_JSON, AUDIT_SCHEMA, "validators/validate_public_reference_100_route_surface_integrity_audit_v1.py"):
        if rel not in locs:
            error(f"source-registry missing {rel}")
            ok = False

    if not any(c.get("claim_id") == "CLAIM-0117" for c in load_json("data/evidence-ledger.json").get("claims", [])):
        error("CLAIM-0117 missing in evidence-ledger")
        ok = False

    if not any(g.get("gate_id") == "PUB-GATE-0110" for g in load_json("data/publisher-quality-gates.json").get("gates", [])):
        error("PUB-GATE-0110 missing in publisher-quality-gates")
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
        validate_docs,
        validate_data,
        validate_counts_and_alignment,
        validate_public_html_integrity,
        validate_internal_links,
        validate_hubs_and_retrieval,
        validate_governance_and_wiring,
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
