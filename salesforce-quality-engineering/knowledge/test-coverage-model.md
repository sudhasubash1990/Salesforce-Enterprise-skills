---
title: Test Coverage Model
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
keywords: [test-coverage, coverage-model]
tags: [knowledge, sprint-3, test-design]
---

# Test Coverage Model

**Purpose:** Analyse and improve test coverage across enterprise quality dimensions.

**Scope:** Coverage dimensions, gap detection, and matrix linkage. Not a numeric fake %-pass claim.

**Owner:** QE Practice Lead

**Version:** 0.4.0

**Status:** Draft (Sprint 3)

---

## Coverage Dimensions

| Dimension | Question |
|-----------|----------|
| Functional Coverage | Are AC behaviours represented by scenarios? |
| Business Rule Coverage | Does each rule have a verifying scenario? |
| Validation Coverage | Are VR / required / format rejects covered? |
| Integration Coverage | Are interfaces success + failure covered? |
| Security Coverage | Are allow/deny personas covered? |
| UI Coverage | Are layouts/messages/key controls covered? |
| Data Coverage | Are mandatory, defaults, edges covered? |
| Automation Coverage | Which High/Critical scenarios are automation-ready? |
| Regression Coverage | What neighbor risk is in the pack? |
| UAT Coverage | Are business-outcome scenarios ready for BA UAT? |
| Production Validation Coverage | What post-deploy checks are needed? |

## Gap Analysis Method

1. List requirements / AC / rules / components from analysis.
2. Map each to ≥1 scenario in the Quality Coverage Matrix.
3. Mark **Covered / Partial / Missing**.
4. Recommend improvements (new scenario types or technique changes).
5. Never invent a coverage percentage without evidence.

## Output Shape

```markdown
### Coverage Assessment
| Dimension | Status | Gaps | Recommendation |
|-----------|--------|------|----------------|
| Functional | Partial | AC4 message text | Add confirmation scenario once text known |
```

## Related Documents

- [test-design-engine.md](test-design-engine.md)
- [traceability.md](traceability.md)

## Navigation

- **Previous:** [test-design-techniques.md](test-design-techniques.md)
- **Next:** [risk-based-testing.md](risk-based-testing.md)
