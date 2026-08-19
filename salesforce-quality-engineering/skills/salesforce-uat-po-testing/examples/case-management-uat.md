---
title: Case Management UAT Example
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, example, service-cloud]
---

# UAT Example — Case Management Business Process

## 1. Intent

Validate the end-to-end case management lifecycle from customer complaint submission through resolution and closure, ensuring service agents, supervisors, and customers experience the process correctly.

## 2. Context

| Attribute | Value |
|-----------|-------|
| Project | Service Transformation |
| Release | R1.0 |
| Salesforce Cloud | Service Cloud |
| Business Domain | Customer Service |

## 3. Assumptions

| ID | Assumption | Status |
|----|------------|--------|
| A1 | SLA targets: Priority cases resolved within 4 hours, standard within 24 hours | Confirmed |
| A2 | Escalation routes to the supervisor of the assigned agent's team | Open |
| A3 | Email-to-Case is enabled for the support inbox | Confirmed |

## 4. UAT Scope

**In scope:** Case creation (manual + email), assignment, escalation, resolution, closure, customer notification
**Out of scope:** Live chat, chatbot deflection (Phase 2), knowledge article management

## 5. Business Risk Assessment

| Feature | Risk | Impact | Priority |
|---------|------|--------|----------|
| Case assignment | Critical | Cases go unassigned; customers wait | Must test |
| SLA escalation | Critical | Breached SLAs damage customer satisfaction | Must test |
| Customer notification | High | Customer unaware of case progress | Must test |
| Case closure | Medium | Cases left open inflate backlog metrics | Should test |

## 7. Business Scenarios

### S-001: Customer Submits a Complaint via Email

| Field | Value |
|-------|-------|
| **Business Scenario** | Customer sends a complaint email to the support address; a case is automatically created and assigned to the correct team |
| **Business Objective** | Verify that customer complaints are captured without manual intervention |
| **Preconditions** | Email-to-Case is active; assignment rules are configured for the product category |
| **Business Steps** | 1. Customer sends email to support@company.com with complaint details 2. System creates a case from the email 3. Case is assigned to the appropriate team based on product category 4. Agent receives notification of the new case |
| **Expected Business Outcome** | Case created with correct details, assigned to the right team, agent notified |
| **Acceptance Criteria** | AC-001, AC-002 |
| **Business Risk** | Customer complaint lost or delayed; customer satisfaction drops |
| **Evidence Required** | Case record with email details, assignment confirmation, agent notification |
| **Business Owner** | Head of Customer Service |
| **UAT Status** | Not Started |

### S-002: Agent Resolves a Case and Customer Is Notified

| Field | Value |
|-------|-------|
| **Business Scenario** | Service agent investigates and resolves a customer complaint; customer receives a resolution notification |
| **Business Objective** | Verify the resolution workflow provides closure to the customer |
| **Preconditions** | Case is assigned to the agent; agent has investigated the issue |
| **Business Steps** | 1. Agent updates the case with resolution details 2. Agent changes case status to "Resolved" 3. Customer receives an email with the resolution summary 4. Case moves to "Closed" after 48 hours if customer doesn't reopen |
| **Expected Business Outcome** | Customer is informed of the resolution; case closes automatically after the feedback window |
| **Acceptance Criteria** | AC-005, AC-006 |
| **Business Risk** | Customer never hears back; reopened cases pile up |
| **Evidence Required** | Resolution email to customer, case status timeline, auto-close confirmation |
| **Business Owner** | Head of Customer Service |
| **UAT Status** | Not Started |

### S-003: SLA Breach Triggers Escalation

| Field | Value |
|-------|-------|
| **Business Scenario** | A priority case is not resolved within the 4-hour SLA; the system escalates to the team supervisor |
| **Business Objective** | Verify SLA enforcement protects service quality |
| **Preconditions** | Priority case created and assigned; 4-hour SLA clock running |
| **Business Steps** | 1. Priority case remains unresolved past 4 hours 2. System triggers escalation to team supervisor 3. Supervisor receives notification with case details and SLA status |
| **Expected Business Outcome** | Supervisor is alerted to the breach and can intervene |
| **Acceptance Criteria** | AC-003 |
| **Business Risk** | SLA breaches go unnoticed; repeat customer complaints |
| **Evidence Required** | Escalation notification, case ownership change or supervisor alert |
| **Business Owner** | Service Operations Manager |
| **UAT Status** | Not Started |

## 8. Acceptance Criteria Validation

| AC ID | Criterion | Scenario | Status |
|-------|-----------|----------|--------|
| AC-001 | Emails to support inbox create cases automatically | S-001 | Not Tested |
| AC-002 | Cases are assigned based on product category | S-001 | Not Tested |
| AC-003 | Priority cases breaching SLA escalate to supervisor | S-003 | Not Tested |
| AC-005 | Resolution notification sent to customer | S-002 | Not Tested |
| AC-006 | Cases auto-close 48 hours after resolution if not reopened | S-002 | Not Tested |

## 9. Persona Coverage

| Persona | Scenarios | Status |
|---------|-----------|--------|
| Customer | S-001, S-002 | Covered |
| Service Agent | S-001, S-002 | Covered |
| Team Supervisor | S-003 | Covered |
