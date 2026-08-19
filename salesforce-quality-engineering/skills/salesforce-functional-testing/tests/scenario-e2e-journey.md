---
title: E2E Journey Test
module: Salesforce Quality Engineering
category: QE Specialized Skill Test Scenario
document_type: Test Scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, test-scenario]
---

# E2E Journey Test

## Objective

Verify that cross-cloud E2E journey prompts produce journey-level scenarios with cloud boundary verification, persona transitions, and failure paths.

## Pass Criteria

- Journey documented as numbered steps with cloud annotations
- Data consistency checks defined at each cloud boundary
- Persona transitions explicitly mapped per step
- Failure / rollback path included (e.g., approval rejection mid-journey)
- TDG chained for prerequisite data setup

## Fail Criteria

- Journey tested as isolated cloud segments without end-to-end verification
- Cloud boundary data consistency not verified
- Only happy path covered — no failure/rollback scenario
- Shared objects (Account, Contact) not verified across cloud contexts
