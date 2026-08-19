---
title: Sales Cloud Test Plan Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, sales-cloud-test-plan-prompt]
---

# Sales Cloud Test Plan Prompt

```
Load skills/salesforce-functional-testing/SKILL.md.
Load skills/salesforce-functional-testing/knowledge/sales-cloud-testing.md.

Cloud: Sales Cloud
Business Scenario: <describe Sales Cloud process — e.g., lead-to-close, campaign management>
Personas: <e.g., Sales Rep, Sales Manager, Marketing User>
Objects: Lead, Account, Contact, Opportunity, Product, Price Book, Campaign
Configuration: <lead assignment rules, stage definitions, validation rules, approval processes>

Generate a Sales Cloud functional test plan covering:
- Lead lifecycle (create, assign, qualify, convert, disqualify)
- Lead conversion (new vs. existing Account/Contact matching)
- Opportunity stage progression with required fields
- Product and price book association
- Campaign member management and influence
- Forecast rollup validation
- Positive, negative, and boundary scenarios
- Backend verification (chain SOVA)
- Test data prerequisites (chain TDG)
```

## Required Output Sections

All 15 sections from [SKILL.md](../SKILL.md) output schema, with Sales Cloud focus.

## Notes

- Test lead conversion with both new and existing records
- Validate forecast recalculation after stage changes
- Include multi-currency scenarios if applicable
