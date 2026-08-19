---
title: Lightning DOM Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [lwc-flow-ui-testing, knowledge]
---

# Lightning DOM Testing

## Purpose

Understand Lightning DOM, Shadow DOM, dynamic rendering, async UI, console navigation, and iframes for accurate UI test design.

## Shadow DOM

- LWC uses **synthetic shadow** (default) or **native shadow** — locator strategy differs
- Synthetic shadow: standard CSS selectors may reach internal elements
- Native shadow: requires `pierce` selectors or component-exposed public APIs
- Always prefer semantic locators (`getByRole`, `getByLabel`) over shadow-piercing CSS
- Test assumption: validate which shadow mode the org/component uses

## Dynamic Rendering

| Pattern | Implication |
|---------|------------|
| `if:true` / `lwc:if` | DOM element is added/removed — assert existence, not visibility |
| `for:each` / `iterator` | List rendering — validate item count, order, empty state |
| `lwc:component` | Dynamic instantiation — verify correct component type loads |
| Slot composition | Parent provides content to child slot — assert slot content renders |

## Async UI Updates

| Trigger | Wait Strategy |
|---------|---------------|
| `@wire` data refresh | Wait for data-bound element to update |
| Imperative Apex call | Wait for promise resolution → UI re-render |
| Platform event | Wait for subscription handler → DOM update |
| `refreshApex()` | Wait for loading indicator to clear |
| `NavigationMixin` | Wait for URL/page change |

**HARD RULE:** Never use `waitForTimeout()` as primary sync. Use condition-based waits: element visible, text content matches, spinner disappears.

## Console Navigation

- Lightning console uses workspace tabs and subtabs
- Scope assertions to **active tab** context — other tabs may have stale DOM
- Utility bar components persist across navigation — test state isolation
- Subtab close should not affect parent tab state

## Iframes

| Context | Strategy |
|---------|----------|
| Experience Cloud | LWC may render inside community iframe — switch frame context |
| Visualforce embed | `<apex:iframe>` — switch to VF frame, then back |
| Flow runtime | Some Flows render in iframe within record page — identify container |

## Cross-Links

- [LWC UI Testing](lwc-ui-testing.md)
- [Salesforce UI Synchronization](salesforce-ui-synchronization.md)
- [SKILL.md](../SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [Playwright Review — Salesforce Synchronization](../../playwright-review/knowledge/salesforce-synchronization-techniques.md)
