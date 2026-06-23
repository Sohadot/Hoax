#!/usr/bin/env python3
"""Validate Hoax.ai interface embodiment governance."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

COMPONENT_REQUIRED = {
    "component_id",
    "name",
    "component_type",
    "status",
    "public_status",
    "purpose",
    "thesis_function",
    "governance_boundary",
    "allowed_use",
    "prohibited_use",
    "dependencies",
    "notes",
}

GRAMMAR_TOP_REQUIRED = {
    "interface_grammar_id",
    "name",
    "version",
    "status",
    "maturity",
    "governing_principle",
    "allowed_visual_metaphors",
    "prohibited_visual_metaphors",
    "allowed_interface_promises",
    "prohibited_interface_promises",
    "accessibility_rules",
    "performance_rules",
    "motion_rules",
    "dependency_rules",
    "last_reviewed",
}

SURFACE_MAP_REQUIRED = {
    "surface_map_id",
    "name",
    "version",
    "status",
    "route_id",
    "path",
    "mapped_components",
    "prohibited_patterns_checked",
    "public_surface_status",
    "external_deployment_status",
    "last_reviewed",
}

REQUIRED_PROHIBITED_METAPHORS = [
    "scanner",
    "fake/real switch",
    "truth meter",
    "lie detector",
    "red threat dashboard",
    "upload-to-detect",
    "subject risk profile",
    "guilt meter",
    "authenticity score gauge",
]

REQUIRED_PROHIBITED_PROMISES = [
    "detection",
    "guarantee",
    "truth verdict",
    "fake/real result",
    "upload to check",
    "score",
    "public classifier",
    "deepfake detected",
]

COMPONENT_PROHIBITED_TERMS = [
    "scan now",
    "upload to",
    "upload workflow",
    "detect fake",
    "truth score",
    "lie score",
    "fake/real result",
    "truth verdict",
    "public classifier",
    "active classifier",
    "subject accusation",
    "guaranteed detection",
    "deepfake detected",
    "score meter",
    "guilt meter",
]

INDEX_FORBIDDEN = [
    "submit",
    "<form",
    "truth score",
    "lie score",
    "first in the world",
    "scan your",
    "scan now",
    "deepfake detector",
    "try our detector",
    "active classifier",
    "live tool",
    "upload to check",
    "detect fake",
    "score meter",
    "guilt meter",
]

INDEX_CONDITIONAL = ["upload", "detect", "check", "verdict", "fake", "real", "scan", "analyze", "classifier"]

CSS_PROHIBITED_CLASS_PATTERNS = [
    "scanner",
    "detector",
    "truth-meter",
    "lie-detector",
    "upload",
    "score-meter",
    "threat-dashboard",
    "guilt",
    "surveillance",
]

NEGATION_MARKERS = [
    "does not",
    "do not",
    "not ",
    "no ",
    "not a ",
    "not an ",
    "not the ",
    "not issue",
    "not claim",
    "not produce",
    "no absolute",
    "never ",
    "without ",
    "planned",
    "under development",
    "prohibited",
    "must not",
    "not absolute",
    "not through",
    "no final",
    ", or not",
    "— not",
    "– not",
]

IFC_PATTERN = re.compile(r"^IFC-\d{4}$")


def error(msg: str) -> None:
    print(f"ERROR: {msg}")


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def contains_unnegated_term(text: str, term: str) -> bool:
    lower = text.lower()
    if term not in lower:
        return False
    idx = 0
    while True:
        pos = lower.find(term, idx)
        if pos == -1:
            return False
        if pos > 0 and lower[pos - 1] == "-":
            idx = pos + len(term)
            continue
        if term == "real" and "fake/real" in lower and "no fake/real" in lower:
            idx = pos + len(term)
            continue
        prefix = lower[max(0, pos - 100) : pos]
        if any(marker in prefix for marker in NEGATION_MARKERS):
            idx = pos + len(term)
            continue
        return True
    return False


def line_has_unnegated_term(line: str, term: str) -> bool:
    lower = line.lower()
    if term not in lower:
        return False
    if any(neg in lower for neg in NEGATION_MARKERS):
        return False
    return contains_unnegated_term(line, term)


def validate_interface_grammar() -> bool:
    ok = True
    data = load_json(ROOT / "data" / "interface-grammar.json")
    missing = GRAMMAR_TOP_REQUIRED - set(data.keys())
    if missing:
        error(f"interface-grammar: missing top-level fields {sorted(missing)}")
        ok = False

    if data.get("status") != "governed_internal_interface_standard":
        error("interface-grammar: status must be governed_internal_interface_standard")
        ok = False
    if data.get("maturity") != "not_public_tool":
        error("interface-grammar: maturity must be not_public_tool")
        ok = False

    metaphors = " ".join(data.get("prohibited_visual_metaphors", [])).lower()
    for term in REQUIRED_PROHIBITED_METAPHORS:
        if term not in metaphors:
            error(f"interface-grammar: prohibited_visual_metaphors missing '{term}'")
            ok = False

    promises = " ".join(data.get("prohibited_interface_promises", [])).lower()
    for term in REQUIRED_PROHIBITED_PROMISES:
        if term not in promises:
            error(f"interface-grammar: prohibited_interface_promises missing '{term}'")
            ok = False

    accessibility = " ".join(data.get("accessibility_rules", [])).lower()
    for req in ["semantic html", "mobile", "javascript"]:
        if req not in accessibility:
            error(f"interface-grammar: accessibility_rules missing '{req}' reference")
            ok = False

    dependencies = " ".join(data.get("dependency_rules", [])).lower()
    if "external" not in dependencies or ("library" not in dependencies and "libraries" not in dependencies):
        error("interface-grammar: dependency_rules must forbid external libraries without approval")
        ok = False

    return ok


def validate_component_registry() -> bool:
    ok = True
    data = load_json(ROOT / "data" / "interface-component-registry.json")
    components = data.get("components", [])
    if not components:
        error("interface-component-registry: components missing")
        return False

    seen: set[str] = set()
    for component in components:
        cid = component.get("component_id", "")
        if not IFC_PATTERN.match(cid):
            error(f"interface-component-registry: invalid component_id '{cid}'")
            ok = False
        if cid in seen:
            error(f"interface-component-registry: duplicate component_id '{cid}'")
            ok = False
        seen.add(cid)

        missing = COMPONENT_REQUIRED - set(component.keys())
        if missing:
            error(f"interface-component-registry '{cid}': missing fields {sorted(missing)}")
            ok = False

        public_status = component.get("public_status", "")
        if public_status not in {
            "active_thesis_surface",
            "internal_only",
            "planned_not_claimed",
            "blocked",
        }:
            error(f"interface-component-registry '{cid}': invalid public_status '{public_status}'")
            ok = False

        tool_terms = ["scan now", "upload to check", "now available", "operational service"]
        for field in ("allowed_use", "thesis_function"):
            text = component.get(field, "").lower()
            for term in COMPONENT_PROHIBITED_TERMS:
                if contains_unnegated_term(text, term):
                    error(
                        f"interface-component-registry '{cid}': "
                        f"prohibited term '{term}' in {field}"
                    )
                    ok = False
            for term in tool_terms:
                if contains_unnegated_term(text, term):
                    error(
                        f"interface-component-registry '{cid}': "
                        f"implies active tool via '{term}' in {field}"
                    )
                    ok = False

    required_ids = {f"IFC-{i:04d}" for i in range(1, 11)}
    if seen != required_ids:
        missing_ids = required_ids - seen
        extra_ids = seen - required_ids
        if missing_ids:
            error(f"interface-component-registry: missing required components {sorted(missing_ids)}")
            ok = False
        if extra_ids:
            error(f"interface-component-registry: unexpected component ids {sorted(extra_ids)}")
            ok = False

    return ok


def validate_surface_map() -> bool:
    ok = True
    data = load_json(ROOT / "data" / "interface-surface-map.json")
    missing = SURFACE_MAP_REQUIRED - set(data.keys())
    if missing:
        error(f"interface-surface-map: missing top-level fields {sorted(missing)}")
        ok = False

    if data.get("route_id") != "ROUTE-0001":
        error("interface-surface-map: route_id must be ROUTE-0001")
        ok = False
    if data.get("path") != "/":
        error("interface-surface-map: path must be /")
        ok = False
    if data.get("external_deployment_status") != "external_deployment_deferred":
        error("interface-surface-map: external_deployment_status must be external_deployment_deferred")
        ok = False

    registry = load_json(ROOT / "data" / "interface-component-registry.json")
    component_ids = {c["component_id"] for c in registry.get("components", [])}
    for cid in data.get("mapped_components", []):
        if cid not in component_ids:
            error(f"interface-surface-map: mapped component '{cid}' not in registry")
            ok = False

    if "IFC-0010" in data.get("mapped_components", []):
        error("interface-surface-map: IFC-0010 must not be public-mapped")
        ok = False

    routes = load_json(ROOT / "data" / "route-registry.json").get("routes", [])
    route = next((r for r in routes if r.get("route_id") == data.get("route_id")), None)
    if route is None:
        error("interface-surface-map: route_id not found in route-registry")
        ok = False
    elif route.get("path") != data.get("path"):
        error("interface-surface-map: path does not match route-registry path")
        ok = False

    required_patterns = {
        "scanner",
        "upload",
        "fake/real",
        "truth score",
        "lie score",
        "red threat dashboard",
        "detection guarantee",
        "public classifier",
        "subject accusation",
        "score meter",
    }
    checked = set(data.get("prohibited_patterns_checked", []))
    if not required_patterns.issubset(checked):
        error("interface-surface-map: prohibited_patterns_checked incomplete")
        ok = False

    return ok


def validate_index_html() -> bool:
    ok = True
    index_path = ROOT / "index.html"
    if not index_path.exists():
        error("interface governance: index.html missing")
        return False

    content = index_path.read_text(encoding="utf-8")
    lower = content.lower()

    h1_count = len(re.findall(r"<h1\b", content, re.IGNORECASE))
    if h1_count != 1:
        error(f"interface governance: expected exactly one H1, found {h1_count}")
        ok = False

    for phrase in INDEX_FORBIDDEN:
        if phrase in lower:
            error(f"interface governance: forbidden phrase '{phrase}' in index.html")
            ok = False

    for line in content.splitlines():
        line_lower = line.lower()
        for term in INDEX_CONDITIONAL:
            if term == "check" and "checklist" in line_lower:
                continue
            if term in line_lower and line_has_unnegated_term(line, term):
                if term == "classifier" and "classification" in line_lower:
                    continue
                error(
                    f"interface governance: '{term}' in index.html may imply "
                    "active tool without clear negation"
                )
                ok = False

    artifact_markers = [
        "evidence artifact",
        "artifact–subject",
        "artifact-subject",
        "not on connected subjects",
        "connected to it",
    ]
    if not any(marker in lower for marker in artifact_markers):
        error("interface governance: artifact-subject separation language not visible")
        ok = False

    return ok


def validate_styles_css() -> bool:
    ok = True
    css_path = ROOT / "styles.css"
    if not css_path.exists():
        error("interface governance: styles.css missing")
        return False

    content = css_path.read_text(encoding="utf-8").lower()
    class_matches = re.findall(r"\.([a-z0-9_-]+)", content)
    for class_name in class_matches:
        for pattern in CSS_PROHIBITED_CLASS_PATTERNS:
            if pattern in class_name:
                error(
                    f"interface governance: prohibited class pattern '{pattern}' "
                    f"in styles.css ('{class_name}')"
                )
                ok = False
    return ok


def validate_source_registry_entries() -> bool:
    ok = True
    registry = load_json(ROOT / "data" / "source-registry.json")
    locations = {s.get("location") for s in registry.get("sources", [])}
    for required in [
        "INTERFACE_EMBODIMENT_GOVERNANCE.md",
        "data/interface-grammar.json",
        "data/interface-component-registry.json",
        "data/interface-surface-map.json",
        "validators/validate_interface_governance.py",
    ]:
        if required not in locations:
            error(f"source-registry: missing interface governance source '{required}'")
            ok = False
    return ok


def main() -> int:
    checks = [
        ("Interface grammar", validate_interface_grammar),
        ("Interface component registry", validate_component_registry),
        ("Interface surface map", validate_surface_map),
        ("Index HTML interface boundaries", validate_index_html),
        ("Styles CSS interface boundaries", validate_styles_css),
        ("Interface source registry", validate_source_registry_entries),
    ]

    all_ok = True
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
