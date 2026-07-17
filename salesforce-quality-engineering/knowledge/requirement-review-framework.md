---
title: Requirement Review Framework
module: Salesforce Quality Engineering
category: Knowledge
document_type: Knowledge Article
version: 0.3.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/knowledge/requirement-analysis.md
  - salesforce-quality-engineering/knowledge/question-generation-framework.md
keywords: [requirement-review, validation]
tags: [knowledge, sprint-2]
---

# Requirement Review Framework

**Purpose:** Structured review workflow and validation catalog for QE requirement inspection.

**Scope:** How to review and what defect types to find. Scoring in [requirements-quality-checklist.md](requirements-quality-checklist.md).

**Owner:** QE Practice Lead

**Version:** 0.3.0

**Status:** Draft (Sprint 2)

---

## Requirement Analysis Philosophy

- Requirements are the primary quality control surface before code.
- QE reviews for **testability, completeness, consistency, and risk**—not to replace the BA.
- Ambiguity is a defect candidate until clarified or assumed with impact.
- Enrichment means surfacing gaps and questions—not inventing silent scope.

## Requirement Review Workflow

```
Receive requirement artifact
    ↓
Classify (story / epic / feature / BRD / FRD excerpt)
    ↓
Run Requirement Analysis Engine (10 steps)
    ↓
Apply Validation Catalog (below)
    ↓
Score quality (1–5 dimensions)
    ↓
Generate questions (Critical → Low)
    ↓
Document risks, scope, assumptions
    ↓
Recommend testing / regression / automation focus (intent only)
    ↓
Next steps (clarify → re-review → only then design tests in later sprints)
```

## Requirement Validation Process

For each finding: **ID · Type · Evidence · Impact · Recommendation · Owner (BA/Arch/Dev/PM)**.

### Requirement Validation Catalog

| Defect type | What to look for |
|-------------|------------------|
| Missing Business Rules | Decisions without stated rule |
| Missing Acceptance Criteria | No Given/When/Then or untestable “done” |
| Conflicting Requirements | Two statements that cannot both be true |
| Ambiguous Requirements | Vague words (fast, easy, handle, etc.) |
| Incomplete Requirements | Partial journeys; missing actors or outcomes |
| Duplicate Requirements | Same need stated twice with drift |
| Missing Error Handling | No negative / failure path |
| Missing Validation Rules | Field/process constraints unspecified |
| Missing Security Requirements | No persona, CRUD/FLS, sharing |
| Missing Data Requirements | No seed/master/migration needs |
| Missing Integration Details | System, contract, timing, failure unknown |
| Missing Notification Requirements | Who is notified when / how |
| Missing Reporting Requirements | Ops/KPI visibility unspecified |
| Missing Performance Requirements | Volume/SLA silent when material |
| Missing Audit Requirements | Who changed what / when needed |
| Missing Compliance Requirements | Regulated claim without control |
| Missing Deployment Considerations | Feature flags, activation, data cutover |

## Related Documents

- [requirement-analysis.md](requirement-analysis.md)
- [acceptance-criteria.md](acceptance-criteria.md)
- [business-rules.md](business-rules.md)

## Future Enhancements

- Severity taxonomy aligned to ADO severity fields (Sprint 6)

## Navigation

- **Previous:** [requirement-analysis.md](requirement-analysis.md)
- **Next:** [question-generation-framework.md](question-generation-framework.md)
- **See Also:** [requirements-quality-checklist.md](requirements-quality-checklist.md)
