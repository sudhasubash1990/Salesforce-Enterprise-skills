---
title: Decision Framework
module: Salesforce Quality Engineering
category: Brain
document_type: Framework
version: 0.2.1
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/skill.md
  - salesforce-quality-engineering/brain/thinking-model.md
  - salesforce-quality-engineering/brain/brain.md
keywords: [decision-framework]
tags: [brain, decisions]
---

# Decision Framework

**Purpose:** Decision trees and heuristics for when to clarify, pause, or proceed to recommendations and deliverables.

**Scope:** Completeness gate, proceed/pause logic, and prefer/avoid heuristics. Stage catalog is in [thinking-model.md](thinking-model.md).

**Owner:** QE Practice Lead

**Version:** 0.2.1

**Status:** Draft (Sprint 1 — modular Brain)

---

## Primary Decision Tree

```
Requirement / story complete enough for the asked deliverable?
    ↓
If No
    ↓
Generate clarification questions (prioritized)
    ↓
Document assumptions (impact if false)
    ↓
Pause or produce a gap/risk advisory only
    ↓
If Yes
    ↓
Identify risks (product, data, integration, security, regression)
    ↓
Determine testing scope (in / out / deferred)
    ↓
Recommend documentation (which deliverable types—do not invent templates)
    ↓
Recommend automation (purpose, candidates, exclusions)
    ↓
Recommend regression (impacted areas, pack depth)
    ↓
Generate requested deliverables (when engines/templates exist; otherwise advisory outline)
```

## Completeness Gate

| Signal | Action |
|--------|--------|
| Missing persona, goal, or outcome | Must clarify (blocker) |
| Untestable or missing AC | Challenge + clarify; do not invent AC silently |
| Missing business rules for constrained behaviour | Ask or label assumption with high impact |
| Unknown security/persona access for UI/data change | Must clarify before permission-path claims |
| Unknown integration contract for interface change | Must clarify before integration coverage claims |
| Material open questions (Stage 27) | Pause heavy deliverables; advisory only |

## Decision Heuristics

| Decision | Prefer | Avoid |
|----------|--------|-------|
| Incomplete AC | Challenge + clarify | Inventing AC silently |
| High business risk | Deeper exploratory + negative + permission paths | Happy-path-only coverage |
| Stable UI + high regression | Automation candidate | Automating unstable or one-off flows |
| Config-only change | Declarative impact tests | Unnecessary Apex-level design |
| Integration involved | Contract + failure + idempotency paths | UI-only coverage |
| UAT | Business-outcome scenarios; partner with BA | Replacing BA UAT ownership |
| Go / No-Go | Evidence against gates | Opinion without evidence |

## Recommendation Priority

| Priority | Use for |
|----------|---------|
| **P0** | Blockers, safety/security, go-live threats |
| **P1** | Core AC / happy + critical negative paths |
| **P2** | Important regression and persona variants |
| **P3** | Nice-to-have / exploratory depth |

Lead with P0/P1. Label automation and regression recommendations with **purpose** (why), not only what.

## Related Documents

- [thinking-model.md](thinking-model.md)
- [brain.md](brain.md)
- [response-guidelines.md](response-guidelines.md)

## Future Enhancements

- Sprint 8: expand automation decision tree
- Sprint 9: expand regression impact decision tree

## Navigation

- **Previous:** [thinking-model.md](thinking-model.md)
- **Next:** [response-guidelines.md](response-guidelines.md)
- **See Also:** [quality-gates.md](../knowledge/quality-gates.md)
