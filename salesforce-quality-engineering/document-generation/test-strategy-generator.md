---
title: Test Strategy Generator
version: 0.7.0
tags: [document-generation, sprint-5]
---

# Test Strategy Generator

## When to use

Program or major release start. Template: [test-strategy](../templates/test-strategy.md).

## Required inputs

Business objectives · Scope/clouds · Constraints · Risks · Environments · Automation intent · Org methodology (Agile/SAFe/Waterfall)

## Generation steps

1. Confirm Strategy is warranted (vs lightweight plan-only).
2. Run/reuse Requirement Analysis themes for scope risks.
3. Map testing types/levels to Salesforce components (4A/4B).
4. Fill all mandatory strategy sections:
   Scope · Objectives · Testing Types · Environment Strategy · Resource Strategy · Risk Strategy · Automation Strategy · Regression Strategy · Defect Management · Entry Criteria · Exit Criteria · Assumptions · Dependencies · Deliverables · Communication Plan · Metrics · Governance
5. Mark assumptions; list open questions.
6. Route for review/approval.

## Tailoring

| Size | Tailoring |
|------|-----------|
| Small change | 1–2 page strategy addendum |
| Enterprise program | Full strategy + governance |


## Related

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
