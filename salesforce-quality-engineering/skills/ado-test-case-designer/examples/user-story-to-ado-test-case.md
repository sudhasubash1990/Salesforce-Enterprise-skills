---
title: "Example: User Story to ADO Test Case"
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, example, user-story]
---

# Example: User Story to ADO Test Case

## Input — User Story

**US-042:** Account Management — Update Customer Status

**As a** Customer Service Agent
**I want to** update the Account Status field to "Inactive" when a customer requests account closure
**So that** the account is excluded from active campaigns and billing processes

**Acceptance Criteria:**

- **AC1:** Given a Customer Service Agent on the Account record page, When they change Account Status to "Inactive" and click Save, Then the Account Status is updated to "Inactive", the Last Modified Date reflects the current timestamp, and a toast message "Account status updated successfully" is displayed.
- **AC2:** Given a Customer Service Agent attempts to set Account Status to "Inactive" on an Account with open Cases, Then a validation error is displayed: "Cannot deactivate account with open cases. Please resolve all open cases first."
- **AC3:** Given a Sales Representative, When they attempt to change Account Status to "Inactive", Then the action is blocked and an insufficient permissions error is displayed.

**Business Rules:**

- BRU-001: Accounts with open Opportunities (Stage ≠ Closed Won / Closed Lost) cannot be deactivated.
- BRU-002: Deactivation triggers a Flow that removes the Account from all active Campaign Members.

---

## Output — ADO Test Cases

### 1. Intent

Generate ADO test cases for Account Status deactivation workflow covering happy path, validation, permission, and automation scenarios.

### 2. Context

| Dimension | Value |
|-----------|-------|
| Salesforce Cloud | Sales Cloud + Service Cloud |
| Objects | Account, Case, Opportunity, CampaignMember |
| Personas | Customer Service Agent, Sales Representative |
| Environment | UAT |

### 3. Assumptions

- `[ASSUMPTION]` Account Status is a picklist field with values: Active, Inactive, Suspended
- `[ASSUMPTION]` Validation rule fires on before-save, not via Flow
- `[ASSUMPTION]` Campaign Member removal Flow is record-triggered (after save)

### 4. Requirement Analysis

| Requirement | Testable Conditions |
|-------------|-------------------|
| AC1 | Status changes to Inactive; Last Modified Date updates; toast displays |
| AC2 | Open Cases block deactivation; specific error message displayed |
| AC3 | Sales Rep profile lacks permission; error displayed |
| BRU-001 | Open Opportunities block deactivation |
| BRU-002 | Flow removes CampaignMembers after deactivation |

### 5. Test Design Approach

| Technique | Applied To |
|-----------|-----------|
| Use Case | E2E deactivation flow |
| Decision Table | Conditions: open Cases, open Opps, persona |
| State Transition | Account Status: Active → Inactive |
| Permission Matrix | Service Agent vs. Sales Rep |

### 6. ADO Test Cases

---

#### TC-001: Account Deactivation — Happy Path

**Area Path:** \Project\Account Management
**Iteration Path:** \Project\Sprint 5
**Test Suite:** Account Status Management
**Priority:** 1
**Test Type:** Functional
**Tags:** account; deactivation; happy-path
**Requirement:** US-042 / AC1
**Persona:** Customer Service Agent
**Environment:** UAT
**Business Criticality:** High

**Preconditions:**
- Logged in as Customer Service Agent
- Account "Acme Corp" exists with Status = "Active"
- No open Cases on the Account
- No open Opportunities on the Account

**Test Data:**

| Data Item | Value |
|-----------|-------|
| Account Name | Acme Corp |
| Current Status | Active |
| Target Status | Inactive |

**Test Steps:**

| Step # | Action | Expected Result |
|--------|--------|-----------------|
| 1 | Navigate to Account record "Acme Corp" | Account record page loads with Status field showing "Active" |
| 2 | Click the Account Status picklist and select "Inactive" | Picklist updates to "Inactive" (unsaved) |
| 3 | Click "Save" | Record saves successfully. Account Status = "Inactive". Last Modified Date = current date/time. Toast message displays: "Account status updated successfully" |

**Post Conditions:** Account Status = Inactive; Last Modified By = logged-in Agent

**Automation Candidate:** Yes — field update with assertion on toast and field values

---

#### TC-002: Account Deactivation — Blocked by Open Cases

**Priority:** 1
**Test Type:** Functional
**Tags:** account; deactivation; negative; validation
**Requirement:** US-042 / AC2
**Persona:** Customer Service Agent

