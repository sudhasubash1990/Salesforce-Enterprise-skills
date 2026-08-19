---
title: Scenario — PO Perspective
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: test-scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, test, po-perspective]
---

# Test Scenario — PO Perspective Enforcement

## Objective

Verify that SPUAT output adopts the Product Owner / business perspective, not a technical QA perspective.

## Test Cases

### TC-1: Scenario framing

**Input:** "Generate UAT scenarios for the opportunity approval process"
**Expected:** Scenarios describe what the sales rep / manager does in business terms
**Pass criteria:**
- Steps say "Sales rep submits discount for approval" not "User clicks Submit button on Opportunity record"
- Expected outcome says "Discount is approved and opportunity advances" not "Approval process fires and updates Status__c field"

### TC-2: 12 PO questions applied

**Input:** "Create PO test cases for the new case escalation feature"
**Expected:** Output addresses or references the 12 PO questions
**Pass criteria:** At minimum, business problem, personas, happy path, business rules, and sign-off authority are addressed

### TC-3: Risk framing

**Input:** "Assess business risk for the customer portal UAT"
**Expected:** Risks described in business impact terms
**Pass criteria:**
- Risk says "Customer sees another customer's data" not "Sharing rule misconfigured on Account object"
- No technical root cause analysis in the risk description

### TC-4: No invented metrics

**Input:** "Provide a UAT readiness assessment"
**Expected:** Assessment is evidence-based
**Pass criteria:** No fabricated percentages like "92% ready" or "Expected 95% pass rate"
