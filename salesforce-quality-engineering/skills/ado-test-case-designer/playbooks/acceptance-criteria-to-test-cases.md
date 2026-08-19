---
title: Acceptance Criteria to Test Cases Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, playbook, acceptance-criteria]
---

# Acceptance Criteria to Test Cases

## Purpose

Derive ADO test cases directly from Given/When/Then acceptance criteria.

## Prerequisites

- Acceptance criteria in Gherkin format (Given/When/Then)
- User story context (persona, business value)

## Steps

### Step 1 — Parse Acceptance Criteria

For each AC:
1. **Given** → Extract preconditions and test data setup
2. **When** → Extract test actions (user steps)
3. **Then** → Extract expected results (must be measurable)
4. **And** → Extract additional conditions or outcomes

### Step 2 — Expand Beyond AC

ACs define minimum acceptance — expand coverage:

1. **Negative path:** What happens when preconditions are NOT met?
2. **Boundary:** What are the edge values for any mentioned data?
3. **Permission:** What if a different persona attempts the action?
4. **Error handling:** What if the action fails (system error, validation)?

### Step 3 — Map to ADO Test Cases

| AC Component | ADO Test Case Field |
|-------------|-------------------|
| Given | Preconditions + Test Data |
| When | Test Steps → Action |
| Then / And | Test Steps → Expected Result |
| AC ID | Tags / linked requirement |

### Step 4 — Generate One TC Per AC (Minimum)

Each AC produces at least one test case. Complex ACs may produce multiple:

- 1 TC for the happy path (exact AC scenario)
- 1+ TCs for negative/boundary/permission variations

### Step 5 — Quality Gate

Verify every expected result is specific. Reject vague outcomes.

## Example

**AC:** Given a Sales Rep on the Account page, When they click "New Opportunity" and fill required fields (Name, Close Date, Stage), Then the Opportunity is created with Status = "Open" and Owner = the logged-in Sales Rep.

**Test Cases Generated:**

1. TC-001: Create Opportunity — happy path (all required fields valid)
2. TC-002: Create Opportunity — missing Close Date (validation error expected)
3. TC-003: Create Opportunity — Stage picklist values per record type
4. TC-004: Create Opportunity — Service Rep profile (insufficient permissions)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
