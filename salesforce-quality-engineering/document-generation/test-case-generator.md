---
title: Test Case Generator
version: 0.7.0
tags: [document-generation, sprint-5]
---

# Test Case Generator

## Formats

| Format | Notes |
|--------|-------|
| Azure DevOps | Title, steps HTML, AC link, tags |
| Excel | Columns for Step / Action / Expected |
| Jira Xray / Zephyr | Preserve step entities |
| Manual | Nested Given/When/Then acceptable |

## Fields

Title · Objective · Preconditions · Test Data · Steps · Expected Results · Postconditions · Automation Candidate · Priority · Requirement Mapping · Regression/Smoke/UAT tags

## Rules

- Generate only after scenario objectives (or explicit user request with ready AC).
- Include negative and permission paths when security is in scope.
- Template: [test-case-document](../templates/test-case-document.md)


## Related

- [QE Brain (Sprint 1)](../brain/README.md)
- [Requirement Analysis (Sprint 2)](../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../knowledge/clouds/README.md)
