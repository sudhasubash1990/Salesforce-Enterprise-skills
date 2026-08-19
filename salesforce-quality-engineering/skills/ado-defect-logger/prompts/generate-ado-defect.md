---
title: Generate ADO Defect Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, generate-ado-defect]
---

# Generate ADO Defect

## Prompt

```
Generate a complete ADO Bug work item for the following defect.
Include ALL fields from the ADO defect template.
Repro steps MUST be numbered and reproducible by another tester.

Defect details:
<paste defect details, error messages, screenshots, logs>

Environment:
<org/sandbox, browser, user profile>

Related requirement:
<user story or requirement ID>

Related test case:
<test case ID if applicable>

Instructions:
- Generate the full ADO Bug format (do NOT create in ADO unless I explicitly ask)
- Include root cause hypothesis
- Assess severity and priority with justification
- List evidence attached vs evidence still needed
```

## Expected Output

Complete ADO Bug work item in markdown format, ready for manual entry or API creation.
