---
title: Rtm Generator
version: 0.7.0
tags: [document-generation, sprint-5]
---

# RTM Generator

## Traceability chain

Business Requirement → User Story → Acceptance Criteria → Business Rule → Salesforce Component → Test Scenario → Test Case → Automation → Regression → Production Validation

## Supported views

| RTM type | Use |
|----------|-----|
| Business RTM | Program/BR coverage |
| Sprint RTM | Sprint backlog coverage |
| Release RTM | Release train evidence |
| UAT RTM | Business validation mapping |
| Regression RTM | Pack ↔ prior requirements |

## Rules

- Never invent coverage %.
- Gap rows must list remediation owner.
- Template: [rtm](../templates/rtm.md)


## Related

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
