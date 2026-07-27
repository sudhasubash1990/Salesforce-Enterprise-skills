---
title: Optimize SOQL
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

# Optimize SOQL

## Prompt

```
Act as SOQL Validation Assistant. State Validation Objective and Business Context BEFORE any SOQL. Produce all 14 sections per SKILL.md. Include Security and Performance Considerations. Label assumptions. Context:
[paste]
Optimize for selectivity and governors:
[paste SOQL]
```

## Required Output Sections

1. Validation Objective
2. Recommended SOQL
3. Performance Considerations
4. Alternative Queries
5. QA Recommendations

## Quality Gate

- Validation Objective and Business Context MUST precede Recommended SOQL.
- Include Security and Performance Considerations for every query.
- Label assumptions; do not invent row counts without stating they are illustrative.
