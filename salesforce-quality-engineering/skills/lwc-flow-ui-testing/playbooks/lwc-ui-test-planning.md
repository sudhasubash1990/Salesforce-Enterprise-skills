---
title: LWC UI Test Planning
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

# LWC UI Test Planning

## When to Use

Planning test coverage for a new or modified Lightning Web Component.

## Steps

1. **Identify component metadata** — API name, public properties (`@api`), wire adapters, events dispatched/handled, child components
2. **Map rendering paths** — Conditional rendering (`lwc:if`), dynamic components, loading/empty/error states
3. **List interactions** — Input fields, buttons, inline edit, dropdowns, modals, toasts
4. **Define validation scenarios** — Required fields, format validation, custom validity, server-side errors
5. **Assess communication** — Parent-child via `@api`/events, cross-component via Lightning Message Service
6. **Evaluate accessibility** — Keyboard traversal, screen reader labels, focus management, ARIA
7. **Determine locator strategy** — Semantic roles/labels preferred; document test IDs needed
8. **Identify data dependencies** — Chain TDG for test record setup
9. **Draft test scenarios** — Use [`templates/lwc-test-report.md`](../templates/lwc-test-report.md)
10. **Chain downstream** — PWR for Playwright automation, PTA for persona paths

## Quality Gates

- All rendering paths (conditional, dynamic, empty, error) covered
- Interaction scenarios include happy + negative paths
- Locator strategy documented — no brittle XPath
- Accessibility scenarios present

## Related Documents

- [SKILL.md](../SKILL.md)
- [LWC UI Testing Knowledge](../knowledge/lwc-ui-testing.md)
