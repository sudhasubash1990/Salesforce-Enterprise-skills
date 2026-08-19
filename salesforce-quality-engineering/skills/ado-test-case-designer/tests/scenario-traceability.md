---
title: "Test: Traceability Chain Maintained"
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test Scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, test, traceability]
---

# Scenario: Traceability Chain Maintained

## Objective

Verify that every generated test case maintains the full traceability chain: Requirement → Business Rule → AC → Test Scenario → ADO Test Case.

## Setup

**Input:** User story with 3 ACs and 2 business rules.

**US-099:** Opportunity Management — Stage Progression

- **AC1:** Given a Sales Rep, When they move Opportunity from "Prospecting" to "Qualification", Then Stage = "Qualification" and Close Date is required.
- **AC2:** Given a Sales Rep, When they move to "Closed Won", Then Amount must be > 0 and Close Date ≤ today.
- **AC3:** Given a Sales Manager, When they view the Opportunity, Then they can see all stages including "Closed Won".
- **BRU-001:** Opportunities cannot skip stages (must follow defined sequence).
- **BRU-002:** "Closed Won" triggers revenue recognition Flow.

## Expected Behavior

1. Traceability Matrix section is present in output
2. Every AC (AC1, AC2, AC3) has at least one test case
3. Every BRU (BRU-001, BRU-002) has at least one test case
4. Every test case has a Requirement/User Story field populated
5. No orphan test cases (all linked)
6. Coverage status shows "Full" for all requirements

## Pass Criteria

- [ ] Traceability Matrix contains all 3 ACs and 2 BRUs
- [ ] Each AC maps to ≥ 1 test case
- [ ] Each BRU maps to ≥ 1 test case
- [ ] No "Gap" entries in the coverage column
- [ ] No "Orphan" entries in backward traceability
- [ ] Test case Requirement field = US-099 for all TCs
- [ ] Backward traceability (TC → Requirement) is complete

## Fail Criteria

- Any AC or BRU has no linked test case
- Traceability Matrix section is missing
- Orphan test cases exist
- Coverage column shows "Gap" for any requirement
