---
title: LWC Accessibility Checklist
module: Salesforce Quality Engineering
category: QE Specialized Skill Template
document_type: Template
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [lwc-flow-ui-testing, template]
---

# LWC Accessibility Checklist — [Component/Flow Name]

## Keyboard Navigation

- [ ] All interactive elements reachable via Tab
- [ ] Logical tab order follows visual layout
- [ ] Enter/Space activates buttons and links
- [ ] Escape closes modals, popovers, dropdowns
- [ ] Arrow keys navigate within composite widgets (combobox, datatable, tabs)
- [ ] No keyboard traps (user can always Tab away)

## Screen Reader

- [ ] All inputs have visible label or `aria-label`
- [ ] Buttons have accessible name (text content or `aria-label`)
- [ ] Images/icons have `alt` text or `aria-hidden="true"` for decorative
- [ ] Status messages use `aria-live` region
- [ ] Toast notifications announced
- [ ] Datatable headers associated with cells
- [ ] Flow screen title announced as heading

## Focus Management

- [ ] Modal open → focus to first element inside
- [ ] Modal close → focus returns to trigger
- [ ] Flow screen transition → focus to first input or heading
- [ ] Inline edit activation → focus to editable field
- [ ] Error state → focus to first invalid field

## ARIA

- [ ] Combobox: `role="combobox"`, `aria-expanded`, `aria-activedescendant`
- [ ] Modal: `role="dialog"`, `aria-modal="true"`, `aria-labelledby`
- [ ] Datatable: `role="grid"` with row/cell roles
- [ ] Custom components: appropriate roles assigned
- [ ] Required fields: `aria-required="true"`
- [ ] Invalid fields: `aria-invalid="true"`, `aria-describedby` pointing to error

## Visual

- [ ] Text contrast ≥ 4.5:1 (normal) / 3:1 (large)
- [ ] Focus indicator visible on all interactive elements
- [ ] Error state uses color + icon/text (not color alone)
- [ ] Loading spinner has accessible label

## Error Messaging

- [ ] Validation errors programmatically linked to input
- [ ] Error text is descriptive and actionable
- [ ] Error summary (if present) lists all issues with field links

## Notes

*Document findings. Do not invent WCAG compliance scores or percentages.*
