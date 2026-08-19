---
title: Requirement to ADO Test Case Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, playbook, requirement-to-test]
---

# Requirement to ADO Test Case

## Purpose

Convert a business or functional requirement into one or more ADO-compatible test cases with full traceability.

## Prerequisites

- Requirement text (BR-XXX or FR-XXX) with clear scope
- Acceptance criteria (or explicit assumptions if missing)
- Target Salesforce objects/features identified

## Steps

### Step 1 — Analyze Requirement

1. Read the requirement and identify testable conditions
2. Extract business rules, constraints, and expected behaviors
3. Identify personas involved
4. Identify Salesforce objects, fields, and features impacted

### Step 2 — Identify Test Scenarios

1. Derive positive scenarios (happy path)
2. Derive negative scenarios (invalid input, unauthorized access)
3. Derive boundary scenarios (field limits, date ranges)
4. Derive permission scenarios (profile/PS-based access)
5. Derive integration scenarios if applicable

### Step 3 — Apply Test Design Techniques

Select techniques based on requirement type:

| Requirement Type | Primary Technique | Secondary |
|-----------------|-------------------|-----------|
| Field validation | Boundary Value + Equivalence Partitioning | Error Guessing |
| Business process | State Transition + Use Case | Decision Table |
| Multi-condition logic | Decision Table | Pairwise |
| Security/access | Permission matrix | Persona-based |

### Step 4 — Generate ADO Test Cases

For each test scenario, produce an ADO test case with all fields from `SKILL.md > ADO Test Case Structure`.

**Critical rules:**
- Every expected result must be specific and measurable
- Never write "Verify it works" — specify the exact observable outcome
- Include preconditions, test data, and post conditions

### Step 5 — Build Traceability Matrix

Map: Requirement → Business Rule → AC → Test Scenario → Test Case

### Step 6 — Quality Gate Review

Run all quality gate checks from `SKILL.md > Quality Gate` before finalizing.

### Step 7 — Output

Generate the 10-section output per `SKILL.md > Output Schema`.

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
