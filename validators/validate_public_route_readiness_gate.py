#!/usr/bin/env python3
"""Validate Hoax.ai public route readiness gate enforcement."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

POLICY_TOP = {
    "policy_id",
    "name",
    "version",
    "status",
    "maturity",
    "governing_principle",
    "boundary_principle",
    "allowed_readiness_actions",
    "prohibited_readiness_actions",
    "readiness_scope",
    "readiness_outcomes",
    "proposed_route_path_policy",
    "metadata_policy",
    "non_authorization_rules",
    "last_reviewed",
}

CRITERIA_TOP = {
    "criteria_set_id",
    "name",
    "version",
    "status",
    "maturity",
    "criteria",
    "last_reviewed",
}

READINESS_TOP = {
    "readiness_gate_id",
    "name",
    "version",
    "status",
    "maturity",
    "reviewed_internal_draft_pack",
    "readiness_records",
    "last_reviewed",
}

CANDIDATE_REGISTRY_TOP = {
    "registry_id",
    "name",
    "version",
    "status",
    "maturity",
    "route_candidates",
    "last_reviewed",
}

REQUIRED_SOURCE_LOCATIONS = [
    "PUBLIC_ROUTE_READINESS_GATE.md",
    "data/public-route-readiness-policy.json",
    "data/public-route-readiness-criteria.json",
    "data/public-route-readiness-v1.json",
    "data/public-route-candidate-registry.json",
    "validators/validate_public_route_readiness_gate.py",
]

REQUIRED_DRAFT_IDS = ["DRAFT-0001", "DRAFT-0002"]
REQUIRED_READINESS_IDS = ["ROUTE-READINESS-0001", "ROUTE-READINESS-0002"]
REQUIRED_ROUTE_CANDIDATE_IDS = ["PUBLIC-ROUTE-CAND-0001", "PUBLIC-ROUTE-CAND-0002"]
REQUIRED_CANDIDATE_IDS = ["REF-CAND-0001", "REF-CAND-0002"]

PROPOSED_PATHS = {
    "DRAFT-0001": "/reference/evidence-posture/",
    "DRAFT-0002": "/reference/artifact-subject-separation/",
}

PATH_SLUGS = ["evidence-posture", "artifact-subject-separation"]

CRITERION_IDS = [f"ROUTE-READINESS-CRITERION-{i:04d}" for i in range(1, 21)]

PROHIBITED_ACTIONS = [
    "public_page",
    "route",
    "sitemap",
    "public_metadata",
    "public_navigation",
    "publication",
    "deployment",
    "dns",
    "cloudflare",
    "tool",
    "classifier",
    "upload",
    "scoring",
    "forms",
    "analytics",
    "api",
    "monetization",
    "external_factual",
]

NON_AUTHORIZATION_TERMS = [
    "routes",
    "sitemap",
    "public_pages",
    "public_metadata",
    "public_navigation",
    "publishing",
    "deployment",
    "seo_expansion",
    "classifier",
    "tool",
    "upload",
]

PROHIBITED_CHANGES = [
    "public_route",
    "sitemap",
    "public_metadata",
    "public_navigation",
    "publication",
    "deployment",
]

NUMERIC_SCORE_PATTERN = re.compile(
    r"\b(seo_score|quality_score|quality grade|\d+\s*%)\b",
    re.IGNORECASE,
)

PUBLIC_FILES = {"index.html", "styles.css", "robots.txt", "sitemap.xml"}

PUBLISHER_STATUS = "blocked_until_first_controlled_public_reference_pilot"

CONVERSION_STATUS = "eligible_for_controlled_public_reference_pilot_only_after_explicit_sprint"
CONVERSION_NEXT_PHASE = "Sprint 24 — First Controlled Public Reference Pilot v1"


def error(msg: str) -> None:
    print(f"ERROR: {msg}")


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def json_has_numeric_scores(data: object) -> bool:
    text = json.dumps(data).lower()
    if NUMERIC_SCORE_PATTERN.search(text):
        if "no_numeric" in text.replace("-", "_"):
            return False
        return True
    return False


def validate_policy() -> bool:
    ok = True
    path = ROOT / "data" / "public-route-readiness-policy.json"
    try:
        data = load_json(path)
    except (json.JSONDecodeError, OSError) as exc:
        error(f"public-route-readiness-policy.json parse failed: {exc}")
        return False

    if POLICY_TOP - set(data.keys()):
        error(f"public-route-readiness-policy.json missing fields: {sorted(POLICY_TOP - set(data.keys()))}")
        ok = False

    if data.get("status") != "governed_public_route_readiness_policy":
        error("public-route-readiness-policy.json: invalid status")
        ok = False
    if data.get("maturity") != "readiness_gate_only_no_routes_no_sitemap_no_publication":
        error("public-route-readiness-policy.json: invalid maturity")
        ok = False

    if set(data.get("readiness_scope", [])) != set(REQUIRED_DRAFT_IDS):
        error("public-route-readiness-policy.json: readiness_scope must be DRAFT-0001 and DRAFT-0002")
        ok = False

    prohibited = " ".join(data.get("prohibited_readiness_actions", [])).lower()
    for term in PROHIBITED_ACTIONS:
        if term.replace("_", "") not in prohibited.replace("_", ""):
            error(f"public-route-readiness-policy.json: prohibited actions missing {term}")
            ok = False

    path_policy = data.get("proposed_route_path_policy", "").lower()
    if "inactive" not in path_policy or "route registry" not in path_policy.replace("-", " "):
        if "route registry" not in path_policy and "route-registry" not in path_policy:
            error("public-route-readiness-policy.json: proposed_route_path_policy must forbid active route registry")
            ok = False
    if "inactive" not in path_policy:
        error("public-route-readiness-policy.json: proposed_route_path_policy must require inactive paths")
        ok = False

    metadata_policy = data.get("metadata_policy", "").lower()
    if "forbid" not in metadata_policy and "forbids" not in metadata_policy:
        error("public-route-readiness-policy.json: metadata_policy must forbid public metadata")
        ok = False

    non_auth = " ".join(data.get("non_authorization_rules", [])).lower()
    for term in NON_AUTHORIZATION_TERMS:
        if term.replace("_", "") not in non_auth.replace("_", ""):
            error(f"public-route-readiness-policy.json: non_authorization_rules missing {term}")
            ok = False

    if json_has_numeric_scores(data):
        error("public-route-readiness-policy.json: numeric scores prohibited")
        ok = False

    return ok


def validate_criteria() -> bool:
    ok = True
    data = load_json(ROOT / "data" / "public-route-readiness-criteria.json")

    if CRITERIA_TOP - set(data.keys()):
        error(f"public-route-readiness-criteria.json missing fields: {sorted(CRITERIA_TOP - set(data.keys()))}")
        ok = False

    criteria = data.get("criteria", [])
    if len(criteria) != 20:
        error("public-route-readiness-criteria.json: exactly 20 criteria required")
        ok = False

    seen = set()
    for c in criteria:
        cid = c.get("criterion_id", "")
        if cid not in CRITERION_IDS:
            error(f"criteria: invalid criterion_id {cid}")
            ok = False
        seen.add(cid)

    if seen != set(CRITERION_IDS):
        error("public-route-readiness-criteria.json: missing required criterion IDs")
        ok = False

    if json_has_numeric_scores(data):
        error("public-route-readiness-criteria.json: numeric scores prohibited")
        ok = False

    return ok


def validate_readiness_results() -> bool:
    ok = True
    registry = {
        d.get("draft_id"): d
        for d in load_json(ROOT / "data" / "internal-draft-registry.json").get("draft_records", [])
    }
    data = load_json(ROOT / "data" / "public-route-readiness-v1.json")

    if READINESS_TOP - set(data.keys()):
        error(f"public-route-readiness-v1.json missing fields: {sorted(READINESS_TOP - set(data.keys()))}")
        ok = False

    records = data.get("readiness_records", [])
    if len(records) != 2:
        error("public-route-readiness-v1.json: exactly 2 readiness records required")
        ok = False

    seen = set()
    for rec in records:
        rid = rec.get("readiness_record_id", "?")
        did = rec.get("draft_id", "?")
        seen.add(rid)

        if rid not in REQUIRED_READINESS_IDS:
            error(f"readiness: invalid readiness_record_id {rid}")
            ok = False

        if rec.get("readiness_status") != "public_route_readiness_checked":
            error(f"readiness {rid}: readiness_status must be public_route_readiness_checked")
            ok = False

        if rec.get("readiness_outcome") != "route_readiness_passed_with_conditions":
            error(f"readiness {rid}: readiness_outcome must be route_readiness_passed_with_conditions")
            ok = False

        if did not in registry:
            error(f"readiness {rid}: draft {did} not in internal draft registry")
            ok = False
        elif registry[did].get("review_status") != "review_completed_internal":
            error(f"readiness {rid}: draft {did} must be review_completed_internal")
            ok = False

        if rec.get("proposed_route_status") != "inactive_candidate_path":
            error(f"readiness {rid}: proposed_route_status must be inactive_candidate_path")
            ok = False

        expected_path = PROPOSED_PATHS.get(did)
        if rec.get("proposed_route_path") != expected_path:
            error(f"readiness {rid}: proposed_route_path must be {expected_path}")
            ok = False

        result_ids = {r.get("criterion_id") for r in rec.get("criteria_results", [])}
        if result_ids != set(CRITERION_IDS):
            error(f"readiness {rid}: must cover all 20 criteria")
            ok = False

        for field, expected in [
            ("route_status_after_readiness", "not_route_created"),
            ("sitemap_status_after_readiness", "not_sitemap_eligible"),
            ("publication_status_after_readiness", "publication_blocked"),
            ("public_metadata_status_after_readiness", "not_created"),
            ("public_navigation_status_after_readiness", "not_linked"),
            ("deployment_status_after_readiness", "not_deployed"),
        ]:
            if rec.get(field) != expected:
                error(f"readiness {rid}: {field} must be {expected}")
                ok = False

        if rec.get("next_allowed_phase") != "first_controlled_public_reference_pilot":
            error(f"readiness {rid}: next_allowed_phase must be first_controlled_public_reference_pilot")
            ok = False

        stmt = rec.get("non_authorization_statement", "").lower()
        if "does not authorize" not in stmt:
            error(f"readiness {rid}: non_authorization_statement required")
            ok = False
        for term in ["routes", "sitemap", "metadata", "navigation", "publication", "deployment", "classifier", "tool", "upload"]:
            if term not in stmt:
                error(f"readiness {rid}: non_authorization must mention {term}")
                ok = False

    if seen != set(REQUIRED_READINESS_IDS):
        error("public-route-readiness-v1.json: missing required readiness record IDs")
        ok = False

    if json_has_numeric_scores(data):
        error("public-route-readiness-v1.json: numeric scores prohibited")
        ok = False

    return ok


def validate_route_candidate_registry() -> bool:
    ok = True
    readiness = {
        r.get("readiness_record_id"): r
        for r in load_json(ROOT / "data" / "public-route-readiness-v1.json").get("readiness_records", [])
    }
    data = load_json(ROOT / "data" / "public-route-candidate-registry.json")

    if CANDIDATE_REGISTRY_TOP - set(data.keys()):
        error(f"public-route-candidate-registry.json missing fields: {sorted(CANDIDATE_REGISTRY_TOP - set(data.keys()))}")
        ok = False

    candidates = data.get("route_candidates", [])
    if len(candidates) != 2:
        error("public-route-candidate-registry.json: exactly 2 route candidate records required")
        ok = False

    seen = set()
    for cand in candidates:
        cid = cand.get("route_candidate_id", "?")
        rid = cand.get("readiness_record_id", "?")
        seen.add(cid)

        if cid not in REQUIRED_ROUTE_CANDIDATE_IDS:
            error(f"route candidate: invalid route_candidate_id {cid}")
            ok = False

        if rid not in readiness:
            error(f"route candidate {cid}: readiness_record_id {rid} not found")
            ok = False

        for field, expected in [
            ("proposed_route_status", "inactive_candidate_path"),
            ("route_status", "not_route_created"),
            ("sitemap_status", "not_sitemap_eligible"),
            ("publication_status", "publication_blocked"),
            ("public_metadata_status", "not_created"),
            ("public_navigation_status", "not_linked"),
            ("deployment_status", "not_deployed"),
            ("conversion_status", CONVERSION_STATUS),
            ("conversion_allowed_next_phase", CONVERSION_NEXT_PHASE),
        ]:
            if cand.get(field) != expected:
                error(f"route candidate {cid}: {field} must be {expected}")
                ok = False

    if seen != set(REQUIRED_ROUTE_CANDIDATE_IDS):
        error("public-route-candidate-registry.json: missing required route candidate IDs")
        ok = False

    return ok


def validate_registries() -> bool:
    ok = True

    for entry in load_json(ROOT / "data" / "internal-draft-registry.json").get("draft_records", []):
        did = entry.get("draft_id", "?")
        if did not in REQUIRED_DRAFT_IDS:
            continue
        if entry.get("public_route_readiness_status") != "public_route_readiness_checked":
            error(f"draft registry: {did} public_route_readiness_status required")
            ok = False
        if entry.get("public_route_readiness_outcome") != "route_readiness_passed_with_conditions":
            error(f"draft registry: {did} invalid readiness outcome")
            ok = False
        if entry.get("public_route_readiness_ref") != "data/public-route-readiness-v1.json":
            error(f"draft registry: {did} public_route_readiness_ref missing or wrong")
            ok = False
        if entry.get("public_route_candidate_ref") != "data/public-route-candidate-registry.json":
            error(f"draft registry: {did} public_route_candidate_ref missing or wrong")
            ok = False
        if entry.get("proposed_route_status") != "inactive_candidate_path":
            error(f"draft registry: {did} proposed_route_status must be inactive_candidate_path")
            ok = False
        if entry.get("proposed_route_path") != PROPOSED_PATHS.get(did):
            error(f"draft registry: {did} proposed_route_path mismatch")
            ok = False
        for field, expected in [
            ("route_status", "not_route_created"),
            ("sitemap_status", "not_sitemap_eligible"),
            ("publication_status", "publication_blocked"),
        ]:
            if entry.get(field) != expected:
                error(f"draft registry: {did} {field} must remain {expected}")
                ok = False

    for entry in load_json(ROOT / "data" / "reference-page-candidate-registry.json").get("candidates", []):
        cid = entry.get("candidate_id", "?")
        if cid in REQUIRED_CANDIDATE_IDS:
            if entry.get("public_route_readiness_status") != "public_route_readiness_checked":
                error(f"candidate registry: {cid} public_route_readiness_status required")
                ok = False
            if entry.get("public_route_readiness_outcome") != "route_readiness_passed_with_conditions":
                error(f"candidate registry: {cid} invalid readiness outcome")
                ok = False
            for field, expected in [
                ("route_status", "not_route_created"),
                ("sitemap_status", "not_sitemap_eligible"),
                ("publication_status", "publication_blocked"),
                ("proposed_route_status", "inactive_candidate_path"),
            ]:
                if entry.get(field) != expected:
                    error(f"candidate registry: {cid} {field} must be {expected}")
                    ok = False
        else:
            if entry.get("public_route_readiness_status") == "public_route_readiness_checked":
                error(f"candidate registry: {cid} must not have public_route_readiness_checked")
                ok = False
            if entry.get("route_status") != "not_route_created":
                error(f"candidate registry: {cid} must not be route-ready")
                ok = False

    return ok


def validate_proposed_path_safety() -> bool:
    ok = True

    for path_str in PROPOSED_PATHS.values():
        rel = path_str.strip("/").replace("/", "\\")
        dir_path = ROOT / rel
        if dir_path.exists():
            error(f"proposed path safety: directory exists for {path_str}")
            ok = False

        file_variants = [
            ROOT / f"{rel}.html",
            ROOT / f"{rel}index.html",
            ROOT / rel / "index.html",
        ]
        for fp in file_variants:
            if fp.exists():
                error(f"proposed path safety: file exists {fp.relative_to(ROOT).as_posix()}")
                ok = False

    routes = load_json(ROOT / "data" / "route-registry.json").get("routes", [])
    route_paths = {r.get("path", "").lower() for r in routes}
    for path_str in PROPOSED_PATHS.values():
        normalized = path_str.lower().rstrip("/") + "/"
        alt = path_str.lower().rstrip("/")
        if normalized in route_paths or alt in route_paths or path_str.lower() in route_paths:
            error(f"proposed path {path_str} must not be in route-registry")
            ok = False

    sitemap_text = (ROOT / "sitemap.xml").read_text(encoding="utf-8").lower()
    for slug in PATH_SLUGS:
        if slug in sitemap_text:
            error(f"sitemap.xml: must not contain {slug}")
            ok = False

    index_html = (ROOT / "index.html").read_text(encoding="utf-8").lower()
    for slug in PATH_SLUGS:
        if slug in index_html:
            error(f"index.html: must not link to {slug}")
            ok = False

    if (ROOT / ".nojekyll").exists():
        error(".nojekyll must not be created in this sprint")
        ok = False

    for html in ROOT.glob("**/*.html"):
        rel = html.relative_to(ROOT).as_posix()
        if rel not in PUBLIC_FILES:
            error(f"public safety: unexpected HTML file {rel}")
            ok = False

    if [r.get("route_id") for r in routes] != ["ROUTE-0001"]:
        error("route-registry: unexpected routes added")
        ok = False

    try:
        tree = ET.parse(ROOT / "sitemap.xml")
        urls = tree.getroot().findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        if len(urls) != 1:
            error("sitemap.xml: expansion detected")
            ok = False
    except ET.ParseError as exc:
        error(f"sitemap.xml parse failed: {exc}")
        ok = False

    return ok


def validate_publisher_and_gates() -> bool:
    ok = True
    pub = load_json(ROOT / "data" / "publisher-governance-policy.json")
    if pub.get("current_publisher_status") != PUBLISHER_STATUS:
        error(f"publisher-governance-policy: current_publisher_status must be {PUBLISHER_STATUS}")
        ok = False

    gates = load_json(ROOT / "data" / "publisher-quality-gates.json").get("gates", [])
    gate = next((g for g in gates if g.get("gate_id") == "PUB-GATE-0023"), None)
    if not gate:
        error("publisher-quality-gates: PUB-GATE-0023 missing")
        ok = False
    elif gate.get("required_before_public_release") is not True or gate.get("bypassable") is True:
        error("publisher-quality-gates: PUB-GATE-0023 must be required and not bypassable")
        ok = False
    else:
        notes = gate.get("notes", "").lower()
        if "does not authorize" not in notes:
            error("publisher-quality-gates: PUB-GATE-0023 must not authorize outputs by itself")
            ok = False

    expansion = load_json(ROOT / "data" / "reference-expansion-gate.json")
    checks = " ".join(expansion.get("required_pre_release_checks", [])).lower()
    if "public_route_readiness" not in checks:
        error("reference-expansion-gate.json: must include public route readiness pre-release check")
        ok = False

    return ok


def validate_cross_file() -> bool:
    ok = True
    locations = {s.get("location") for s in load_json(ROOT / "data" / "source-registry.json").get("sources", [])}
    for loc in REQUIRED_SOURCE_LOCATIONS:
        if loc not in locations:
            error(f"source-registry.json: missing source for {loc}")
            ok = False

    content = (ROOT / "validators" / "validate_all.py").read_text(encoding="utf-8")
    if "validate_public_route_readiness_gate.py" not in content:
        error("validate_all.py: must include validate_public_route_readiness_gate.py")
        ok = False

    return ok


def main() -> int:
    parse_paths = [
        "data/public-route-readiness-policy.json",
        "data/public-route-readiness-criteria.json",
        "data/public-route-readiness-v1.json",
        "data/public-route-candidate-registry.json",
        "data/internal-draft-registry.json",
        "data/internal-draft-pack-v1.json",
        "data/reference-page-candidate-registry.json",
        "data/publisher-governance-policy.json",
        "data/publisher-quality-gates.json",
        "data/reference-expansion-gate.json",
        "data/route-registry.json",
    ]
    for rel in parse_paths:
        try:
            load_json(ROOT / rel)
        except (json.JSONDecodeError, OSError) as exc:
            error(f"{rel} parse failed: {exc}")
            return 1

    try:
        ET.parse(ROOT / "sitemap.xml")
    except ET.ParseError as exc:
        error(f"sitemap.xml parse failed: {exc}")
        return 1

    if not (ROOT / "index.html").exists():
        error("index.html missing")
        return 1

    checks = [
        validate_policy,
        validate_criteria,
        validate_readiness_results,
        validate_route_candidate_registry,
        validate_registries,
        validate_proposed_path_safety,
        validate_publisher_and_gates,
        validate_cross_file,
    ]
    if not all(fn() for fn in checks):
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
