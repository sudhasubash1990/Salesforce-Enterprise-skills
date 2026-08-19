---
title: Requirement-to-Test Traceability
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, traceability]
---

# Requirement-to-Test Traceability

Traceability model ensuring every requirement is covered by test cases and every test case links back to a business need.

## Traceability Chain

```
Requirement (BR-XXX / FR-XXX)
  └── Business Rule (BRU-XXX)
       └── Acceptance Criteria (AC-XXX)
            └── Test Scenario (TS-XXX)
                 └── ADO Test Case (TC-XXX)
                      └── Defect (DEF-XXX) — if found during execution
```

## Traceability Levels

| Level | Artifact | ID Pattern | Owner |
|-------|----------|------------|-------|
| L1 | Business Requirement | BR-001 | Business Analyst |
| L2 | Functional Requirement | FR-001 | Business Analyst |
| L3 | Business Rule | BRU-001 | Business Analyst |
| L4 | Acceptance Criteria | AC-001 | Product Owner / BA |
| L5 | Test Scenario | TS-001 | QE / Test Designer |
| L6 | ADO Test Case | TC-001 | QE / Test Designer |
| L7 | Defect | DEF-001 | QE / Tester |

## Coverage Analysis

### Forward Traceability (Requirement → Test)

Ensures every requirement has test coverage:

| Requirement | Business Rules | Acceptance Criteria | Test Scenarios | Test Cases | Coverage |
|-------------|---------------|--------------------:|----------------|------------|----------|
| BR-001 | BRU-001, BRU-002 | AC-001, AC-002 | TS-001, TS-002 | TC-001–TC-005 | Full |
| BR-002 | BRU-003 | AC-003 | — | — | **Gap** |

### Backward Traceability (Test → Requirement)

Ensures no orphan test cases exist:

| Test Case | Scenario | AC | Requirement | Status |
|-----------|----------|-----|-------------|--------|
| TC-001 | TS-001 | AC-001 | BR-001 | Linked |
| TC-010 | TS-008 | — | — | **Orphan** |

## ADO Implementation

### Link Types

| Link | From Work Item | To Work Item |
|------|---------------|--------------|
| Tests / Tested By | Test Case | User Story |
| Parent / Child | Epic → Feature → User Story | Hierarchy |
| Related | Test Case | Bug |

### Requirement-Based Test Suites

Create ADO test suites linked to requirements:

1. Create a **Requirement-Based Suite** in the test plan
2. Link to the User Story / Requirement work item
3. ADO auto-populates test cases linked via "Tests" relationship
4. Coverage reports show requirement-to-test mapping

## Traceability Rules

1. Every requirement must have ≥ 1 test case (forward coverage)
2. Every test case must link to ≥ 1 requirement (no orphans)
3. Coverage gaps must be flagged in the Traceability Matrix output section
4. Orphan test cases trigger a warning in the Quality Gates section
5. When requirements change, impacted test cases must be identified

## Gap Identification

Gaps are reported in the output Traceability Matrix:

- **Uncovered Requirements:** Requirements with no linked test cases
- **Partially Covered:** Requirements where not all ACs have test cases
- **Orphan Tests:** Test cases with no requirement linkage
- **Stale Tests:** Test cases linked to requirements that have been modified since last test update

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
