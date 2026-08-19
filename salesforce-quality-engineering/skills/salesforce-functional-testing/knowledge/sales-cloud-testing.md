---
title: Sales Cloud Functional Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Guide
document_type: Guide
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, sales-cloud-testing]
---

# Sales Cloud Functional Testing

## Purpose

Provide testing guidance for Sales Cloud objects, features, and automation — Leads, conversion, Opportunities, stages, products, price books, Campaigns, forecasts, account hierarchy, and territory management.

## Business Context

Sales Cloud drives revenue pipeline. Functional defects in lead conversion, opportunity stage progression, or forecast rollup directly impact pipeline accuracy and sales team productivity. Testing must cover the full lead-to-close lifecycle.

## Assessment Criteria

- Lead lifecycle tested from creation through conversion and disqualification
- Opportunity stage transitions validated with required fields and validation rules
- Product and price book associations verified across currency and discount scenarios
- Campaign influence and member status tracking confirmed

## Key Areas

- **Lead CRUD:** Create, assign, qualify, convert, disqualify, merge, duplicate management
- **Lead Conversion:** Account/Contact/Opportunity creation, existing record matching, field mapping
- **Opportunity Stages:** Stage path, required fields per stage, probability, close date enforcement
- **Products & Price Books:** Product association, price book assignment, multi-currency, discount schedules
- **Quotes:** Quote creation, sync, line items, PDF generation, approval
- **Campaigns:** Campaign creation, member add/status, influence, ROI fields
- **Forecasts:** Forecast category mapping, rollup hierarchy, override, snapshot
- **Account Hierarchy:** Parent-child relationships, rollup fields, territory assignment
- **Territory Management:** Assignment rules, territory hierarchy, opportunity territory

## Decision Framework

| Scenario | Testing Focus |
|----------|---------------|
| Lead management rollout | Lead lifecycle + conversion + duplicate rules |
| Pipeline visibility | Opportunity stages + forecast rollup + reports |
| Product catalog setup | Products + price books + quotes + discounts |
| Campaign launch | Member management + influence + ROI tracking |

## Best Practices

- Test lead conversion with existing Account/Contact to verify matching logic
- Validate opportunity stage transitions enforce required fields before advancing
- Test forecast rollup with territory hierarchy and role hierarchy
- Verify campaign member status transitions follow defined picklist sequence
- Chain [SOVA](../../soql-validation-assistant/SKILL.md) for backend record verification post-conversion

## Anti-Patterns

- Testing lead conversion only with new records — missing existing-record matching
- Skipping forecast validation after opportunity stage changes
- Assuming price book behavior is identical across currencies

## Related Documents

- [Sales Cloud Knowledge](../../../knowledge/clouds/sales-cloud.md)
- [SKILL.md](../SKILL.md)
- [SOQL Validation Assistant](../../soql-validation-assistant/SKILL.md)
