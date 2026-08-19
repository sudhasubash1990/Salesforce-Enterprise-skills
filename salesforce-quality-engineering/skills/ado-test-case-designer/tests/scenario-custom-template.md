---
title: "Test: Custom Template Override"
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test Scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, test, custom-template]
---

# Scenario: Custom Template Override

## Objective

Verify that when the user provides a custom template, the skill uses the user's template instead of ADO default format.

## Setup

**Input prompt:**
> Generate test cases for Contact creation. Use this template:
>
> ```
> TC-ID: [ID]
> Feature: [Feature]
> Description: [What is tested]
> Pre-conditions: [Setup]
> Steps:
>   1. [Do X] → [Expect Y]
> Result: [Pass/Fail]
> ```

## Expected Behavior

1. Output uses the user's template structure — NOT ADO format
2. Fields match the user's template naming (TC-ID, Feature, Description, Pre-conditions, Steps, Result)
3. Quality rules still enforced: expected outcomes are measurable, not vague
4. Traceability section is still included in the report (even if not in the user's template)

## Pass Criteria

- [ ] Output matches user's template structure
- [ ] ADO-specific fields (Area Path, Iteration Path, etc.) are NOT present in test cases
- [ ] Expected outcomes in Steps are specific and measurable
- [ ] Traceability matrix is still generated as a separate section
- [ ] Assumptions are labeled with `[ASSUMPTION]`

## Fail Criteria

- Output uses ADO format despite user providing a custom template
- Vague expected results appear in the output
- Traceability is dropped entirely
