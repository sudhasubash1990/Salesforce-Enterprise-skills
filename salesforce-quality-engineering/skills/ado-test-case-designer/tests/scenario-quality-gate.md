---
title: "Test: Quality Gate — Vague Expected Results Rejected"
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test Scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, test, quality-gate]
---

# Scenario: Quality Gate — Vague Expected Results

## Objective

Verify that the skill never produces vague expected results and rejects/rewrites them.

## Banned Phrases

The following phrases must NEVER appear in any Expected Result field:

| Banned Phrase | Why |
|---------------|-----|
| "Verify it works" | Not measurable — what does "works" mean? |
| "Check functionality" | Not specific — which functionality, what outcome? |
| "Validate successfully" | Not observable — success must be defined |
| "Ensure correct behavior" | Not testable — "correct" is subjective |
| "Should work fine" | Not verifiable — no pass/fail criteria |
| "System behaves correctly" | Not measurable — no specific behavior stated |
| "Test the feature" | Action, not an expected result |
| "Verify the output" | Not specific — what output, what value? |

## Test Method

1. Provide a requirement with ambiguous acceptance criteria
2. Observe the generated test cases
3. Scan every Expected Result field for banned phrases

## Input

**Requirement:** "Users should be able to manage their Contacts."

_(Deliberately vague to test the skill's quality gate)_

## Expected Behavior

1. The skill flags the requirement as ambiguous
2. Assumptions are made and labeled with `[ASSUMPTION]`
3. Generated expected results are specific, e.g.:
   - "Contact record is created with First Name = 'John', Last Name = 'Doe', Account = 'Acme Corp'. Contact detail page displays all entered field values."
   - NOT: "Verify Contact is created successfully"

## Pass Criteria

- [ ] Zero banned phrases appear in any Expected Result
- [ ] Every Expected Result specifies observable system state, UI element, or data value
- [ ] Ambiguous input triggers assumption labeling
- [ ] Quality Gates section shows "Pass" for "No vague expected results"

## Fail Criteria

- Any banned phrase appears in an Expected Result field
- Expected results lack specific observable outcomes
