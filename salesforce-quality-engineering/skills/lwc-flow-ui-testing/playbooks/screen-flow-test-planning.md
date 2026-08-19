---
title: Screen Flow Test Planning
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

# Screen Flow Test Planning

## When to Use

Planning test coverage for a new or modified Screen Flow.

## Steps

1. **Map Flow screens** — List all screens, their input components, and required fields
2. **Document navigation paths** — Next, Back, Cancel, Resume, Finish for each screen
3. **Identify decisions** — Map each Decision element to expected screen routing
4. **Trace conditional visibility** — Components that show/hide based on prior selections
5. **Define fault paths** — DML errors, Apex exceptions, governor limits → fault screen behavior
6. **Test persona variations** — Profile-based record types, permission-controlled entry, FLS-hidden fields
7. **Validate data persistence** — Back navigation preserves data; Cancel discards
8. **Assess success screen** — Confirmation message, record link, post-flow redirect
9. **Draft test matrix** — Use [`templates/flow-ui-test-report.md`](../templates/flow-ui-test-report.md)
10. **Chain downstream** — PTA for persona coverage, TDG for test data, PWR for automation

## Quality Gates

- All screens and navigation paths documented
- Decision branches have at least one test scenario each
- Fault paths explicitly covered
- Persona variations identified (or marked N/A)

## Related Documents

- [SKILL.md](../SKILL.md)
- [Flow UI Testing Knowledge](../knowledge/flow-ui-testing.md)
