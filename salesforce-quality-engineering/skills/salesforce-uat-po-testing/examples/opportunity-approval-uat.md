---
title: Opportunity Approval UAT Example
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, example, sales-cloud]
---

# PO UAT Example — Opportunity Approval Process

## 1. Intent

Validate that the new opportunity discount approval process works correctly for sales reps, sales managers, and VP-level approvers from a business perspective.

## 2. Context

| Attribute | Value |
|-----------|-------|
| Project | CRM Enhancement Phase 2 |
| Release | R2.3 |
| Salesforce Cloud | Sales Cloud |
| Business Domain | Sales Operations |

## 3. Assumptions

| ID | Assumption | Status |
|----|------------|--------|
| A1 | Discount thresholds are: 0–15% (auto-approve), 16–25% (manager), >25% (VP) | Confirmed |
| A2 | All approvers have email notifications enabled | Open |

## 4. UAT Scope

**In scope:** Discount approval workflow for standard opportunities
**Out of scope:** CPQ-driven quoting (separate release), partner-originated deals

## 5. Business Risk Assessment

| Feature | Risk | Impact | Priority |
|---------|------|--------|----------|
| Discount approval routing | Critical | Unapproved discounts erode margin | Must test |
| Approval notifications | High | Approvers miss requests, deals stall | Must test |
| Rejection workflow | Medium | Sales reps unclear on next steps | Should test |

## 6. Reasoning

Discount governance is a top-3 business priority. Incorrect routing could result in margin erosion or deal delays. All three approval tiers must be validated with boundary values.

## 7. Business Scenarios

### S-001: Sales Rep Submits Discount Within Auto-Approve Range

| Field | Value |
|-------|-------|
| **Business Scenario** | Sales rep applies a 10% discount to an opportunity and submits for approval |
| **Business Objective** | Verify low-value discounts are auto-approved without delay |
| **Preconditions** | Opportunity exists with line items; sales rep is the opportunity owner |
| **Business Steps** | 1. Sales rep opens the opportunity 2. Applies a 10% discount 3. Submits for approval |
| **Expected Business Outcome** | Discount is automatically approved; opportunity stage advances; no manager intervention required |
| **Acceptance Criteria** | AC-001 |
| **Business Risk** | Low discounts being delayed unnecessarily slows deal closure |
| **Evidence Required** | Screenshot of approved status, opportunity stage change |
| **Business Owner** | Sales Operations Manager |
| **UAT Status** | Not Started |

### S-002: Manager Approval for Mid-Range Discount

| Field | Value |
|-------|-------|
| **Business Scenario** | Sales rep applies an 18% discount; sales manager reviews and approves |
| **Business Objective** | Verify manager-level approval is correctly routed and processed |
| **Preconditions** | Opportunity with 18% discount submitted; manager is in the role hierarchy |
| **Business Steps** | 1. Sales rep submits 18% discount 2. Sales manager receives approval notification 3. Manager reviews and approves 4. Sales rep sees approved discount |
| **Expected Business Outcome** | Manager receives notification, approves, and the opportunity reflects the approved discount |
| **Acceptance Criteria** | AC-002, AC-003 |
| **Business Risk** | Approval goes to wrong manager; deal delayed |
| **Evidence Required** | Approval notification screenshot, approval history, opportunity update |
| **Business Owner** | VP of Sales |
| **UAT Status** | Not Started |

### S-003: Manager Rejects Discount Request

| Field | Value |
|-------|-------|
| **Business Scenario** | Sales manager rejects a discount request; sales rep is notified with the reason |
| **Business Objective** | Verify rejection workflow provides clear feedback to the sales rep |
| **Preconditions** | Discount request submitted and pending manager approval |
| **Business Steps** | 1. Manager opens the approval request 2. Rejects with a reason ("Margin too thin for this account tier") 3. Sales rep receives rejection notification with reason |
| **Expected Business Outcome** | Sales rep sees rejection reason and can revise the discount |
| **Acceptance Criteria** | AC-004 |
| **Business Risk** | Sales rep doesn't know why the request was rejected; wastes time |
| **Evidence Required** | Rejection notification with reason text |
| **Business Owner** | Sales Operations Manager |
| **UAT Status** | Not Started |

## 8. Acceptance Criteria Validation

| AC ID | Criterion | Scenario | Status |
|-------|-----------|----------|--------|
| AC-001 | Discounts ≤15% are auto-approved | S-001 | Not Tested |
| AC-002 | Discounts 16–25% route to direct manager | S-002 | Not Tested |
| AC-003 | Approver receives email notification | S-002 | Not Tested |
| AC-004 | Rejection includes reason visible to submitter | S-003 | Not Tested |

## 9. Persona Coverage

| Persona | Scenarios | Status |
|---------|-----------|--------|
| Sales Rep | S-001, S-003 | Covered |
| Sales Manager | S-002, S-003 | Covered |
| VP | — | Gap — add >25% scenario |

## 10–14

*(Sections 10–14 follow the UAT Test Report template structure.)*
