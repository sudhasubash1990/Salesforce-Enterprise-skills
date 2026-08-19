---
title: "Test: ADO Default Format"
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test Scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, test, default-format]
---

# Scenario: ADO Default Format

## Objective

Verify that when the user does not provide a custom template, the skill generates test cases in ADO-compatible format.

## Setup

**Input prompt:** "Generate test cases for the following requirement: FR-001 — Users can create Accounts with Name, Industry, and BillingAddress."

**No custom template provided.**

## Expected Behavior

1. Output uses ADO test case format with all fields from `SKILL.md > ADO Test Case Structure`
2. Each test case includes: Test Case ID, Title, Area Path, Iteration Path, Test Suite, Priority, Test Type, Tags, Requirement, Preconditions, Test Data, Test Steps (Step #, Action, Expected Result), Persona, Environment
3. Test Steps table has columns: Step #, Action, Expected Result
4. The 10-section output schema is followed

## Pass Criteria

- [ ] Test cases contain all required ADO fields
- [ ] Test Steps are in tabular format with Step #, Action, Expected Result
- [ ] No custom template format is used
- [ ] Output follows the 10-section schema
- [ ] Every Expected Result is specific and measurable

## Fail Criteria

- Test cases are in free-form text without ADO structure
- Any ADO field is missing from the output
- Expected results contain vague language
