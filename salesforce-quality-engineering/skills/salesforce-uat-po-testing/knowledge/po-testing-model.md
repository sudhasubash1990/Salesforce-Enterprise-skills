---
title: PO Testing Model
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: knowledge
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, po-testing-model]
---

# Product Owner Testing Model

## Purpose

Defines how the Product Owner lens is applied to Salesforce validation — focusing on business value, not technical correctness.

## PO vs. Technical Validation

| Dimension | PO / Business Validation | Technical Validation |
|-----------|--------------------------|----------------------|
| **Language** | Business terms, process names | API names, field names, code |
| **Focus** | Does it meet the business need? | Does it function correctly? |
| **Scenarios** | Real-world business journeys | Feature-level test cases |
| **Success measure** | Business outcome achieved | Test case passed |
| **Audience** | Business owners, POs, end users | Developers, QA engineers |
| **Defect framing** | Business impact description | Technical root cause |

## The 12 PO Questions Framework

These questions form the foundation of every PO testing engagement. They must be asked (or addressed) before generating any UAT output.

### Business Value Questions (1–3)

1. **What business problem does this feature solve?** — Prevents testing features that don't connect to business outcomes.
2. **Who are the primary business users / personas?** — Ensures every impacted role is represented in testing.
3. **What does the happy-path business process look like end-to-end?** — Establishes the core scenario before exploring exceptions.

### Business Rules Questions (4–6)

4. **What are the business rules that must be enforced?** — Drives rule-based validation (approvals, pricing, SLAs, escalations).
5. **What happens when a business exception occurs?** — Ensures negative paths reflect real business scenarios.
6. **What are the acceptance criteria from the business owner?** — Anchors every test case to a signable AC.

### Data and Integration Questions (7–9)

7. **What data does the business user need to see / enter?** — Identifies data validation, visibility, and quality needs.
8. **What downstream processes depend on this?** — Extends coverage to end-to-end journey impact.
9. **What regulatory or policy constraints apply?** — Triggers compliance-aware testing.

### Outcome and Governance Questions (10–12)

10. **How will the business measure success post-go-live?** — Connects UAT to business KPIs.
11. **What is the business risk if this doesn't work correctly?** — Prioritizes scenario severity.
12. **Who has authority to sign off on UAT completion?** — Establishes clear governance.

## Applying the PO Lens in Salesforce

### Sales Cloud examples

- PO asks: "Can the sales rep progress an opportunity through the approval process without getting stuck?"
- Not: "Does the Apex trigger fire on OpportunityLineItem insert?"

### Service Cloud examples

- PO asks: "When a customer calls with a complaint, can the agent find their case history and escalate correctly?"
- Not: "Does the Case assignment rule route to Queue X?"

### Experience Cloud examples

- PO asks: "Can the partner log in, see their opportunities, and submit a deal registration?"
- Not: "Does the Aura component render in the community page?"

## Business vs. Technical Defect Framing

| Business framing | Technical framing (avoid in UAT) |
|------------------|----------------------------------|
| "Customer cannot see their invoice history on the portal" | "LWC component query fails on Experience Cloud page" |
| "Approval request goes to the wrong manager" | "Approval process criteria evaluates incorrectly on custom field" |
| "Sales rep cannot discount beyond 20% as per policy" | "Validation rule VR_Discount_Cap does not fire" |

## Related

- [UAT Framework](uat-framework.md)
- [Business Acceptance](business-acceptance.md)
