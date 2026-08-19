---
title: Salesforce E2E Test Planning
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, e2e-test-planning]
---

# Salesforce E2E Test Planning

## Objective

Design and plan cross-cloud end-to-end journey tests that validate business processes spanning Service Cloud, Sales Cloud, and Experience Cloud.

## Inputs

- Business process map with cloud touchpoints
- E2E journey definitions (start event → steps → end state)
- Persona transitions across journey steps
- Shared object model (Account, Contact across clouds)
- Prerequisite data requirements

## Validation Workflow

1. Document each E2E journey as numbered steps with cloud annotations
2. Identify cloud boundary transitions and shared object verification points
3. Map persona transitions per journey step
4. Define prerequisite data — chain [TDG](../../test-data-generator/SKILL.md)
5. Design positive path, failure path, and rollback scenarios
6. Verify data consistency at each cloud boundary
7. Include timing-sensitive steps (SLA, escalation) with expected behavior

## Decision Points

| Decision | Criteria |
|----------|----------|
| Journey scope | Two or more clouds = E2E; single cloud = system test |
| External system mock | Integration point in journey = define stub strategy |
| Persona transition | Different user acts at different steps = explicit handoff test |
| Failure / rollback | Approval rejection or system error mid-journey |

## Expected Results

- Each journey completes end-to-end with correct data at every step
- Shared objects (Account, Contact) are consistent across cloud contexts
- Persona transitions preserve expected record access and visibility
- Failure paths produce defined rollback behavior — not orphaned records

## Anti-Patterns

- Testing cloud segments independently without full journey verification
- Skipping data consistency checks at cloud boundaries
- Assuming real-time sync between clouds without verifying

## Related Documents

- [E2E Testing Knowledge](../knowledge/salesforce-e2e-testing.md)
- [SKILL.md](../SKILL.md)
