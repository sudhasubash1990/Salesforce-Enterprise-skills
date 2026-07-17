---
title: Artifact Relationships
version: 0.7.0
---

# Artifact Relationships

```
Requirement Review / Gap / Quality Score
        ↓
   Risk Assessment
        ↓
 Test Strategy → Test Plan
        ↓
 Test Design (scenarios) → RTM
        ↓
 Test Cases ←→ Automation Candidate Matrix
        ↓
 Execution (Daily/Weekly) + Defects
        ↓
 Test Summary → Release Readiness → Go/No-Go
        ↓
 Production Validation → Hypercare → Lessons Learned / KT
```

## Traceability chain (RTM)

Business Requirement → User Story → AC → Business Rule → Salesforce Component → Scenario → Case → Automation → Regression → Production Validation

## Related

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
