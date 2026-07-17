---
title: Requirements Quality Checklist
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
  - salesforce-quality-engineering/knowledge/requirement-review-framework.md
keywords: [quality-score, checklist]
tags: [knowledge, sprint-2]
---

# Requirements Quality Checklist & Score

**Purpose:** Requirement Quality Assessment Model—score and improve requirement readiness for testing.

**Scope:** Dimensions, 1–5 rubric, overall score, improvement recommendations. Not a gate waiver process.

**Owner:** QE Practice Lead

**Version:** 0.3.0

**Status:** Draft (Sprint 2)

---

## Quality Dimensions (Score 1–5 Each)

| Dimension | 1 (Poor) | 3 (Acceptable) | 5 (Strong) |
|-----------|----------|----------------|------------|
| **Completeness** | Major gaps | Core path present; some gaps | End-to-end + rules + security + data |
| **Clarity** | Ambiguous | Mostly clear | Precise, unambiguous language |
| **Consistency** | Conflicts | Minor tension | No conflicts across statements |
| **Testability** | Untestable | Partially observable | Fully observable AC |
| **Traceability** | Orphan | Partial links | Objective → story → AC → component intent |
| **Feasibility** | Unclear / unlikely | Plausible with risks | Platform-aligned and actionable |
| **Maintainability** | Opaque | Understandable | Modular, reusable phrasing |
| **Business Value** | Unclear why | Stated benefit | Measurable outcome |
| **Risk** *(invert)* | Extreme unmanaged risk = 1 | Managed medium = 3 | Low residual / mitigated = 5 |

> For **Risk**, higher score = healthier (lower residual risk). Call out raw risks separately in [requirement-risk-analysis.md](requirement-risk-analysis.md).

## Overall Requirement Quality Score

```
Overall = average of the nine dimension scores (round to 1 decimal)
```

| Overall | Band | Guidance |
|---------|------|----------|
| 4.5–5.0 | Excellent | Ready for test design (later sprint) with minor notes |
| 3.5–4.4 | Good | Proceed with documented assumptions |
| 2.5–3.4 | Fair | Clarify Critical/High questions before heavy design |
| 1.0–2.4 | Poor | Pause; return to BA/PO for enrichment |

## Checklist (Quick Scan)

- [ ] Business objective stated
- [ ] Persona / actor clear
- [ ] In / out of scope clear
- [ ] Business rules explicit or questioned
- [ ] AC present and testable
- [ ] Error handling addressed
- [ ] Security / persona access addressed (if UI/data)
- [ ] Data needs addressed
- [ ] Integration details addressed (if applicable)
- [ ] Reporting / notification needs considered
- [ ] NFR / audit / compliance considered when material
- [ ] Deployment considerations noted when material

## Output Shape

```markdown
### Requirement Quality Assessment
| Dimension | Score (1–5) | Notes |
|-----------|-------------|-------|
| Completeness | | |
| Clarity | | |
| Consistency | | |
| Testability | | |
| Traceability | | |
| Feasibility | | |
| Maintainability | | |
| Business Value | | |
| Risk (health) | | |
| **Overall** | **X.X** | Band: … |

### Improvement recommendations
1. …
```

## Related Documents

- [requirement-analysis.md](requirement-analysis.md)
- [requirement-review-framework.md](requirement-review-framework.md)
- [acceptance-criteria.md](acceptance-criteria.md)

## Future Enhancements

- Automate scoring assist from gap catalog counts

## Navigation

- **Previous:** [acceptance-criteria.md](acceptance-criteria.md)
- **Next:** [requirement-analysis.md](requirement-analysis.md)
- **See Also:** [question-generation-framework.md](question-generation-framework.md)
