---
title: Sales Cloud Opportunity Approval — Example
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, sales-cloud-opportunity-approval]
---

# Sales Cloud Opportunity Approval

## Business Scenario

Opportunities exceeding a discount threshold require manager approval before advancing to Close-Won. The approval process locks the record, notifies the approver, and updates the stage upon approval or rejection.

## Cloud

Sales Cloud

## Objects

Opportunity, OpportunityLineItem, Product2, PricebookEntry, ProcessInstanceStep

## Test Scenarios

### Positive

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| OA-P01 | Submit opportunity with discount > 20% for approval | Record locked, approval request sent to manager |
| OA-P02 | Manager approves opportunity | Stage advances to Close-Won, record unlocked |
| OA-P03 | Opportunity below threshold — no approval needed | Stage advances directly without approval submission |

### Negative

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| OA-N01 | Manager rejects approval | Stage reverts to Negotiation, rejection comment saved |
| OA-N02 | Rep edits locked record during pending approval | Edit blocked with lock message |
| OA-N03 | Submit approval without required Discount Justification field | Validation error, submission blocked |

### Boundary

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| OA-B01 | Discount at exactly 20% threshold | Approval triggered (boundary inclusive) |
| OA-B02 | Discount at 19.99% | No approval required |

### Permission

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| OA-PM01 | Non-manager attempts to approve | Approve action not available |

## Expected Results

Approval chain, record lock state, and stage transitions verified at each step.

## Chain Skills

- [SOVA](../../soql-validation-assistant/SKILL.md) — verify ProcessInstanceStep records
- [PTA](../../permission-testing-agent/SKILL.md) — approver permission validation

## Related Documents

- [Sales Cloud Testing Knowledge](../knowledge/sales-cloud-testing.md)
- [SKILL.md](../SKILL.md)
