# Hoax.ai Security and Privacy Boundary

**Version:** v1.0.0  
**Status:** governed_internal_security_privacy_boundary  
**Maturity:** zero_data_static_foundation  
**Decision:** DEC-024

## A. Purpose

This boundary defines the allowed and prohibited security and privacy posture for the current Hoax.ai foundation.

It enforces a static-first, zero-data posture before any future tool, engine, form, upload, analytics, API, or external dependency exists.

## B. Non-Purpose

This boundary does **not**:

- create a public tool;
- create a public classifier;
- create upload functionality;
- create forms;
- create analytics;
- create cookies;
- create API access;
- create user accounts;
- create monetization;
- create external deployment readiness;
- create legal compliance certification.

## C. Governing Principle

**No interaction before a privacy and security boundary exists.**

**A trust asset must not collect data before it can govern data.**

## D. Current Approved Posture

| Posture Element | Status |
|-----------------|--------|
| Static-first delivery | Approved |
| No user accounts | Approved |
| No forms | Approved |
| No uploads | Approved |
| No user-submitted evidence | Approved |
| No analytics | Approved |
| No cookies | Approved |
| No tracking pixels | Approved |
| No third-party scripts | Approved |
| No external JavaScript libraries | Approved |
| No API endpoints | Approved |
| No server-side processing | Approved |
| No payment collection | Approved |
| No newsletter capture | Approved |
| No personal data collection | Approved |
| Readable without JavaScript | Approved |
| GitHub repository as source of truth | Approved |

## E. Prohibited Current Behaviors

- file uploads;
- evidence submission;
- scan/check/detect forms;
- contact forms;
- newsletter forms;
- lead forms;
- analytics scripts;
- tracking pixels;
- cookies;
- localStorage/sessionStorage for tracking;
- third-party embeds;
- external script sources;
- uncontrolled fonts/CDNs;
- API calls;
- login/account systems;
- payment widgets;
- data collection before policy approval.

## F. Future Interaction Gate

Any future interaction must have:

- explicit decision log entry;
- interaction permission registry entry;
- threat model;
- privacy boundary;
- data minimization rule;
- retention rule;
- user disclosure language;
- validation coverage;
- audit record;
- rollback condition.

## G. Upload Gate

Upload functionality is blocked until a separate upload-security model exists.

Future upload handling must define: file types allowed; size limits; storage policy; retention policy; deletion policy; malware scanning posture; user consent; abuse prevention; no public accusation output; no automatic verdict output.

## H. Analytics Gate

Analytics are blocked until a separate measurement policy exists.

Future analytics must define: what is measured; why it is measured; what is not collected; cookie posture; anonymization where applicable; retention; disclosure; opt-out posture where applicable.

## I. External Dependency Gate

External libraries, CDNs, embeds, widgets, fonts, analytics, or scripts are blocked unless:

- listed in `data/external-dependency-registry.json`;
- approved by decision log;
- justified by necessity;
- checked for privacy/security impact;
- validated by tooling.

## J. Security Language Boundary

**Use:** No known unresolved critical security, privacy, technical, accessibility, or performance issues after validation.

**Do not use:** perfectly secure; no security gaps; fully secure; guaranteed safe; unhackable.

## K. Maturity

| Field | Value |
|-------|-------|
| Version | v1.0.0 |
| Status | governed_internal_security_privacy_boundary |
| Maturity | zero_data_static_foundation |

## Machine-Readable Sources

- Boundary: `data/security-privacy-boundary.json`
- Interaction permissions: `data/interaction-permission-registry.json`
- External dependencies: `data/external-dependency-registry.json`
- Validator: `validators/validate_security_privacy_boundary.py`

## Related Governance

- DEC-024
- `validators/validate_all.py` includes security/privacy validation
