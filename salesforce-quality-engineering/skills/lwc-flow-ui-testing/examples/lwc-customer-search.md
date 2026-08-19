---
title: "Example: LWC Customer Search"
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [lwc-flow-ui-testing, example]
---

# Example — LWC Customer Search Component

## 1. Intent

Test the `customerSearchLWC` component for rendering, interaction, and accessibility in a Service Cloud console context.

## 2. Context

| Field | Value |
|-------|-------|
| Component API Name | `customerSearchLWC` |
| Org Type | Service Cloud Console |
| Parent Page | Account Record Page |
| Personas | Service Agent, Service Manager |
| Related Components | `lightning-input`, `lightning-datatable`, `lightning-card` |

## 3. Assumptions

- Component uses `@wire` with custom Apex to fetch accounts
- Results render in `lightning-datatable`
- Lightning Message Service publishes selected account to sibling components

## 4. Scope

**In scope:** Search input, result rendering, row selection, LMS publish, empty/loading/error states, accessibility

**Out of scope:** Apex query logic, Playwright scripts (chain PWR)

## 5. Component Analysis

| Property | Details |
|----------|---------|
| Public APIs | `@api recordId` |
| Wire adapters | Custom Apex `searchAccounts` |
| Events dispatched | `accountselected` (CustomEvent via LMS) |
| Child components | `lightning-input`, `lightning-datatable`, `lightning-spinner` |

## 6. Rendering Validation

| Scenario | Condition | Expected |
|----------|-----------|----------|
| Initial load | No search term | Empty state message: "Enter search criteria" |
| Loading | Search initiated | Spinner visible, datatable hidden |
| Results | Records found | Datatable with columns: Name, Phone, Industry |
| No results | Zero matches | "No accounts found" message |
| Error | Apex throws | Error banner with retry option |

## 7. Interaction Testing

| Scenario | Action | Expected |
|----------|--------|----------|
| Search | Type 3+ characters, debounce triggers | Results load after debounce |
| Clear | Clear input | Reset to empty state |
| Row select | Click row | LMS publishes account ID |
| Sort | Click column header | Datatable re-sorts |

## 8. Accessibility Assessment

| Check | Expected |
|-------|----------|
| Search input label | "Search Accounts" visible or `aria-label` |
| Datatable navigation | Arrow keys between rows, Enter to select |
| Spinner | `role="status"` with label |
| Error banner | Announced via `aria-live` |

## 9. Flow Navigation Testing

N/A — standalone LWC, not embedded in Flow.

## 10. Error & Edge Cases

| Scenario | Expected |
|----------|----------|
| Network timeout | Error state with retry |
| Special characters in search | Handled gracefully, no injection |
| 200+ results | Pagination or "refine search" message |

## 11. Quality Gates

- [x] Component metadata identified
- [x] All rendering states covered
- [x] Interaction happy + negative paths
- [x] Accessibility assessed
- [x] Semantic locators: `getByRole('searchbox')`, `getByRole('grid')`

## 12. Dependencies

| Dependency | Chain |
|------------|-------|
| Test accounts | TDG |
| Service Agent profile | PTA |

## 13. Recommended Next Actions

- Chain PWR for Playwright automation with locator map
- Chain PTA for Manager vs Agent visibility differences
