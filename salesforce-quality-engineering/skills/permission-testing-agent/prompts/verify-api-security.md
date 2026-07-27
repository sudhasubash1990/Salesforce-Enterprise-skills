---
title: Verify API Security
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.17.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [permission-testing, prompt]
---

# Verify API Security

## Prompt

```
Act as Permission Testing Agent. Reason through Security Context and Business Requirement BEFORE test scenarios. Produce all 19 sections per SKILL.md. Include CRUD, FLS, Sharing, negative scenarios. Delegate detailed SOQL to SOQL Validation Assistant when expanding section 17. Context:
[paste]
Focus: integration user, connected app, API CRUD/FLS.
```

## Required Output Sections

1. Executive Summary
2. Security Context
3. Business Requirement
4. Security Components Impacted
5. CRUD Validation Matrix
6. Field Level Security Validation
7. Record Access Validation
8. Sharing Validation
9. Profile Validation
10. Permission Set Validation
11. Permission Set Group Validation
12. API Security Validation
13. Experience Cloud Validation
14. Negative Test Scenarios
15. Regression Scope
16. Automation Candidates
17. Recommended SOQL Validation
18. Deployment Risks
19. Security Recommendations

## Quality Gate

- Security Context and Business Requirement BEFORE test scenarios.
- CRUD, FLS, Sharing, and Record Access sections required.
- Delegate SOQL expansion to SOQL Validation Assistant when needed.
