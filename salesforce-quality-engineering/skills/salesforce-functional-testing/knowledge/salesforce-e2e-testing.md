---
title: Salesforce E2E Testing Patterns
module: Salesforce Quality Engineering
category: QE Specialized Skill Guide
document_type: Guide
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, e2e-testing]
---

# Salesforce E2E Testing Patterns

## Purpose

Define cross-cloud end-to-end journey testing patterns that validate business processes spanning Service Cloud, Sales Cloud, and Experience Cloud.

## Business Context

Enterprise Salesforce implementations connect multiple clouds. A lead captured via a campaign may convert to an opportunity managed in Sales Cloud while the customer self-serves through Experience Cloud. E2E testing validates these journeys are seamless and data-consistent across cloud boundaries.

## Assessment Criteria

- Each E2E journey has a defined start event, cloud transitions, and end state
- Data consistency verified at every cloud boundary (shared objects: Account, Contact)
- Persona transitions mapped (e.g., marketing user → sales rep → service agent)

## Key Areas

### Journey Patterns

| Journey | Clouds | Key Verification Points |
|---------|--------|------------------------|
| Lead → Conversion → Opp → Close | Sales | Account/Contact created, Opp stage, forecast update |
| Customer → Portal → Case → Agent → Resolution | Experience + Service | Portal login, case creation, routing, agent action, closure |
| Account → Contact → Opp → Product → Approval → Contract | Sales | Approval chain, product line items, contract generation |
| Campaign → Lead → Assignment → Conversion → Opp | Sales | Campaign member, lead source, assignment rule, conversion |

### Cross-Cloud Verification

- Shared object consistency (Account, Contact records match across cloud contexts)
- Automation trigger sequencing (Flow/Process Builder firing order across objects)
- Notification delivery (email, in-app, push) at journey milestones

## Decision Framework

| Signal | Decision |
|--------|----------|
| Journey stays within one cloud | System-level test — not E2E |
| Journey crosses two clouds | E2E with explicit boundary checks |
| Journey involves external system | E2E + integration stub/mock strategy |

## Best Practices

- Document journey as a numbered step sequence before writing scenarios
- Verify data at each cloud boundary — not just at journey end
- Include rollback / failure scenarios (what happens if approval is rejected mid-journey)
- Chain [TDG](../../test-data-generator/SKILL.md) for prerequisite data setup

## Anti-Patterns

- Testing each cloud segment independently without verifying the full journey
- Assuming data created in one cloud is immediately visible in another context
- Skipping failure/rollback paths in E2E journeys

## Related Documents

- [SKILL.md](../SKILL.md)
- [Cloud Testing Model](cloud-testing-model.md)
- [Test Data Generator](../../test-data-generator/SKILL.md)
