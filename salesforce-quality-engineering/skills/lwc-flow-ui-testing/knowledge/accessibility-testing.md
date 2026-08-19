---
title: Accessibility Testing
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

# Accessibility Testing

## Purpose

WCAG-aligned accessibility testing for LWC and Flow UI: keyboard navigation, screen reader, focus order, labels, contrast, ARIA, and error messaging.

## Keyboard Navigation

| Test | Expected Behavior |
|------|-------------------|
| Tab order | Follows logical reading order; skips hidden/disabled elements |
| Enter/Space on button | Activates button action |
| Escape on modal | Closes modal, returns focus to trigger |
| Arrow keys in combobox | Navigate options without mouse |
| Tab through datatable | Moves between actionable cells; inline edit activates on Enter |
| Flow Next/Back buttons | Reachable via Tab; activatable via Enter |

## Screen Reader

- All interactive elements have accessible names (visible label or `aria-label`)
- Status messages use `role="status"` or `aria-live` regions
- Toast notifications announced via live region
- Datatable column headers associated with data cells
- Flow screen titles announced on screen transition

## Focus Management

- Modal open → focus moves to first interactive element inside modal
- Modal close → focus returns to triggering element
- Flow screen transition → focus moves to first input or heading
- Inline edit → focus moves to editable field
- Error → focus moves to first invalid field

## ARIA Attributes

| Component | Expected ARIA |
|-----------|--------------|
| `lightning-combobox` | `role="combobox"`, `aria-expanded`, `aria-activedescendant` |
| `lightning-modal` | `role="dialog"`, `aria-modal="true"`, `aria-labelledby` |
| `lightning-datatable` | `role="grid"`, row/cell roles, sort indicators |
| Custom LWC | Developer must add appropriate `role`, `aria-label`, `aria-describedby` |
| Flow screens | `role="form"` or landmark, screen title as heading |

## Contrast and Visual

- Text meets WCAG AA contrast ratio (4.5:1 normal, 3:1 large)
- Focus indicators visible on all interactive elements
- Error states use color + icon/text (not color alone)
- Loading states accessible (spinner has `aria-label` or `role="status"`)

## Error Messaging

- Validation errors programmatically associated with input (`aria-describedby` or `aria-errormessage`)
- Error summary provides count and links to invalid fields
- Flow fault screen error messages are readable and actionable

## Limitations

- This capability assesses accessibility through component analysis and known patterns
- No invented WCAG compliance scores or percentages
- Automated accessibility scanning tools (axe, Lighthouse) are complementary — recommend but do not simulate results

## Cross-Links

- [LWC UI Testing](lwc-ui-testing.md)
- [Flow UI Testing](flow-ui-testing.md)
- [SKILL.md](../SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [Playwright Review — Accessibility](../../playwright-review/knowledge/accessibility-testing.md)
