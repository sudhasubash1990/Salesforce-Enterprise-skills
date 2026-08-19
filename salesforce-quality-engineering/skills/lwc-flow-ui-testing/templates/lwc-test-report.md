---
title: LWC Test Report Template
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

# LWC Test Report — [Component Name]

## 1. Intent

*What is being tested and why.*

## 2. Context

| Field | Value |
|-------|-------|
| Component API Name | |
| Org Type | Lightning / Experience / Console |
| Parent Page | Record Page / App Page / Home Page |
| Personas | |
| Related Components | |

## 3. Assumptions

- [ ] *List assumptions about environment, data, and configuration*

## 4. Scope

**In scope:** *List specific rendering, interaction, and validation scenarios*

**Out of scope:** *List exclusions (e.g., backend logic, Playwright scripts)*

## 5. Component Analysis

| Property | Details |
|----------|---------|
| Public APIs (`@api`) | |
| Wire adapters | |
| Events dispatched | |
| Events handled | |
| Child components | |
| Lightning Message Service | Yes / No |

## 6. Rendering Validation

| Scenario | Condition | Expected | Status |
|----------|-----------|----------|--------|
| *Conditional render* | | | |
| *Loading state* | | | |
| *Empty state* | | | |
| *Error state* | | | |

## 7. Interaction Testing

| Scenario | User Action | Expected Result | Status |
|----------|-------------|-----------------|--------|
| *Input entry* | | | |
| *Button click* | | | |
| *Inline edit* | | | |
| *Modal open/close* | | | |

## 8. Accessibility Assessment

| Check | Expected | Status |
|-------|----------|--------|
| Keyboard tab order | Logical sequence | |
| Screen reader labels | All interactive elements labeled | |
| Focus management | Returns to trigger on modal close | |
| ARIA attributes | Correct roles and states | |
| Error messaging | Programmatically associated | |

*No invented WCAG compliance scores. Document observable findings.*

## 9. Flow Navigation Testing

*N/A for standalone LWC — or document if component is embedded in a Flow screen.*

## 10. Error & Edge Cases

| Scenario | Trigger | Expected Behavior | Status |
|----------|---------|-------------------|--------|
| *Network error* | | | |
| *Governor limit* | | | |
| *Concurrent edit* | | | |

## 11. Quality Gates

- [ ] Component metadata identified
- [ ] Rendering paths covered (conditional, dynamic, empty, error)
- [ ] Interaction scenarios include happy + negative
- [ ] Accessibility assessed
- [ ] Semantic locators documented
- [ ] No brittle XPath or hard waits

## 12. Dependencies

| Dependency | Type | Status |
|------------|------|--------|
| *Test data* | Chain TDG | |
| *Permissions* | Chain PTA | |
| *Metadata impact* | Chain MIA | |

## 13. Recommended Next Actions

- [ ] Chain PWR for Playwright automation
- [ ] Chain PTA for persona-specific paths
- [ ] Chain TDG for test data setup
- [ ] *Additional actions*
