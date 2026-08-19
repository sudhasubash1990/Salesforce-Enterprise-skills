---
title: LWC UI Testing Model
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

# LWC UI Testing Model

## Purpose

Define the testing model for Lightning Web Component rendering, interaction, visibility, and validation.

## Rendering Validation

| Category | What to Test |
|----------|-------------|
| Conditional rendering | `if:true`, `lwc:if`, `lwc:elseif`, `lwc:else` — assert DOM presence/absence |
| Dynamic components | `lwc:component` — verify correct component loads for given input |
| Loading states | Spinner/skeleton visible during wire/imperative calls |
| Empty states | Meaningful message when no records returned |
| Error states | User-facing error when Apex fails or wire returns error |

## Interaction Testing

| Component | Interactions |
|-----------|-------------|
| `lightning-input` | Type, clear, tab, validation message on blur |
| `lightning-combobox` | Open dropdown, select, keyboard navigate, filter |
| `lightning-button` | Click, disabled state, variant rendering |
| `lightning-datatable` | Sort, inline edit, row selection, pagination, column resize |
| `lightning-record-edit-form` | Field entry, save, cancel, server-side validation errors |
| `lightning-modal` | Open, close (X, cancel, ESC), focus trap, backdrop click |

## Visibility and Layout

- Component visibility based on `@api` property or conditional attribute
- Responsive behavior: verify layout shifts at standard breakpoints
- Tab/accordion collapse and expand
- Related list rendering within record pages

## Validation Patterns

- Required field enforcement on blur and submit
- Pattern/format validation (email, phone, currency)
- Custom validation via `reportValidity()` and `setCustomValidity()`
- Server-side validation errors surfaced in `lightning-record-edit-form`

## Component Communication

| Pattern | Testing Approach |
|---------|-----------------|
| `@api` property | Parent sets value → child renders correctly |
| Custom events | Child dispatches → parent handler updates state |
| Lightning Message Service | Publisher sends → subscriber reacts across DOM |
| `@wire` reactive | Property change → wire re-fires → UI updates |

## Toast and Notification

- Success/error/warning/info toast appears after action
- Toast auto-dismisses or is manually closeable
- Toast message content matches expected text

## Cross-Links

- [Lightning DOM Testing](lightning-dom-testing.md)
- [Accessibility Testing](accessibility-testing.md)
- [SKILL.md](../SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [Playwright Review — Salesforce UI](../../playwright-review/knowledge/salesforce-ui-automation-best-practices.md)
