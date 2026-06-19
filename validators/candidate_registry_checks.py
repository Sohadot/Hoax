"""Shared reference candidate registry safety checks."""

from __future__ import annotations

from public_surface_checks import BATCH1_CANDIDATE_IDS, BATCH2_CANDIDATE_IDS

ALLOWED_CANDIDATE_STATUS = {"candidate_registered", "proposed_internal"}

REQUIRED_BLOCKED_FIELDS = {
    "route_status": "not_route_created",
    "sitemap_status": "not_sitemap_eligible",
    "publication_status": "publication_blocked",
}

BATCH1_REQUIRED_FIELDS = {
    "route_status": "public_reference_production_batch_1_route_created",
    "sitemap_status": "sitemap_eligible",
    "publication_status": "public_reference_production_batch_1",
}

BATCH2_REQUIRED_FIELDS = {
    "route_status": "public_reference_production_batch_2_route_created",
    "sitemap_status": "sitemap_eligible",
    "publication_status": "public_reference_production_batch_2",
}


def is_batch1_production_candidate(entry: dict) -> bool:
    return entry.get("candidate_id") in BATCH1_CANDIDATE_IDS


def is_batch2_production_candidate(entry: dict) -> bool:
    return entry.get("candidate_id") in BATCH2_CANDIDATE_IDS


def validate_batch1_production_candidate(entry: dict, error, label: str = "candidate") -> bool:
    ok = True
    cid = entry.get("candidate_id", "?")
    prefix = f"{label} {cid}"
    if entry.get("candidate_status") not in ALLOWED_CANDIDATE_STATUS:
        error(f"{prefix}: invalid candidate_status {entry.get('candidate_status')}")
        ok = False
    if entry.get("draft_status") != "production_page_created":
        error(f"{prefix}: draft_status must be production_page_created")
        ok = False
    for field, expected in BATCH1_REQUIRED_FIELDS.items():
        if entry.get(field) != expected:
            error(f"{prefix}: {field} must be {expected}")
            ok = False
    return ok


def validate_batch2_production_candidate(entry: dict, error, label: str = "candidate") -> bool:
    ok = True
    cid = entry.get("candidate_id", "?")
    prefix = f"{label} {cid}"
    if entry.get("candidate_status") not in ALLOWED_CANDIDATE_STATUS:
        error(f"{prefix}: invalid candidate_status {entry.get('candidate_status')}")
        ok = False
    if entry.get("draft_status") != "production_page_created":
        error(f"{prefix}: draft_status must be production_page_created")
        ok = False
    for field, expected in BATCH2_REQUIRED_FIELDS.items():
        if entry.get(field) != expected:
            error(f"{prefix}: {field} must be {expected}")
            ok = False
    return ok


def validate_candidates_blocked_only(candidates: list, error) -> bool:
    """Return True if every registry candidate is internal-only and blocked from public output."""
    ok = True
    for entry in candidates:
        if entry.get("public_reference_pilot_status") == "converted_to_controlled_public_reference_pilot":
            continue
        cid = entry.get("candidate_id", "?")
        if is_batch1_production_candidate(entry):
            if not validate_batch1_production_candidate(entry, error):
                ok = False
            continue
        if is_batch2_production_candidate(entry):
            if not validate_batch2_production_candidate(entry, error):
                ok = False
            continue
        status = entry.get("candidate_status", "")
        if status not in ALLOWED_CANDIDATE_STATUS:
            error(f"candidate {cid}: invalid candidate_status {status}")
            ok = False
        draft_status = entry.get("draft_status", "")
        if draft_status not in ("not_draft_created", "internal_draft_created"):
            error(f"candidate {cid}: invalid draft_status {draft_status}")
            ok = False
        for field, expected in REQUIRED_BLOCKED_FIELDS.items():
            if entry.get(field) != expected:
                error(f"candidate {cid}: {field} must be {expected}")
                ok = False
        if entry.get("route_active") is True or entry.get("sitemap_eligible") is True:
            error(f"candidate {cid}: must not be route-active or sitemap-eligible")
            ok = False
        if entry.get("draft_created") is True or entry.get("publication_eligible") is True:
            error(f"candidate {cid}: must not be draft-created or publication-eligible")
            ok = False
    return ok
