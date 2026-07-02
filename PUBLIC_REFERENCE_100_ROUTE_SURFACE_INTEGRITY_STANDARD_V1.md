# Public Reference 100-Route Surface Integrity Standard v1

**Decision:** DEC-134  
**Sprint:** Sprint 116  
**Status:** Active audit standard

## Standard statement

After reaching a major public route milestone, Hoax.ai must complete an integrity audit before further public route expansion.

## Audit-only constraint

At the 100-route milestone, the sprint must be audit-only. No new route, new condition, new crosswalk, tool, dashboard, graph layer, API, monetization page, or transaction/sales page is authorized.

## Required audit checks

1. **Route-count integrity**
   - sitemap URL count equals route-registry count equals 100.

2. **Registry alignment**
   - every route-registry path exists as static HTML;
   - every route HTML has matching route-registry and public-file-registry references.

3. **Metadata integrity**
   - every public route page has exactly one H1;
   - title, canonical, meta description, Open Graph title, and Open Graph description are present.

4. **Internal-link integrity**
   - internal absolute links resolve to existing registered routes;
   - no broken route-level links in public pages.

5. **Boundary-language integrity**
   - no unnegated detector/verdict/score/upload/API/transaction claims appear.

6. **Hub-summary integrity**
   - key hubs include explicit summary-oriented reference wording.

7. **Retrieval integrity**
   - key retrieval surfaces expose stable summary/answer/retrieval blocks or equivalent retrieval-safe orientation.

8. **Validator coverage integrity**
   - the Sprint 116 validator is wired into `validators/validate_all.py`.

## Forbidden positive capability phrases

Forbidden in public HTML unless clearly negated/prohibitive context:

- real or fake
- fake detector / ai detector / detects fake
- verifies truth
- scores authenticity / confidence score
- upload a file / submit evidence / analyze your file
- generate report
- for sale / asking price / valuation / term sheet
- private data room / downloadable report / pitch deck / sales page
- dashboard / graph tool / scorecard / rating system

## Required negative boundary allowance

The validator must allow explicit negative boundary language such as:

- not a transaction page
- not a pricing statement
- not a private data room
- not a downloadable report
- not a dashboard
- not a graph tool

## Closure criteria

Sprint 116 passes only when:

- integrity artifacts exist;
- validator passes;
- compileall validators passes;
- validate_all passes;
- required internal harnesses pass;
- no new public route is introduced.
