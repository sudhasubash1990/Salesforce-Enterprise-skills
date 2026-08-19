---
title: Flow Negative Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [lwc-flow-ui-testing, playbook]
---

# Flow Negative Testing

## When to Use

Designing negative and fault-path test scenarios for Screen Flows.

## Steps

1. **Identify fault connectors** — Map every Fault path in the Flow diagram
2. **Test required field bypass** — Attempt Next without completing required fields
3. **Trigger DML failures** — Duplicate record, validation rule violation, required field missing on save
4. **Trigger Apex exceptions** — Invocable action throws exception → fault screen behavior
5. **Test governor limits** — Large data set operations within Flow → timeout/limit error handling
6. **Validate error messages** — User-friendly, actionable, no technical stack traces exposed
7. **Test retry behavior** — Can user retry from fault screen or must restart?
8. **Test cancel during error** — Cancel from fault screen exits cleanly
9. **Test concurrent access** — Two users modify same record via Flow simultaneously
10. **Document edge cases** — Boundary values, special characters, maximum field lengths

## Error Message Quality Checklist

- [ ] Error message is user-readable (no exception class names)
- [ ] Error provides guidance on next action
- [ ] Error is accessible (announced by screen reader)
- [ ] Retry or Back option available from error state

## Related Documents

- [SKILL.md](../SKILL.md)
- [Flow UI Testing Knowledge](../knowledge/flow-ui-testing.md)
