---
title: Decision Table Testing
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
keywords: [decision-table]
tags: [knowledge, sprint-3, test-design]
---

# Decision Table Testing

**Purpose:** Tabulate condition combinations → expected actions/rules.

**Scope:** Scenario objectives and design guidance only. Do **not** generate detailed test cases or automation scripts in Sprint 3.

**Owner:** QE Practice Lead

**Version:** 0.4.0

**Status:** Draft (Sprint 3)

---

## When to Use

Complex eligibility, routing, multi-rule Flows, CPQ-like rules.

## Guidance

- Collapse impossible combinations.
- Prioritize Business Critical/High rows first ([risk-based-testing.md](risk-based-testing.md)).

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
