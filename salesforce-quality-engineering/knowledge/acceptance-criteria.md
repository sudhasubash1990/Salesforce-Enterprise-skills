---
title: Acceptance Criteria (QE)
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
  - salesforce-business-analyst/knowledge/acceptance-criteria.md
keywords: [acceptance-criteria, testability]
tags: [knowledge, sprint-2]
---

# Acceptance Criteria — QE Review

**Purpose:** Review acceptance criteria for observability, completeness, and testability. Does **not** author full AC packs unless asked—prefer gap feedback to BA.

**Scope:** QE review checklist. Authoring standard: [BA acceptance-criteria.md](../../salesforce-business-analyst/knowledge/acceptance-criteria.md).

**Owner:** QE Practice Lead

**Version:** 0.3.0

**Status:** Draft (Sprint 2)

---

## Testability Checklist

| Check | Pass looks like |
|-------|-----------------|
| Observable outcome | Can be verified in UI/API/data without opinion |
| Given/When/Then (or equivalent) | Preconditions, action, result clear |
| Positive path | Happy path present |
| Negative / validation path | Error or reject path present when rules exist |
| Permission path | Persona without access handled when security relevant |
| Data precondition | Required records/fields stated or assumed |
| No implementation prescription | Avoids Apex class names unless constrained |

## Common Failures

- “System should be user-friendly / fast / handle correctly”
- Missing actor (who performs the action)
- Missing failure path for validation rules
- AC that cannot fail (always true)
- Duplicate AC with conflicting outcomes

## Output Shape

```markdown
### Acceptance Criteria Review
| AC | Testable? | Gaps | Recommendation |
|----|-----------|------|----------------|
| AC1 | Yes/Partial/No | … | … |

### Missing AC themes
- Negative path for …
- Permission path for …
```

**Do not generate test cases** from AC in Sprint 2—only review and recommend AC improvements.

## Related Documents

- [business-rules.md](business-rules.md)
- [requirement-review-framework.md](requirement-review-framework.md)
- [../../salesforce-business-analyst/knowledge/acceptance-criteria.md](../../salesforce-business-analyst/knowledge/acceptance-criteria.md)

## Future Enhancements

- Sprint 3: derive scenario intent from reviewed AC

## Navigation

- **Previous:** [business-rules.md](business-rules.md)
- **Next:** [requirements-quality-checklist.md](requirements-quality-checklist.md)
- **See Also:** [traceability.md](traceability.md)
