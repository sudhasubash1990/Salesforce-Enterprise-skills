---
title: Review Integration Procedure
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.22.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [omnistudio-qa, prompt]
---

# Review Integration Procedure

## Prompt

```
Load skills/omnistudio-qa/SKILL.md.
Review Integration Procedure: {{IPName}} — branches, cache, retry, remotes, SF ops.
Populate Integration Validation, Negatives, and SOVA stubs.
```

## Required Output Sections

1. Executive Summary
2. Business Scenario
3. OmniStudio Components Reviewed
4. Architecture Assessment
5. Functional Validation
6. Data Validation
7. JSON Validation
8. Integration Validation
9. Security Assessment
10. Performance Assessment
11. Negative Test Scenarios
12. Edge Case Testing
13. Regression Scope
14. Automation Opportunities
15. Deployment Readiness
16. Risks
17. Recommendations

## Quality Gate

- Business Scenario + OmniStudio Components Reviewed BEFORE detailed test cases.
- Label assumptions; do not invent latency/throughput or SLA percentages.
- Chain MIA / SOVA / PTA / PWR / AFT / TDG when applicable.
