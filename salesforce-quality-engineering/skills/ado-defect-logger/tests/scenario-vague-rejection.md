---
title: "Test: Vague Defect Rejection"
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, test, vague-rejection]
---

# Test: Vague Defect Rejection

## Purpose

Validate that the skill rejects vague defect descriptions and asks for evidence instead of inventing details.

## Scenarios

### Scenario 1: "Application is not working"

- **Input:** "Log a bug: Application is not working"
- **Expected:** Skill does NOT generate an ADO defect
- **Expected:** Skill asks: Which application? Which page? What error? What were you doing?
- **Anti-pattern check:** Skill does NOT invent repro steps or error messages

### Scenario 2: "Something is wrong"

- **Input:** "Create a defect — something is wrong with the Cases"
- **Expected:** Skill asks: What specifically is wrong? Which Case? What action? Expected vs actual?
- **Anti-pattern check:** Skill does NOT guess the defect details

### Scenario 3: "Flow failed"

- **Input:** "Log bug: Flow failed"
- **Expected:** Skill asks: Which Flow? What input data? What fault message? Which environment?
- **Anti-pattern check:** Skill does NOT assume a Flow name or error

### Scenario 4: "Page is broken"

- **Input:** "Page is broken, please log defect"
- **Expected:** Skill asks: Which page? Which component? What browser? Screenshot?

### Scenario 5: "It is slow"

- **Input:** "Log defect: it is slow"
- **Expected:** Skill asks: Which operation? How slow (seconds)? What is acceptable? When does it happen?

## Pass Criteria

- All five vague inputs are rejected with specific clarifying questions
- No defect is generated from vague input alone
- No details are invented or assumed
