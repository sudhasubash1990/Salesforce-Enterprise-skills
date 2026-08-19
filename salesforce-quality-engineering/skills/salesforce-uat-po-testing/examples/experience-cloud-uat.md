---
title: Experience Cloud UAT Example
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, example, experience-cloud]
---

# UAT Example — Customer Portal (Experience Cloud)

## 1. Intent

Validate that the customer self-service portal allows customers to view their account information, submit and track support cases, and access knowledge articles — all without needing to call the support line.

## 2. Context

| Attribute | Value |
|-----------|-------|
| Project | Digital Self-Service |
| Release | R1.0 |
| Salesforce Cloud | Experience Cloud + Service Cloud |
| Business Domain | Customer Self-Service |

## 3. Assumptions

| ID | Assumption | Status |
|----|------------|--------|
| A1 | Customers receive portal login credentials via welcome email | Confirmed |
| A2 | Customers can only see their own cases and account data | Confirmed |
| A3 | Knowledge articles are published and categorized by product | Open |

## 5. Business Risk Assessment

| Feature | Risk | Impact | Priority |
|---------|------|--------|----------|
| Customer login and access | Critical | Customers locked out; calls increase | Must test |
| Data visibility (own data only) | Critical | Data exposure; compliance risk | Must test |
| Case submission from portal | High | Customers can't get help via self-service | Must test |
| Knowledge article search | Medium | Deflection rate drops; call volume stays high | Should test |

## 7. Business Scenarios

### S-001: Customer Logs In and Views Account Dashboard

| Field | Value |
|-------|-------|
| **Business Scenario** | Customer logs into the portal and sees their account summary, open cases, and recent invoices |
| **Business Objective** | Verify customers can self-serve for account information |
| **Preconditions** | Customer has active portal credentials; account has recent activity |
| **Business Steps** | 1. Customer navigates to the portal URL 2. Enters login credentials 3. Sees the account dashboard with summary, cases, and invoices |
| **Expected Business Outcome** | Customer sees only their own data; dashboard loads with accurate information |
| **Acceptance Criteria** | AC-001, AC-002 |
| **Business Risk** | Customer sees another customer's data (compliance breach) |
| **Evidence Required** | Dashboard screenshot showing correct customer data, no cross-account exposure |
| **Business Owner** | Digital Experience Manager |
| **UAT Status** | Not Started |

### S-002: Customer Submits a Support Case from the Portal

| Field | Value |
|-------|-------|
| **Business Scenario** | Customer creates a new support case through the portal, receives confirmation, and can track its progress |
| **Business Objective** | Enable self-service case submission to reduce call volume |
| **Preconditions** | Customer is logged into the portal |
| **Business Steps** | 1. Customer clicks "Submit a Request" 2. Fills in the case details (category, description, urgency) 3. Submits the case 4. Sees confirmation with case number 5. Can track case status on the dashboard |
| **Expected Business Outcome** | Case is created in Salesforce, assigned to the correct team, and visible on the customer's portal dashboard |
| **Acceptance Criteria** | AC-003, AC-004 |
| **Business Risk** | Cases submitted via portal are lost or not routed correctly |
| **Evidence Required** | Case confirmation screen, case visible in agent console, portal dashboard showing case |
| **Business Owner** | Digital Experience Manager |
| **UAT Status** | Not Started |

### S-003: Customer Searches Knowledge Articles

| Field | Value |
|-------|-------|
| **Business Scenario** | Customer searches for help articles before submitting a case; finds relevant content |
| **Business Objective** | Deflect support cases through self-service knowledge |
| **Preconditions** | Knowledge articles are published for the customer's product category |
| **Business Steps** | 1. Customer searches for "reset password" in the portal 2. Sees relevant knowledge articles 3. Opens an article and follows the instructions |
| **Expected Business Outcome** | Customer finds the answer without submitting a case |
| **Acceptance Criteria** | AC-005 |
| **Business Risk** | Knowledge search returns irrelevant results; deflection fails |
| **Evidence Required** | Search results screenshot, article content |
| **Business Owner** | Knowledge Manager |
| **UAT Status** | Not Started |

### S-004: Customer Cannot See Another Customer's Data

| Field | Value |
|-------|-------|
| **Business Scenario** | Customer attempts to access data belonging to another customer; system blocks access |
| **Business Objective** | Verify data isolation and compliance |
| **Preconditions** | Two customer accounts exist with separate portal users |
| **Business Steps** | 1. Customer A logs in 2. Attempts to navigate to Customer B's case or account (URL manipulation) 3. System denies access |
| **Expected Business Outcome** | Access denied; no data from other customers visible |
| **Acceptance Criteria** | AC-002 |
| **Business Risk** | Data breach; regulatory non-compliance |
| **Evidence Required** | Access denied screen or redirect, no cross-account data displayed |
| **Business Owner** | Information Security Officer |
| **UAT Status** | Not Started |

## 8. Acceptance Criteria Validation

| AC ID | Criterion | Scenario | Status |
|-------|-----------|----------|--------|
| AC-001 | Customer sees their account dashboard after login | S-001 | Not Tested |
| AC-002 | Customer can only see their own data | S-001, S-004 | Not Tested |
| AC-003 | Customer can submit a case from the portal | S-002 | Not Tested |
| AC-004 | Submitted cases appear on the customer's dashboard | S-002 | Not Tested |
| AC-005 | Knowledge search returns relevant articles | S-003 | Not Tested |

## 9. Persona Coverage

| Persona | Scenarios | Status |
|---------|-----------|--------|
| Customer (portal user) | S-001, S-002, S-003, S-004 | Covered |
| Service Agent (backend) | S-002 (verify case appears) | Covered |
