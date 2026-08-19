---
title: Scenario — UAT Routing
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: test-scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, test, routing]
---

# Test Scenario — UAT Routing

## Objective

Verify that requests containing UAT/PO testing keywords are routed to the SPUAT skill.

## Test Cases

### TC-1: Direct UAT keyword

**Input:** "Plan UAT for the new billing process"
**Expected:** Routes to `salesforce-uat-po-testing/SKILL.md`
**Pass criteria:** SPUAT skill is loaded; output follows the 14-section schema

### TC-2: PO testing keyword

**Input:** "What should the Product Owner test for the approval workflow?"
**Expected:** Routes to SPUAT; applies the 12 PO questions
**Pass criteria:** PO questions are addressed in the output

### TC-3: Business sign-off keyword

**Input:** "Generate a Go/No-Go recommendation for the Service Cloud release"
**Expected:** Routes to SPUAT; produces sign-off recommendation
**Pass criteria:** Sign-off output uses the uat-signoff-template structure

### TC-4: Technical testing keyword (negative)

**Input:** "Write Apex unit tests for the discount trigger"
**Expected:** Does NOT route to SPUAT; routes to SFT or technical skill
**Pass criteria:** SPUAT is not activated

### TC-5: Ambiguous keyword

**Input:** "Test the case management process"
**Expected:** Routes to SPUAT if context is business validation; to SFT if context is technical
**Pass criteria:** Clarifying question asked if context is unclear
