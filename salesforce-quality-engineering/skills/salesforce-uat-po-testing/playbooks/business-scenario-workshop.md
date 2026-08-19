---
title: Business Scenario Workshop Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-uat-po-testing, scenario-workshop]
---

# Business Scenario Workshop Playbook

## When to Use

When collaborating with business users and Product Owners to identify, validate, and prioritize UAT scenarios.

## Inputs

- UAT scope and in-scope features
- Acceptance criteria from user stories
- Business process maps (AS-IS / TO-BE)
- Persona list

## Steps

### Step 1 — Set the Stage (10 min)

1. Explain the purpose: "We're identifying real-world business scenarios to test, not technical test cases"
2. Clarify: scenarios should be in the language of the business user
3. Introduce the PO-friendly format (Business Scenario, Objective, Steps, Expected Outcome)

### Step 2 — Walk Through Each Business Process (30 min per process)

For each in-scope business process:

1. Ask the PO: "Walk me through how this works in your day-to-day"
2. Capture the happy-path scenario in business language
3. Ask: "What can go wrong?" — capture exception scenarios
4. Ask: "What business rules must be enforced?" — capture rule validation scenarios
5. Ask: "Who else is involved in this process?" — ensure persona coverage

### Step 3 — Prioritize Scenarios (15 min)

1. Classify each scenario by business risk: Critical / High / Medium / Low
2. Mark must-test scenarios (Critical + High) vs. nice-to-test (Medium + Low)
3. Confirm with PO: "If we can only test 10 scenarios, which are the non-negotiables?"

### Step 4 — Map Scenarios to Acceptance Criteria (15 min)

1. For each scenario, link to the AC it validates
2. Identify any AC without a corresponding scenario (gap)
3. Identify any scenario without a corresponding AC (validate if needed)

### Step 5 — Review and Confirm (10 min)

1. Read back scenarios to participants for accuracy
2. Confirm business owners for each scenario area
3. Agree on evidence requirements (screenshots, data checks, sign-off)

## Outputs

- Prioritized business scenario list in PO-friendly format
- AC-to-scenario traceability matrix
- Persona coverage matrix
- Open questions and assumptions log

## Tips

- Keep the language non-technical — if a developer term slips in, rephrase it
- Use real examples from the business user's daily work
- Don't try to cover everything — focus on business-critical paths first
- Record the workshop for reference
