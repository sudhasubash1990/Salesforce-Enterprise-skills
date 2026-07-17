---
title: Scope Analysis
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
keywords: [scope]
tags: [knowledge, sprint-2]
---

# Scope Analysis

**Purpose:** Structure in-scope / out-of-scope and related boundary artifacts during requirement analysis.

**Scope:** Boundary analysis for QE. Does not own project scope decisions (PM/BA).

**Owner:** QE Practice Lead

**Version:** 0.3.0

**Status:** Draft (Sprint 2)

---

## Required Sections

| Section | QE focus |
|---------|----------|
| **In Scope** | Behaviours, personas, objects, integrations explicitly covered |
| **Out of Scope** | Explicit exclusions and deferred items |
| **Dependencies** | Upstream stories, data, env, integrations, licenses |
| **Assumptions** | `A#` with impact if false |
| **Constraints** | Time, org limits, regulatory, tool constraints |
| **Open Issues** | Unresolved conflicts or decisions |
| **Future Enhancements** | Parked ideas—not current test scope |

## Rules

- If out of scope is silent, ask or assume and label impact.
- Dependencies that block testing are **Critical** open questions.
- Future enhancements must not leak into Recommended Testing Areas without label.

## Output Shape

```markdown
### Scope
- **In scope:** …
- **Out of scope:** …
- **Dependencies:** …
- **Assumptions:** A1 …
- **Constraints:** …
- **Open issues:** …
- **Future enhancements:** …
```

## Related Documents

- [requirement-analysis.md](requirement-analysis.md)
- [requirement-risk-analysis.md](requirement-risk-analysis.md)
- [question-generation-framework.md](question-generation-framework.md)

## Future Enhancements

- Tie to quality gates entry criteria (later)

## Navigation

- **Previous:** [requirement-risk-analysis.md](requirement-risk-analysis.md)
- **Next:** [traceability.md](traceability.md)
- **See Also:** [stakeholder-analysis.md](stakeholder-analysis.md)
