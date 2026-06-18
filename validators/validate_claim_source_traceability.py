#!/usr/bin/env python3
"""Validate Hoax.ai claim and source traceability."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

LEDGER_REQUIRED = {
    "claim_id",
    "claim_text",
    "claim_type",
    "evidence_posture",
    "support_location",
    "source_type",
    "status",
    "last_reviewed",
    "notes",
}

CLAIM_TYPES = {
    "conceptual_thesis",
    "operational_claim",
    "governance_claim",
    "external_factual_claim",
    "future_capability_claim",
}

EVIDENCE_POSTURES = {
    "conceptual",
    "repository_supported",
    "source_supported",
    "planned_not_claimed",
    "needs_review",
    "retired",
}

LINK_REQUIRED = {
    "claim_id",
    "claim_type",
    "evidence_posture",
    "support_locations",
    "source_refs",
    "support_scope",
    "traceability_status",
    "public_surface_refs",
    "notes",
}

PUBLIC_CLAIM_REQUIRED = {
    "public_claim_id",
    "claim_id",
    "statement_snippet",
    "public_location",
    "claim_role",
    "allowed_public_use",
    "prohibited_interpretation",
    "notes",
}

PROHIBITED_PUBLIC_PATTERNS = [
    "first in the world",
    "only system",
    "guaranteed authority",
    "detects all",
    "certifies truth",
    "public classifier",
    "scan now",
    "upload to check",
    "truth score",
    "lie score",
    "deepfake detected",
    "hoax confirmed",
]

NEGATION_MARKERS = [
    "does not",
    "do not",
    "not ",
    "no ",
    "never ",
    "without ",
    "not a ",
    "not an ",
    "not claim",
    "not issue",
    "planned",
    "under development",
]

CLAIM_PATTERN = re.compile(r"^CLAIM-\d{4}$")
SOURCE_PATTERN = re.compile(r"^SOURCE-\d{4}$")
FILE_PATH_PATTERN = re.compile(r"^[A-Za-z0-9_./-]+\.(md|json|html|css|xml|txt|py)$")


def error(msg: str) -> None:
    print(f"ERROR: {msg}")


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u2014", "—").replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", text.strip().lower())


def contains_unnegated(text: str, phrase: str) -> bool:
    lower = text.lower()
    idx = 0
    while True:
        pos = lower.find(phrase, idx)
        if pos == -1:
            return False
        prefix = lower[max(0, pos - 40) : pos]
        if any(marker in prefix for marker in NEGATION_MARKERS):
            idx = pos + len(phrase)
            continue
        return True
    return False


def resolve_support_path(location: str) -> Path | None:
    loc = location.strip()
    if SOURCE_PATTERN.match(loc):
        return None
    if FILE_PATH_PATTERN.match(loc) or loc in {"index.html", "styles.css", "robots.txt", "sitemap.xml"}:
        return ROOT / loc
    return None


def validate_policy() -> bool:
    ok = True
    data = load_json(ROOT / "data" / "claim-source-traceability-policy.json")
    required = {
        "policy_id",
        "name",
        "version",
        "status",
        "maturity",
        "governing_principle",
        "claim_categories",
        "source_support_scope_rules",
        "support_location_rules",
        "public_claim_mapping_rules",
        "prohibited_claim_patterns",
        "validation_requirements",
        "last_reviewed",
    }
    missing = required - set(data.keys())
    if missing:
        error(f"claim-source-traceability-policy: missing fields {sorted(missing)}")
        ok = False
    if data.get("status") != "governed_internal_claim_source_traceability_policy":
        error("claim-source-traceability-policy: invalid status")
        ok = False
    if data.get("maturity") != "pre_reference_expansion_hardening":
        error("claim-source-traceability-policy: invalid maturity")
        ok = False

    categories = data.get("claim_categories", {})
    for cat in [
        "conceptual_thesis",
        "operational_claim",
        "governance_claim",
        "repository_supported_claim",
        "external_factual_claim",
        "future_capability_claim",
    ]:
        if cat not in categories:
            error(f"claim-source-traceability-policy: missing category '{cat}'")
            ok = False

    prohibited = " ".join(data.get("prohibited_claim_patterns", [])).lower()
    for term in [
        "first in the world",
        "certifies truth",
        "detects all",
        "subject accusation",
        "overbroad source support",
    ]:
        if term not in prohibited:
            error(f"claim-source-traceability-policy: missing prohibited pattern '{term}'")
            ok = False
    return ok


def validate_evidence_ledger(sources: dict[str, dict]) -> tuple[bool, dict[str, dict]]:
    ok = True
    data = load_json(ROOT / "data" / "evidence-ledger.json")
    claims = data.get("claims", [])
    by_id: dict[str, dict] = {}

    seen: set[str] = set()
    for claim in claims:
        cid = claim.get("claim_id", "")
        if not CLAIM_PATTERN.match(cid):
            error(f"evidence-ledger: invalid claim_id '{cid}'")
            ok = False
        if cid in seen:
            error(f"evidence-ledger: duplicate claim_id '{cid}'")
            ok = False
        seen.add(cid)
        by_id[cid] = claim

        missing = LEDGER_REQUIRED - set(claim.keys())
        if missing:
            error(f"evidence-ledger '{cid}': missing fields {sorted(missing)}")
            ok = False

        ctype = claim.get("claim_type")
        posture = claim.get("evidence_posture")
        if ctype not in CLAIM_TYPES:
            error(f"evidence-ledger '{cid}': invalid claim_type '{ctype}'")
            ok = False
        if posture not in EVIDENCE_POSTURES:
            error(f"evidence-ledger '{cid}': invalid evidence_posture '{posture}'")
            ok = False

        support = str(claim.get("support_location", "")).strip()
        if posture in {"repository_supported", "source_supported"} and not support:
            error(f"evidence-ledger '{cid}': missing support_location")
            ok = False

        if ctype == "future_capability_claim" and posture not in {
            "planned_not_claimed",
            "conceptual",
            "retired",
        }:
            error(f"evidence-ledger '{cid}': future capability marked as existing")
            ok = False

        if ctype == "external_factual_claim":
            if posture == "source_supported":
                error(
                    f"evidence-ledger '{cid}': external factual claim requires registered external source"
                )
                ok = False
            has_external = any(
                sources.get(sid, {}).get("source_type", "").startswith("external")
                for sid in sources
            )
            if posture == "source_supported" and not has_external:
                error(f"evidence-ledger '{cid}': no registered external source for external claim")
                ok = False

    return ok, by_id


def validate_source_registry() -> tuple[bool, dict[str, dict]]:
    ok = True
    data = load_json(ROOT / "data" / "source-registry.json")
    sources = data.get("sources", [])
    by_id: dict[str, dict] = {}

    seen: set[str] = set()
    for source in sources:
        sid = source.get("source_id", "")
        if not SOURCE_PATTERN.match(sid):
            error(f"source-registry: invalid source_id '{sid}'")
            ok = False
        if sid in seen:
            error(f"source-registry: duplicate source_id '{sid}'")
            ok = False
        seen.add(sid)
        by_id[sid] = source

        if not source.get("supports"):
            error(f"source-registry '{sid}': missing supports field")
            ok = False

        stype = source.get("source_type", "")
        location = source.get("location", "")
        if stype.startswith("internal") and location:
            if not (ROOT / location).exists():
                error(f"source-registry '{sid}': internal file missing '{location}'")
                ok = False

        if stype.startswith("internal") and "external_factual_claim" in source.get("supports", []):
            if "external_factual_claim" in source.get("supports", []) and stype.startswith(
                "internal"
            ):
                supports = source.get("supports", [])
                if "external_factual_claim" in supports and stype != "external_web":
                    error(
                        f"source-registry '{sid}': internal source must not support broad external factual claims"
                    )
                    ok = False

    return ok, by_id


def validate_claim_source_map(ledger: dict[str, dict], sources: dict[str, dict]) -> bool:
    ok = True
    data = load_json(ROOT / "data" / "claim-source-map.json")
    links = data.get("claim_source_links", [])
    mapped_ids: set[str] = set()
    public_ids: set[str] = set()

    pub_map = load_json(ROOT / "data" / "public-claim-map.json")
    valid_public_ids = {p["public_claim_id"] for p in pub_map.get("mapped_public_claims", [])}

    for link in links:
        cid = link.get("claim_id", "?")
        missing = LINK_REQUIRED - set(link.keys())
        if missing:
            error(f"claim-source-map '{cid}': missing fields {sorted(missing)}")
            ok = False

        mapped_ids.add(cid)
        ledger_claim = ledger.get(cid)
        if ledger_claim is None:
            error(f"claim-source-map '{cid}': claim not in evidence-ledger")
            ok = False
            continue

        if link.get("claim_type") != ledger_claim.get("claim_type"):
            error(f"claim-source-map '{cid}': claim_type mismatch with ledger")
            ok = False
        if link.get("evidence_posture") != ledger_claim.get("evidence_posture"):
            error(f"claim-source-map '{cid}': evidence_posture mismatch with ledger")
            ok = False

        if link.get("traceability_status") == "unsupported":
            error(f"claim-source-map '{cid}': traceability_status unsupported")
            ok = False

        if ledger_claim.get("claim_type") == "future_capability_claim":
            if ledger_claim.get("evidence_posture") not in {"planned_not_claimed", "conceptual"}:
                error(f"claim-source-map '{cid}': future capability not bounded")
                ok = False

        for sid in link.get("source_refs", []):
            if sid not in sources:
                error(f"claim-source-map '{cid}': invalid source_ref '{sid}'")
                ok = False

        for loc in link.get("support_locations", []):
            path = resolve_support_path(loc)
            if path is not None and not path.exists():
                error(f"claim-source-map '{cid}': support_location missing '{loc}'")
                ok = False

        for pref in link.get("public_surface_refs", []):
            public_ids.add(pref)
            if pref not in valid_public_ids:
                error(f"claim-source-map '{cid}': public_surface_ref '{pref}' not in public-claim-map")
                ok = False

    for cid in ledger:
        if cid not in mapped_ids:
            error(f"claim-source-map: ledger claim '{cid}' not mapped")
            ok = False

    return ok


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def snippet_in_html(snippet: str, html: str) -> bool:
    plain = strip_html(html)
    norm_html = normalize_text(plain)
    norm_snippet = normalize_text(snippet)
    if norm_snippet in norm_html:
        return True
    # Allow near-match if first 40 chars match
    if len(norm_snippet) > 40 and norm_snippet[:40] in norm_html:
        return True
    return False


def validate_public_claim_map(ledger: dict[str, dict]) -> bool:
    ok = True
    data = load_json(ROOT / "data" / "public-claim-map.json")
    routes = load_json(ROOT / "data" / "route-registry.json").get("routes", [])

    if data.get("route_id") != "ROUTE-0001":
        error("public-claim-map: route_id must be ROUTE-0001")
        ok = False
    if data.get("path") != "/":
        error("public-claim-map: path must be /")
        ok = False

    source_file = data.get("source_file", "")
    if not (ROOT / source_file).exists():
        error(f"public-claim-map: source_file missing '{source_file}'")
        ok = False

    route = next((r for r in routes if r.get("route_id") == data.get("route_id")), None)
    if route is None:
        error("public-claim-map: route_id not in route-registry")
        ok = False

    html = (ROOT / source_file).read_text(encoding="utf-8")
    html_lower = html.lower()

    for entry in data.get("mapped_public_claims", []):
        pid = entry.get("public_claim_id", "?")
        missing = PUBLIC_CLAIM_REQUIRED - set(entry.keys())
        if missing:
            error(f"public-claim-map '{pid}': missing fields {sorted(missing)}")
            ok = False

        cid = entry.get("claim_id")
        claim = ledger.get(cid or "")
        if claim is None:
            error(f"public-claim-map '{pid}': claim_id '{cid}' not in ledger")
            ok = False
            continue

        if claim.get("evidence_posture") in {"needs_review", "retired"}:
            error(f"public-claim-map '{pid}': maps to unsupported ledger posture")
            ok = False

        if not entry.get("allowed_public_use"):
            error(f"public-claim-map '{pid}': allowed_public_use must be true for mapped claims")
            ok = False

        snippet = entry.get("statement_snippet", "")
        if not snippet_in_html(snippet, html):
            error(f"public-claim-map '{pid}': statement_snippet not found in index.html")
            ok = False

        prohibited = entry.get("prohibited_interpretation", "").lower()
        for term in ["active classifier", "upload", "truth score", "deployment completion"]:
            if term in prohibited:
                pass

    for phrase in PROHIBITED_PUBLIC_PATTERNS:
        if contains_unnegated(html_lower, phrase):
            error(f"public surface: prohibited claim pattern '{phrase}' in index.html")
            ok = False

    accusation_markers = ["deceptive person", "guilty institution", "person is lying"]
    for marker in accusation_markers:
        if marker in html_lower:
            error(f"public surface: subject accusation pattern '{marker}' in index.html")
            ok = False

    return ok


def validate_source_registry_entries() -> bool:
    ok = True
    registry = load_json(ROOT / "data" / "source-registry.json")
    locations = {s.get("location") for s in registry.get("sources", [])}
    for required in [
        "CLAIM_SOURCE_TRACEABILITY_POLICY.md",
        "data/claim-source-traceability-policy.json",
        "data/claim-source-map.json",
        "data/public-claim-map.json",
        "validators/validate_claim_source_traceability.py",
    ]:
        if required not in locations:
            error(f"source-registry: missing traceability source '{required}'")
            ok = False
    return ok


def main() -> int:
    source_ok, sources = validate_source_registry()
    ledger_ok, ledger = validate_evidence_ledger(sources)

    checks = [
        ("Claim source traceability policy", validate_policy),
        ("Claim source map", lambda: validate_claim_source_map(ledger, sources)),
        ("Public claim map", lambda: validate_public_claim_map(ledger)),
        ("Traceability source registry", validate_source_registry_entries),
    ]

    all_ok = source_ok and ledger_ok
    for name, fn in checks:
        if not fn():
            all_ok = False

    if all_ok:
        print("PASS")
        return 0

    print("FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
