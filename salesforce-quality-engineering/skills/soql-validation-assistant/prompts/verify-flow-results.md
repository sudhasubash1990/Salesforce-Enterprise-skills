---
title: Verify Flow Results
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.16.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [soql-validation, prompt]
---

# Verify Flow Results

## Prompt

```
Act as SOQL Validation Assistant. State Validation Objective and Business Context BEFORE any SOQL. Produce all 14 sections per SKILL.md. Include Security and Performance Considerations. Label assumptions. Context:
[paste]
Focus: records created/updated by Flow; related object state.
```

## Required Output Sections

1. Validation Objective
2. Business Context
3. Recommended SOQL
4. Query Explanation
5. Expected Result
6. Backend Validation Steps
7. Security Considerations
8. Performance Considerations
9. Automation Opportunities
10. Related Metadata
11. Negative Validation
12. Edge Cases
13. Alternative Queries
14. QA Recommendations

## Quality Gate

- Validation Objective and Business Context MUST precede Recommended SOQL.
- Include Security and Performance Considerations for every query.
- Label assumptions; do not invent row counts without stating they are illustrative.
