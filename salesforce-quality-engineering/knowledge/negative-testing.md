---
title: Negative Testing
module: Salesforce Quality Engineering
category: Knowledge
document_type: Knowledge Article
version: 0.4.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/knowledge/test-design-engine.md
  - salesforce-quality-engineering/knowledge/requirement-analysis.md
keywords: [negative-testing]
tags: [knowledge, sprint-3, test-design]
---

# Negative Testing

**Purpose:** Confirm the system rejects invalid actions/data with observable outcomes.

**Scope:** Scenario objectives and design guidance only. Do **not** generate detailed test cases or automation scripts in Sprint 3.

**Owner:** QE Practice Lead

**Version:** 0.4.0

**Status:** Draft (Sprint 3)

---

## When to Use

Business rules, mandatory fields, invalid picklists, unauthorized actions.

## Guidance

- One meaningful invalid class per rule (not infinite junk data).
- Assert error visibility / blocked save—not only 'doesn't work'.
- Combine with [validation-rule-testing.md](validation-rule-testing.md) when VRs exist.

## Scenario Objectives (Examples)

Describe **what** to verify—not step scripts.

## Related Documents

- [test-design-engine.md](test-design-engine.md)
- [test-design-techniques.md](test-design-techniques.md)

## Future Enhancements

- Link to detailed case templates in Sprint 5

## Navigation

- **Previous:** [test-design-techniques.md](test-design-techniques.md)
- **Next:** [test-design-engine.md](test-design-engine.md)
- **See Also:** [test-coverage-model.md](test-coverage-model.md)
