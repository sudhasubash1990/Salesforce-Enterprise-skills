---
title: Salesforce Accessibility Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, accessibility-testing]
---

# Salesforce Accessibility Testing

## Purpose

Reference for assessing WCAG compliance testing scope for Salesforce UI — LWC components and Experience Cloud pages.

## WCAG Assessment Areas

| Area | WCAG Criteria | Salesforce Context |
|------|--------------|-------------------|
| **Keyboard navigation** | 2.1.1, 2.1.2 | Tab through Lightning components, modal focus traps |
| **Screen reader** | 1.3.1, 4.1.2 | ARIA labels on LWC, live regions for dynamic content |
| **Focus order** | 2.4.3 | Logical tab sequence in flexipages, utility bar, modals |
| **Labels** | 1.3.1, 3.3.2 | Form field labels, lightning-input label attribute |
| **Contrast** | 1.4.3, 1.4.11 | Custom CSS overrides, Experience Cloud themes |
| **Error messaging** | 3.3.1, 3.3.3 | Inline validation announcements, toast accessibility |
| **ARIA** | 4.1.2 | Roles, states, properties on custom LWC components |
| **Images** | 1.1.1 | Alt text on images, decorative image handling |

## Salesforce-Specific Considerations

### Lightning Web Components
- Base components (lightning-input, lightning-datatable) have built-in accessibility
- Custom components must implement ARIA attributes manually
- Shadow DOM boundaries affect screen reader traversal

### Experience Cloud
- Custom themes may override SLDS contrast ratios
- Guest user pages need full keyboard accessibility
- CMS content blocks require alt text and heading structure

### WCAG Compliance Levels
| Level | Scope | Typical Requirement |
|-------|-------|-------------------|
| **A** | Minimum | Most Salesforce projects |
| **AA** | Standard | Government, healthcare, financial services |
| **AAA** | Enhanced | Rarely required in full; specific criteria may apply |

## Related

- [Specialized Testing Model](specialized-testing-model.md)
- [Mobile Testing](mobile-testing.md) — Overlaps with responsive accessibility
