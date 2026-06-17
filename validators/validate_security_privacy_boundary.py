#!/usr/bin/env python3
"""Validate Hoax.ai security and privacy boundary enforcement."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BOUNDARY_TOP_REQUIRED = {
    "boundary_id",
    "name",
    "version",
    "status",
    "maturity",
    "governing_principle",
    "current_posture",
    "prohibited_behaviors",
    "future_interaction_gate",
    "upload_gate",
    "analytics_gate",
    "external_dependency_gate",
    "approved_storage",
    "approved_data_collection",
    "prohibited_security_claims",
    "last_reviewed",
}

PERMISSION_REQUIRED = {
    "permission_id",
    "name",
    "status",
    "allowed_currently",
    "required_future_gate",
    "prohibited_until_approved",
    "notes",
}

REQUIRED_BLOCKED_PERMISSIONS = {
    "PERMISSION-0002": "user_file_upload",
    "PERMISSION-0003": "evidence_submission_form",
    "PERMISSION-0004": "contact_form",
    "PERMISSION-0005": "newsletter_capture",
    "PERMISSION-0006": "analytics_tracking",
    "PERMISSION-0007": "public_classifier_interaction",
    "PERMISSION-0008": "api_access",
    "PERMISSION-0009": "payment_collection",
    "PERMISSION-0010": "third_party_embed",
}

REQUIRED_PROHIBITED_BEHAVIORS = [
    "forms",
    "uploads",
    "analytics",
    "cookies",
    "tracking_pixels",
    "external_script",
    "api_calls",
    "user_accounts",
    "payment_widgets",
    "third_party_embeds",
]

PROHIBITED_APPROVED_STORAGE = {
    "cookies",
    "localstorage",
    "sessionstorage",
    "database",
    "server_logs",
    "uploads",
    "user_accounts",
    "analytics",
}

BLOCKED_DEPENDENCY_TYPES = [
    "external javascript",
    "analytics scripts",
    "tracking pixels",
    "third-party embeds",
    "cdn ui libraries",
    "remote fonts",
    "payment widgets",
    "social widgets",
    "external api clients",
]

INDEX_FORBIDDEN_PATTERNS = [
    ("<form", "form element"),
    ("<input", "input element"),
    ('type="file"', "file upload input"),
    ("<iframe", "iframe embed"),
    ("<script", "script element"),
    ("google-analytics", "analytics reference"),
    ("googletagmanager", "analytics reference"),
    ("gtag(", "analytics reference"),
    ("plausible.io", "analytics reference"),
    ("matomo", "analytics reference"),
    ("hotjar", "analytics reference"),
    ("mixpanel", "analytics reference"),
    ("segment.io", "analytics reference"),
    ("tracking pixel", "tracking pixel"),
    ("newsletter", "newsletter capture"),
    ("subscribe", "newsletter capture"),
    ("contact form", "contact form"),
    ("mailto:", "contact form interaction"),
    ("stripe.com", "payment widget"),
    ("paypal.com", "payment widget"),
    ("fetch(", "fetch API call"),
    ("xmlhttprequest", "XHR API call"),
    ("localstorage", "localStorage usage"),
    ("sessionstorage", "sessionStorage usage"),
    ("document.cookie", "cookie setting"),
]

INDEX_NEGATION_MARKERS = [
    "no ",
    "not ",
    "without ",
    "does not",
    "do not",
    "never ",
    "blocked",
    "prohibited",
]

CSS_PROHIBITED_CLASS_PATTERNS = [
    "upload",
    "scanner",
    "detector",
    "score",
    "payment",
    "tracking",
    "login",
    "account",
]

PERMISSION_PATTERN = re.compile(r"^PERMISSION-\d{4}$")


def error(msg: str) -> None:
    print(f"ERROR: {msg}")


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def contains_unnegated(lower: str, pattern: str) -> bool:
    if pattern not in lower:
        return False
    idx = 0
    while True:
        pos = lower.find(pattern, idx)
        if pos == -1:
            return False
        prefix = lower[max(0, pos - 40) : pos]
        if any(marker in prefix for marker in INDEX_NEGATION_MARKERS):
            idx = pos + len(pattern)
            continue
        return True
    return False


def validate_security_boundary_data() -> bool:
    ok = True
    data = load_json(ROOT / "data" / "security-privacy-boundary.json")
    missing = BOUNDARY_TOP_REQUIRED - set(data.keys())
    if missing:
        error(f"security-privacy-boundary: missing fields {sorted(missing)}")
        ok = False

    if data.get("status") != "governed_internal_security_privacy_boundary":
        error("security-privacy-boundary: invalid status")
        ok = False
    if data.get("maturity") != "zero_data_static_foundation":
        error("security-privacy-boundary: maturity must be zero_data_static_foundation")
        ok = False

    posture = [p.lower() for p in data.get("current_posture", [])]
    if "zero_data" not in posture:
        error("security-privacy-boundary: current_posture missing zero_data")
        ok = False
    if "static_first" not in posture:
        error("security-privacy-boundary: current_posture missing static_first")
        ok = False

    collection = [c.lower() for c in data.get("approved_data_collection", [])]
    if collection != ["none"]:
        error("security-privacy-boundary: approved_data_collection must be none")
        ok = False

    storage_text = " ".join(str(s) for s in data.get("approved_storage", [])).lower()
    if storage_text != "none":
        for prohibited in PROHIBITED_APPROVED_STORAGE:
            if prohibited in storage_text:
                error(f"security-privacy-boundary: prohibited approved_storage '{prohibited}'")
                ok = False

    behaviors = " ".join(data.get("prohibited_behaviors", [])).lower()
    for term in REQUIRED_PROHIBITED_BEHAVIORS:
        if term.replace("_", " ") not in behaviors and term not in behaviors:
            if term == "forms" and "contact_forms" in behaviors:
                continue
            if term == "uploads" and "file_uploads" in behaviors:
                continue
            if term == "external_script" and "external_script_sources" in behaviors:
                continue
            if term == "user_accounts" and "login_account" in behaviors:
                continue
            if term == "third_party_embeds" and "third_party_embeds" in behaviors:
                continue
            error(f"security-privacy-boundary: prohibited_behaviors missing '{term}' coverage")
            ok = False

    return ok


def validate_interaction_permissions() -> bool:
    ok = True
    data = load_json(ROOT / "data" / "interaction-permission-registry.json")
    permissions = data.get("permissions", [])
    if not permissions:
        error("interaction-permission-registry: permissions missing")
        return False

    seen: set[str] = set()
    by_id: dict[str, dict] = {}
    for perm in permissions:
        pid = perm.get("permission_id", "")
        if not PERMISSION_PATTERN.match(pid):
            error(f"interaction-permission-registry: invalid permission_id '{pid}'")
            ok = False
        missing = PERMISSION_REQUIRED - set(perm.keys())
        if missing:
            error(f"interaction-permission-registry '{pid}': missing fields {sorted(missing)}")
            ok = False
        seen.add(pid)
        by_id[pid] = perm

    if by_id.get("PERMISSION-0001", {}).get("status") != "allowed":
        error("interaction-permission-registry: PERMISSION-0001 must be allowed")
        ok = False
    if not by_id.get("PERMISSION-0001", {}).get("allowed_currently"):
        error("interaction-permission-registry: PERMISSION-0001 must be allowed_currently true")
        ok = False

    for pid, expected_name in REQUIRED_BLOCKED_PERMISSIONS.items():
        perm = by_id.get(pid)
        if perm is None:
            error(f"interaction-permission-registry: missing '{pid}'")
            ok = False
            continue
        if perm.get("status") != "blocked":
            error(f"interaction-permission-registry '{pid}': must be blocked")
            ok = False
        if perm.get("allowed_currently"):
            error(f"interaction-permission-registry '{pid}': allowed_currently must be false")
            ok = False
        if perm.get("name") != expected_name:
            error(f"interaction-permission-registry '{pid}': name must be '{expected_name}'")
            ok = False

    return ok


def validate_external_dependencies() -> bool:
    ok = True
    data = load_json(ROOT / "data" / "external-dependency-registry.json")
    blocked = [b.lower() for b in data.get("blocked_dependency_types", [])]
    for required in BLOCKED_DEPENDENCY_TYPES:
        if required not in blocked:
            error(f"external-dependency-registry: missing blocked type '{required}'")
            ok = False

    external_types = {
        "external_javascript",
        "analytics",
        "tracking",
        "cdn",
        "remote_font",
        "payment",
        "social",
        "api_client",
    }
    for dep in data.get("approved_dependencies", []):
        dtype = dep.get("type", "").lower()
        location = dep.get("location", "")
        if dtype not in {"first_party_local", "internal_local"}:
            if not dep.get("decision_log_ref"):
                error(
                    f"external-dependency-registry '{dep.get('dependency_id')}': "
                    "external dependency requires decision_log_ref"
                )
                ok = False
        if location and not (ROOT / location).exists():
            error(f"external-dependency-registry: approved dependency file missing '{location}'")
            ok = False
        combined = f"{dtype} {dep.get('name', '')} {location}".lower()
        for ext in external_types:
            if ext in combined and dtype not in {"first_party_local", "internal_local"}:
                if not dep.get("decision_log_ref"):
                    error(
                        f"external-dependency-registry: unapproved external dependency "
                        f"'{dep.get('dependency_id')}'"
                    )
                    ok = False
    return ok


def validate_index_html() -> bool:
    ok = True
    index_path = ROOT / "index.html"
    if not index_path.exists():
        error("security-privacy: index.html missing")
        return False

    content = index_path.read_text(encoding="utf-8")
    lower = content.lower()

    for pattern, label in INDEX_FORBIDDEN_PATTERNS:
        if pattern.startswith("<"):
            if pattern in lower:
                error(f"security-privacy: index.html contains {label}")
                ok = False
        elif contains_unnegated(lower, pattern):
            error(f"security-privacy: index.html contains {label}")
            ok = False

    if re.search(r'<script[^>]+src\s*=\s*["\']https?://', content, re.IGNORECASE):
        error("security-privacy: index.html contains external script src")
        ok = False

    if "upload" in lower and contains_unnegated(lower, "upload"):
        error("security-privacy: index.html contains upload workflow language")
        ok = False

    classifier_markers = ["try our classifier", "use our classifier", "run classifier", "classifier tool"]
    for marker in classifier_markers:
        if marker in lower:
            error(f"security-privacy: index.html contains public classifier interaction '{marker}'")
            ok = False

    return ok


def validate_styles_css() -> bool:
    ok = True
    css_path = ROOT / "styles.css"
    if not css_path.exists():
        error("security-privacy: styles.css missing")
        return False

    content = css_path.read_text(encoding="utf-8")
    lower = content.lower()

    if "@import" in lower:
        if re.search(r'@import\s+url\(["\']?https?://', lower):
            error("security-privacy: styles.css contains external @import")
            ok = False

    if "fonts.googleapis.com" in lower or "fonts.gstatic.com" in lower:
        error("security-privacy: styles.css contains remote font import")
        ok = False

    class_matches = re.findall(r"\.([a-z0-9_-]+)", lower)
    for class_name in class_matches:
        for pattern in CSS_PROHIBITED_CLASS_PATTERNS:
            if pattern in class_name:
                error(
                    f"security-privacy: styles.css prohibited class pattern '{pattern}' "
                    f"in '{class_name}'"
                )
                ok = False

    return ok


def validate_repository_scripts() -> bool:
    ok = True
    for rel in ["index.html", "styles.css"]:
        path = ROOT / rel
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8").lower()
        for pattern in ["fetch(", "xmlhttprequest", "localstorage", "sessionstorage", "document.cookie"]:
            if pattern in content:
                error(f"security-privacy: '{rel}' contains forbidden interaction '{pattern}'")
                ok = False
    js_files = list(ROOT.glob("**/*.js"))
    for js in js_files:
        if "node_modules" in str(js) or "validators" in str(js):
            continue
        rel = js.relative_to(ROOT)
        error(f"security-privacy: unexpected JavaScript file '{rel}'")
        ok = False
    return ok


def validate_source_registry_entries() -> bool:
    ok = True
    registry = load_json(ROOT / "data" / "source-registry.json")
    locations = {s.get("location") for s in registry.get("sources", [])}
    for required in [
        "SECURITY_PRIVACY_BOUNDARY.md",
        "data/security-privacy-boundary.json",
        "data/interaction-permission-registry.json",
        "data/external-dependency-registry.json",
        "validators/validate_security_privacy_boundary.py",
    ]:
        if required not in locations:
            error(f"source-registry: missing security/privacy source '{required}'")
            ok = False
    return ok


def main() -> int:
    checks = [
        ("Security privacy boundary data", validate_security_boundary_data),
        ("Interaction permission registry", validate_interaction_permissions),
        ("External dependency registry", validate_external_dependencies),
        ("Index HTML zero-interaction", validate_index_html),
        ("Styles CSS zero-dependency", validate_styles_css),
        ("Repository scripts and storage", validate_repository_scripts),
        ("Security privacy source registry", validate_source_registry_entries),
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
