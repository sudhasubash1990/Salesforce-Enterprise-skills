---
title: Accessibility Test Assessment Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, accessibility-testing, playbook]
---

# Accessibility Test Assessment Playbook

## Purpose

Structured workflow for assessing WCAG compliance testing scope for Salesforce UI.

## Assessment Steps

### Step 1 — Identify UI Scope
- Custom LWC components
- Experience Cloud pages and templates
- Custom CSS/theme overrides
- Third-party embedded components

### Step 2 — Determine WCAG Level
- Level A (minimum) — most projects
- Level AA (standard) — government, healthcare, financial services
- Level AAA (enhanced) — specific criteria as required

### Step 3 — Assess Keyboard Accessibility
- Tab order through all interactive elements
- Focus management in modals and popovers
- Keyboard shortcuts and their discoverability
- Skip navigation links

### Step 4 — Assess Screen Reader Compatibility
- ARIA labels on custom components
- Live regions for dynamic content updates
- Semantic HTML structure (headings, landmarks)
- Form field label associations

### Step 5 — Assess Visual Compliance
- Color contrast ratios (4.5:1 normal text, 3:1 large text for AA)
- Non-text contrast (3:1 for UI components)
- Text resizing behavior (200% zoom)
- Motion and animation controls

### Step 6 — Document Assessment
- Produce Accessibility Assessment section in SST report
- List components requiring accessibility testing
- Identify legal/regulatory requirements
- Recommend tooling (axe, WAVE, screen readers)

## Output

Accessibility Assessment section (section 11 of 18-section SST report).

## Related

- [Accessibility Testing Knowledge](../knowledge/accessibility-testing.md)
