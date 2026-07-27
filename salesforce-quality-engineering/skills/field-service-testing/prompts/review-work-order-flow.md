---
title: Review Work Order Flow
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.19.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [field-service-testing, prompt]
---

# Review Work Order Flow

## Prompt

```
Act as Salesforce Field Service Testing capability. Provide Business Scenario and FSL Components Reviewed BEFORE detailed test cases. Produce all 18 sections per SKILL.md. Cover scheduling, mobile/offline, and inventory when in scope. Label assumptions; do not invent optimization scores or SLA values. Context:
[paste]
```

## Required Output Sections

1. Executive Summary
2. Business Scenario
3. FSL Components Reviewed
4. Scheduling Assessment
5. Dispatcher Assessment
6. Mobile Assessment
7. Inventory Assessment
8. Security Assessment
9. Performance Assessment
10. Offline Validation
11. Negative Test Scenarios
12. Edge Case Testing
13. Regression Scope
14. Automation Opportunities
15. Recommended SOQL Validation
16. Deployment Readiness
17. Risks
18. Recommendations

## Quality Gate

- Business Scenario and FSL Components Reviewed BEFORE detailed test cases.
- Cover scheduling, mobile/offline, and inventory when in scope.
- Label assumptions; do not invent optimization scores or SLA values.
