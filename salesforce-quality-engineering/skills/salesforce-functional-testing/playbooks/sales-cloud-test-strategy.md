---
title: Sales Cloud Test Strategy
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, sales-cloud-test-strategy]
---

# Sales Cloud Test Strategy

## Objective

Plan and execute functional testing for Sales Cloud implementations covering lead management, conversion, opportunity lifecycle, products, campaigns, and forecasts.

## Inputs

- Sales process documentation (lead-to-close workflow)
- Sales Cloud configuration (lead assignment, stage definitions, validation rules)
- Persona list (sales rep, manager, operations, marketing)
- Product catalog and price book structure
- Forecast hierarchy and territory model

## Validation Workflow

1. Confirm lead sources and assignment rule criteria
2. Map lead conversion scenarios (new vs. existing Account/Contact)
3. Design opportunity stage progression with required fields per stage
4. Validate product association and price book selection logic
5. Test campaign member management and influence tracking
6. Verify forecast rollup through role/territory hierarchy
7. Chain [SOVA](../../soql-validation-assistant/SKILL.md) for post-conversion record verification
8. Chain [TDG](../../test-data-generator/SKILL.md) for seed data (accounts, leads, products)

## Decision Points

| Decision | Criteria |
|----------|----------|
| Include territory testing | Territory management enabled |
| Include multi-currency | Multi-currency enabled and multiple price books |
| Include quote testing | Quotes enabled with approval process |
| Include forecast testing | Collaborative forecasting configured |

## Expected Results

- Leads route to correct owners per assignment rule criteria
- Lead conversion creates/maps Account, Contact, and Opportunity correctly
- Opportunity stage transitions enforce required fields and validation rules
- Forecast categories update when opportunity stage changes
- Campaign influence attribution tracks correctly across multiple touchpoints

## Anti-Patterns

- Testing lead conversion only with new records — ignoring duplicate matching
- Skipping forecast recalculation after stage changes
- Testing products without multi-currency when org has multiple currencies

## Related Documents

- [Sales Cloud Testing Knowledge](../knowledge/sales-cloud-testing.md)
- [SKILL.md](../SKILL.md)
