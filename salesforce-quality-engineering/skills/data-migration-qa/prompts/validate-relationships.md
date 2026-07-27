---
title: Validate Relationships
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.23.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [data-migration-qa, prompt]
---

# Validate Relationships

## Prompt

```
Load skills/data-migration-qa/SKILL.md.
Validate relationship migration and lookup resolution for {{ObjectGraph}}.
Include load order, orphans, External ID resolve, and SOQL stubs.
```

## Required Output Sections

1. Executive Summary
2. Migration Scope
3. Source System Assessment
4. Target System Assessment
5. Data Mapping Review
6. Transformation Validation
7. Relationship Validation
8. Record Count Validation
9. Data Quality Assessment
10. Reconciliation Strategy
11. Security Assessment
12. Performance Assessment
13. Negative Test Scenarios
14. Regression Scope
15. Automation Opportunities
16. Recommended SOQL Validation
17. Cutover Readiness
18. Rollback Readiness
19. Hypercare Validation
20. Risks and Recommendations

## Quality Gate

- Migration Scope + Source/Target Assessment BEFORE detailed validation cases.
- Label assumptions; do not invent throughput/duration or SLA percentages.
- Do not claim GDPR certification; flag Legal/Compliance when needed.
- Chain MIA / SOVA / PTA / TDG / PWR / OSQA / AFT when applicable.
