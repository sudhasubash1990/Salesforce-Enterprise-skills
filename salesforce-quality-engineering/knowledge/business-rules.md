---
title: Business Rules (QE)
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
  - salesforce-business-analyst/knowledge/business-rules.md
keywords: [business-rules]
tags: [knowledge, sprint-2]
---

# Business Rules — QE Extraction & Validation

**Purpose:** Extract, classify, and challenge business rules for testability during requirement analysis.

**Scope:** QE lens only. Authoring standards remain in BA: [BA business-rules.md](../../salesforce-business-analyst/knowledge/business-rules.md).

**Owner:** QE Practice Lead

**Version:** 0.3.0

**Status:** Draft (Sprint 2)

---

## What QE Looks For

| Rule type | Testability concern |
|-----------|---------------------|
| Decision rules | Branch coverage; conflicting decisions |
| Validation rules | Error message, field, timing |
| Calculation rules | Inputs, rounding, currency, timezone |
| Eligibility / entitlement | Persona and data preconditions |
| Compliance rules | Evidence and audit path |

## Extraction Steps

1. List rules stated explicitly in the artifact (`BR-#` if present).
2. Infer implied rules; label as **Assumed** with impact.
3. Map each rule to Salesforce component candidates (VR, Flow, Apex, CPQ, OmniStudio).
4. Flag missing error handling for each constraining rule.
5. Flag conflicts between rules.

## Output Shape

```markdown
### Business Rules
| ID | Rule | Source (Explicit/Implied) | Component hint | Gap? |
|----|------|---------------------------|----------------|------|
| BR-1 | … | Explicit | Validation Rule | … |
```

Do not invent formal rule IDs that pretend BA ownership—use provisional `BR-Q-#` when enriching.

## Related Documents

- [acceptance-criteria.md](acceptance-criteria.md)
- [requirement-review-framework.md](requirement-review-framework.md)
- [../../salesforce-business-analyst/knowledge/business-rules.md](../../salesforce-business-analyst/knowledge/business-rules.md)

## Future Enhancements

- Link rules to test scenarios in Sprint 3

## Navigation

- **Previous:** [stakeholder-analysis.md](stakeholder-analysis.md)
- **Next:** [acceptance-criteria.md](acceptance-criteria.md)
- **See Also:** [requirement-analysis.md](requirement-analysis.md)