**Preconditions:**
- Account "Beta Inc" has Status = "Active"
- Account has 1 open Case (Status = "New")

**Test Steps:**

| Step # | Action | Expected Result |
|--------|--------|-----------------|
| 1 | Navigate to Account record "Beta Inc" | Account page loads; Status = "Active" |
| 2 | Change Account Status to "Inactive" and click "Save" | Save is blocked. Validation error displayed: "Cannot deactivate account with open cases. Please resolve all open cases first." Account Status remains "Active" |

**Automation Candidate:** Yes — validation rule error assertion

---

#### TC-003: Account Deactivation — Blocked by Open Opportunities

**Priority:** 1
**Test Type:** Functional
**Tags:** account; deactivation; negative; business-rule
**Requirement:** US-042 / BRU-001
**Persona:** Customer Service Agent

**Preconditions:**
- Account "Gamma Ltd" has Status = "Active"
- Account has 1 open Opportunity (Stage = "Proposal")

**Test Steps:**

| Step # | Action | Expected Result |
|--------|--------|-----------------|
| 1 | Navigate to Account record "Gamma Ltd" | Account page loads; Status = "Active" |
| 2 | Change Account Status to "Inactive" and click "Save" | Save is blocked. Error message related to open Opportunities is displayed. Account Status remains "Active" |

---

#### TC-004: Account Deactivation — Insufficient Permissions (Sales Rep)

**Priority:** 1
**Test Type:** Security
**Tags:** account; deactivation; permission; negative
**Requirement:** US-042 / AC3
**Persona:** Sales Representative

**Preconditions:**
- Logged in as Sales Representative
- Account "Delta Co" has Status = "Active", no open Cases/Opps

**Test Steps:**

| Step # | Action | Expected Result |
|--------|--------|-----------------|
| 1 | Navigate to Account record "Delta Co" | Account page loads; Status = "Active" |
| 2 | Attempt to change Account Status to "Inactive" and click "Save" | Action is blocked. Insufficient permissions error is displayed. Account Status remains "Active" |

---

#### TC-005: Account Deactivation — Campaign Member Removal Flow

**Priority:** 2
**Test Type:** Integration
**Tags:** account; deactivation; flow; campaign
**Requirement:** US-042 / BRU-002
**Persona:** Customer Service Agent

**Preconditions:**
- Account "Epsilon Inc" has Status = "Active"
- Account has 2 Contacts who are active Campaign Members
- No open Cases or Opportunities

**Test Steps:**

| Step # | Action | Expected Result |
|--------|--------|-----------------|
| 1 | Note current CampaignMember records for Epsilon Inc Contacts | 2 CampaignMember records exist with Status = "Sent" |
| 2 | Change Account Status to "Inactive" and Save | Account Status = "Inactive". Save succeeds |
| 3 | Navigate to each Contact's Campaign History related list | CampaignMember records are removed (0 active campaign memberships) |

**Post Conditions:** No active CampaignMember records for Contacts under Epsilon Inc

---

### 7. Traceability Matrix

| Requirement | Business Rule | AC | Test Scenario | Test Case | Coverage |
|-------------|--------------|-----|---------------|-----------|----------|
| US-042 | — | AC1 | Happy path deactivation | TC-001 | Full |
| US-042 | — | AC2 | Open Cases block | TC-002 | Full |
| US-042 | — | AC3 | Permission block | TC-004 | Full |
| US-042 | BRU-001 | — | Open Opps block | TC-003 | Full |
| US-042 | BRU-002 | — | Campaign removal | TC-005 | Full |

### 8. Quality Gates

| Gate | Status |
|------|--------|
| Requirement understandable | Pass |
| AC available | Pass |
| Assumptions labeled | Pass (3 assumptions) |
| Test data identified | Pass |
| Persona identified | Pass (Service Agent, Sales Rep) |
| Expected results measurable | Pass |
| No vague expected results | Pass |

### 9. Dependencies

| Dependency | Type | Status |
|-----------|------|--------|
| Account Status validation rule deployed | Environment | Required before test |
| Campaign Member removal Flow deployed | Environment | Required for TC-005 |
| Sales Rep profile configured without Status edit | Security | Required for TC-004 |

### 10. Recommended Next Actions

- [ ] Deploy validation rule and Flow to UAT sandbox
- [ ] Create test data per preconditions (chain TDG skill)
- [ ] Execute TC-001 through TC-005
- [ ] Log defects for any failures (chain ADL skill)
- [ ] Consider boundary test: Account with exactly 0 vs. 1 open Case

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
