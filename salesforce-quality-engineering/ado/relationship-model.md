---
title: Azure DevOps Relationship Model
version: 0.8.0
tags: [ado, sprint-6]
---

# Azure DevOps Relationship Model

## Purpose

Teach end-to-end hierarchy and traceability for Salesforce QE delivery in Azure DevOps.

## Hierarchy

```
Portfolio / Initiative (optional)
        ↓
      Epic
        ↓
     Feature
        ↓
   User Story
        ↓
      Task
        ↓
    Test Case  ←── Shared Steps
        ↓
       Bug
        ↓
   Regression pack (suites/tags)
        ↓
     Release
        ↓
Production Validation
```

## Traceability across levels

| From | To | Why it matters |
|------|----|----------------|
| Epic | Feature | Outcome decomposition |
| Feature | User Story | Shippable increments |
| User Story | AC / Business Rule | Testability |
| User Story | Test Scenario / Case | Coverage evidence |
| Test Case | Bug | Failure linkage |
| Bug | Regression | Prevent recurrence |
| Release | Prod Validation | Go-live evidence |

## Quality Engineering Perspective

Without links, dashboards lie and audits fail. QE owns the integrity of the chain from requirement intent to production validation.

## Related Documents

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../templates/README.md)
- [BA ADO Backlog Integration](../../salesforce-business-analyst/knowledge/ado-backlog-integration.md) (sibling—do not duplicate)
- [traceability-intelligence.md](traceability-intelligence.md)
- [artifact-generation.md](artifact-generation.md)

## Navigation

- **Previous:** [README.md](README.md)
- **Next:** [traceability-intelligence.md](traceability-intelligence.md)
