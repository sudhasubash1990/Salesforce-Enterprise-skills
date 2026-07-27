---
title: Improve Test Maintainability
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.21.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [playwright-review, prompt]
---

# Improve Test Maintainability

## Prompt

```
Act as Salesforce Playwright Review (PWR). Provide Framework Assessment context BEFORE line-by-line script critique. Produce all 18 sections per SKILL.md. Score 1–5 with evidence or N/A; do not invent coverage or flake %. Refactoring suggestions as snippets only unless full rewrite requested. Context:
[paste]
Focus: Maintainability, Refactoring Suggestions, Overall Quality Score.
```

## Required Output Sections

1. Executive Summary
2. Framework Assessment
3. Architecture Review
4. Code Quality Review
5. Locator Review
6. Assertion Review
7. Synchronization Review
8. Salesforce Compatibility Review
9. Maintainability Assessment
10. Performance Analysis
11. CI/CD Readiness
12. Security Considerations
13. Flaky Test Analysis
14. Risks
15. Recommendations
16. Refactoring Suggestions
17. Best Practices
18. Overall Quality Score

## Quality Gate

- Framework context and review scope BEFORE line-by-line critique.
- 1–5 scores with evidence or N/A; no invented coverage/flake %.
- Refactoring suggestions as snippets only unless full rewrite requested.
