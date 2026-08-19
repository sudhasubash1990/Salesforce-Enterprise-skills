---
title: Service Cloud Test Plan Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, service-cloud-test-plan-prompt]
---

# Service Cloud Test Plan Prompt

```
Load skills/salesforce-functional-testing/SKILL.md.
Load skills/salesforce-functional-testing/knowledge/service-cloud-testing.md.

Cloud: Service Cloud
Business Scenario: <describe Service Cloud process — e.g., case management, Omni-Channel routing>
Personas: <e.g., Service Agent, Service Manager, Customer (portal)>
Objects: Case, Knowledge, Entitlement, Queue
Configuration: <assignment rules, escalation rules, Omni-Channel config, entitlements>

Generate a Service Cloud functional test plan covering:
- Case lifecycle (create, assign, escalate, resolve, close)
- All case channels in scope (manual, Email-to-Case, Web-to-Case)
- Omni-Channel routing and capacity scenarios
- Knowledge article search and visibility
- Entitlement and milestone validation
- Positive, negative, and boundary scenarios
- Persona-based access (chain PTA)
- Backend verification (chain SOVA)
```

## Required Output Sections

All 15 sections from [SKILL.md](../SKILL.md) output schema, with Service Cloud focus.

## Notes

- Include time-dependent escalation scenarios
- Verify Omni-Channel overflow behavior
- Chain PTA for case visibility per profile
