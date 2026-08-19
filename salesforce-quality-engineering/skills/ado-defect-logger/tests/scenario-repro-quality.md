---
title: "Test: Repro Steps Quality"
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, test, repro-quality]
---

# Test: Repro Steps Quality

## Purpose

Validate that generated repro steps are always numbered, atomic, and reproducible by another tester.

## Scenarios

### Scenario 1: Well-described defect

- **Input:** "When a Sales Rep creates an Opportunity with Stage = Closed Won and Amount > 100,000, the approval process doesn't trigger. Environment: QA sandbox, Chrome."
- **Expected repro steps format:**
  1. Log in to QA sandbox as Sales Rep profile user
  2. Navigate to Opportunities tab → click "New"
  3. Fill fields: Account = [test account], Stage = "Closed Won", Amount = 100,001, Close Date = today
  4. Click "Save"
  5. Observe that no approval request is generated (check Approval History related list)
- **Verify:** Steps are numbered, each is one action, includes specific data values, observation point explicit

### Scenario 2: Minimal input

- **Input:** "Approval process not working for large Opportunities"
- **Expected:** Skill asks for specifics before generating repro steps (does not invent steps)

### Scenario 3: Complex multi-step defect

- **Input:** Detailed defect involving 8+ steps
- **Expected:** All steps numbered sequentially, no steps combined, each step independently executable
- **Verify:** A tester unfamiliar with the defect could follow the steps

## Quality Checks

- [ ] Every repro step block uses numbered list (1. 2. 3.)
- [ ] No step contains multiple actions ("click Save and then navigate to...")
- [ ] Login/persona specified in step 1
- [ ] Navigation path explicit
- [ ] Test data values included
- [ ] Observation step present
- [ ] Expected and actual results stated separately from repro steps
