---
title: Salesforce User Story to Test Cases Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, playbook, user-story]
---

# Salesforce User Story to Test Cases

## Purpose

Decompose a complete Salesforce user story (with description, ACs, business rules, field requirements, object impact) into a comprehensive ADO test case suite.

## Prerequisites

- Complete user story with all 18 sections (per BA skill pack)
- Salesforce cloud/objects identified

## Steps

### Step 1 — Story Analysis

Extract from the user story:
1. **Persona** → test execution role
2. **Goal** → primary test scenario
3. **Business value** → criticality classification
4. **Description** → AS-IS/TO-BE for regression and new tests
5. **Acceptance criteria** → minimum test cases
6. **Business rules** → business rule test cases
7. **Field requirements** → field validation test cases
8. **Object impact** → CRUD test cases per object
9. **Security & permissions** → permission matrix test cases

### Step 2 — Test Case Categories

From a single user story, generate test cases in these categories:

| Category | Source Section | Priority |
|----------|--------------|----------|
| Functional (happy path) | AC + Description | P1 |
| Validation/Error | Business Rules + Field Requirements | P1 |
| Permission/Security | Security & Permissions | P1 |
| Boundary | Field Requirements | P2 |
| Integration | Dependencies | P2 |
| Regression | Description (AS-IS impact) | P2 |
| E2E | Description (TO-BE flow) | P2 |
| Data | Field Requirements + Object Impact | P3 |

### Step 3 — Salesforce Platform Test Cases

Based on object impact, generate platform-specific tests:

- **Flow tests** if automation is flow-based
- **Validation rule tests** if VRs are mentioned
- **Sharing tests** if OWD/sharing rules apply
- **Trigger tests** if Apex triggers are in scope
- **LWC tests** if UI components are involved

### Step 4 — Generate ADO Test Cases

Produce all test cases in ADO format with full traceability back to the user story sections.

### Step 5 — Traceability Matrix

Map each story section to the test cases derived from it.

### Step 6 — Quality Gate

Run all checks. Ensure no vague expected results.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
