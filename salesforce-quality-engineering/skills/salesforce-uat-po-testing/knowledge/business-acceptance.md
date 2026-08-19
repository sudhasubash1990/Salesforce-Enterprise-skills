---
title: Business Acceptance Criteria Validation
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: knowledge
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, business-acceptance]
---

# Business Acceptance Criteria Validation

## Purpose

Guides the validation of business acceptance criteria during UAT — ensuring every AC is tested, traced to evidence, and signed off by the business owner.

## AC-to-Scenario Traceability

Every acceptance criterion must map to at least one UAT scenario:

| AC ID | Acceptance Criterion | UAT Scenario(s) | Evidence | Status |
|-------|----------------------|------------------|----------|--------|
| AC-001 | Given a sales rep, when they submit a discount > 20%, then the system blocks the submission | S-003: Discount cap enforcement | Screenshot of error | Passed |

- If an AC has no mapped scenario → gap
- If a scenario has no mapped AC → orphan (evaluate if needed or remove)

## Business Rule Testing

Business rules in Salesforce typically manifest as:

| Business Rule Type | Salesforce Mechanism | UAT Validation Approach |
|--------------------|----------------------|-------------------------|
| Approval thresholds | Approval Processes | Submit records at boundary values; confirm correct approver |
| Data validation | Validation Rules | Enter invalid data; confirm business-friendly error message |
| Escalation timing | Escalation Rules / Flows | Wait for SLA breach; confirm escalation occurs |
| Pricing / discount | Price Books / CPQ | Apply discounts at cap boundaries; verify enforcement |
| Routing / assignment | Assignment Rules / Flows | Create records; confirm correct owner / queue |
| Record access | Sharing Rules / OWD | Log in as each persona; confirm correct visibility |

### Testing approach

1. Identify all business rules from requirements / user stories
2. For each rule, create boundary-value scenarios (at, above, below threshold)
3. Include the "what if the rule doesn't fire" negative scenario
4. Record evidence of both pass and fail paths

## Persona-Based Business Testing

### Persona coverage matrix

| Persona | Business Process | Scenario Count | Coverage |
|---------|------------------|----------------|----------|
| Sales Rep | Opportunity creation, discount request | 5 | Covered |
| Sales Manager | Approval, pipeline review | 3 | Covered |
| Customer (Portal) | Case submission, knowledge search | 4 | Covered |
| Service Agent | Case management, escalation | 6 | Covered |
| Operations Manager | Reporting, bulk operations | 2 | Gap — add scenarios |

### Persona validation checklist

- [ ] Each persona can log in and access their expected landing page
- [ ] Each persona sees only the data they should see (no over-exposure)
- [ ] Each persona can complete their primary business process end-to-end
- [ ] Each persona receives appropriate notifications / alerts
- [ ] Each persona's experience matches the documented TO-BE process

## Negative and Exception Scenarios

For every happy-path scenario, ask:

- What if the user enters invalid data?
- What if a required field is missing?
- What if the user doesn't have permission?
- What if the upstream system is unavailable?
- What if the approval is rejected?
- What if the SLA is breached?

Frame exceptions in business language:
- "Customer submits a complaint without providing an order number — system prompts for required information"
- Not: "Validation rule VR_Order_Required fires on Case insert"

## Related

- [PO Testing Model](po-testing-model.md)
- [UAT Sign-off](uat-signoff.md)
