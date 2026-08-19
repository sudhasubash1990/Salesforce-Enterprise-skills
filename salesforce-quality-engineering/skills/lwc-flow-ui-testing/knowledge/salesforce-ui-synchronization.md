---
title: Salesforce UI Synchronization
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

# Salesforce UI Synchronization

## Purpose

Document async patterns, polling, loading indicators, and platform event UI refresh that affect LWC and Flow UI testing.

## Common Async Patterns

| Pattern | UI Behavior | Sync Strategy |
|---------|------------|---------------|
| Wire adapter | Component re-renders when data arrives | Wait for bound element content |
| Imperative Apex | Promise resolves → state update → re-render | Wait for loading spinner removal + content |
| `refreshApex()` | Forces wire re-fetch → re-render | Wait for stale content to update |
| Platform events | Streaming subscription → handler fires → DOM update | Wait for expected DOM change after publish |
| `lightning/navigation` | Page transition | Wait for target page indicator |

## Loading Indicators

- `lightning-spinner` — component-level loading
- Skeleton screens — placeholder content before data loads
- Progress indicators in Flows — between screen transitions
- Global spinner — full-page loading during navigation

**Test pattern:** Assert loading indicator appears → disappears → content renders.

## Polling and Refresh

- Some LWC implement polling via `setInterval` for near-real-time updates
- Test that polling does not cause memory leaks or stale state accumulation
- Verify manual refresh button triggers data reload

## Platform Events and UI

- Empapi subscription receives platform event → handler updates component state
- Test: publish event → verify UI reflects new data within reasonable time
- Do not assert exact timing — use condition-based waits

## Toast Timing

- Toasts auto-dismiss after platform default (~3 seconds for success)
- Assert toast content immediately after action — do not rely on toast persistence
- Error toasts may persist until manually dismissed — verify dismissal

## Flow Screen Transitions

- Screen Flow transitions involve server round-trip
- Wait for next screen's input fields to render before asserting
- Back navigation may re-render with cached or fresh data — verify

## Cross-Links

- [Lightning DOM Testing](lightning-dom-testing.md)
- [LWC UI Testing](lwc-ui-testing.md)
- [SKILL.md](../SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [Playwright Review — Salesforce Synchronization](../../playwright-review/knowledge/salesforce-synchronization-techniques.md)
