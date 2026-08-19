---
title: Experience Cloud Test Plan Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, experience-cloud-test-plan-prompt]
---

# Experience Cloud Test Plan Prompt

```
Load skills/salesforce-functional-testing/SKILL.md.
Load skills/salesforce-functional-testing/knowledge/experience-cloud-testing.md.

Cloud: Experience Cloud
Business Scenario: <describe portal — e.g., customer self-service, partner portal>
Personas: <e.g., Portal Customer, Partner User, Guest User>
Objects/Features: Login, Registration, Case, Knowledge, File Upload, Navigation, LWC
Configuration: <sharing sets, guest profile, experience builder pages, SSO>

Generate an Experience Cloud functional test plan covering:
- Authentication flows (login, registration, SSO, MFA, password reset)
- Guest user access restrictions
- Self-service case creation and case visibility
- Knowledge article search and channel visibility
- File upload with size and type boundaries
- Navigation and page access per persona
- LWC component rendering and error states
- Negative authorization scenarios (chain PTA)
- UI automation readiness (chain PWR)
```

## Required Output Sections

All 15 sections from [SKILL.md](../SKILL.md) output schema, with Experience Cloud focus.

## Notes

- Mandatory guest user and negative authorization coverage
- Chain PTA for CRUD/FLS per external user profile
- Chain PWR for browser-level portal validation
