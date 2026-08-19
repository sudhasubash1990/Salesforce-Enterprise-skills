---
title: Scenario — Business Language
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: test-scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, test, business-language]
---

# Test Scenario — Business Language Enforcement

## Objective

Verify that SPUAT outputs use business language exclusively — no technical QA jargon, no Apex/API references, no developer terms.

## Test Cases

### TC-1: No technical object names

**Input:** "Generate UAT test cases for case management"
**Expected:** Test cases reference "customer complaint" and "support request", not "Case object" or "CaseComment record"
**Pass criteria:** Scan output for Salesforce API names (Case__c, Account.Name, etc.) — none present

### TC-2: No developer terms in steps

**Input:** "Create UAT scenarios for the approval workflow"
**Expected:** Steps say "Manager reviews and approves the discount request" not "Approver clicks Approve on ApprovalProcess"
**Pass criteria:** No references to: Apex, trigger, Flow, Process Builder, Validation Rule, SOQL, API, field API name

### TC-3: Defect description in business terms

**Input:** "Help me triage this UAT defect: the approval email didn't arrive"
**Expected:** Defect framed as "Approver did not receive the discount approval request notification"
**Pass criteria:** Not framed as "EmailAlert on Approval Process did not fire"

### TC-4: Exception scenarios in business terms

**Input:** "What negative scenarios should we test for the portal?"
**Expected:** Exceptions like "Customer tries to view another customer's information" not "Guest user bypasses OWD restriction"
**Pass criteria:** All exception descriptions are understandable by a non-technical business user
