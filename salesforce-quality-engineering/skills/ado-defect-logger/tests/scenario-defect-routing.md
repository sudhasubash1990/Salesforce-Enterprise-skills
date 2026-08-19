---
title: "Test: Defect Routing"
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, test, routing]
---

# Test: Defect Routing

## Purpose

Validate that defect-related keywords correctly route to the ADO Defect Logger skill.

## Scenarios

### Scenario 1: Direct defect keyword

- **Input:** "Log a defect for a Flow failure in Service Cloud"
- **Expected:** Routes to `ado-defect-logger/SKILL.md`
- **Verify:** Skill loads and produces 9-section output

### Scenario 2: Bug keyword

- **Input:** "Create an ADO bug for this Apex exception"
- **Expected:** Routes to `ado-defect-logger/SKILL.md`
- **Verify:** Skill loads; does NOT create in ADO unless explicitly confirmed

### Scenario 3: Severity/priority keyword

- **Input:** "What severity should this integration timeout be?"
- **Expected:** Routes to `ado-defect-logger/SKILL.md`, loads `knowledge/severity-priority-model.md`
- **Verify:** Provides severity assessment with justification

### Scenario 4: Non-defect keyword (negative test)

- **Input:** "Create a test case for Account creation"
- **Expected:** Does NOT route to ADO Defect Logger; routes to ADO Test Case Designer
- **Verify:** Different skill activated

## Pass Criteria

All four scenarios route (or do not route) as expected.
