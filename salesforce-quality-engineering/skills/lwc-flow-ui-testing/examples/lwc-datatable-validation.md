---
title: "Example: LWC Datatable Validation"
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

# Example — LWC Datatable Rendering and Interaction

## 1. Intent

Test a custom LWC using `lightning-datatable` for rendering, sorting, inline edit, row selection, and pagination.

## 2. Context

| Field | Value |
|-------|-------|
| Component API Name | `opportunityListLWC` |
| Org Type | Lightning App |
| Parent Page | Account Record Page (related list replacement) |
| Personas | Sales Rep, Sales Manager |
| Data source | `@wire` with Apex `getOpportunities` |

## 3. Assumptions

- Datatable columns: Name, Stage, Amount, Close Date, Owner
- Inline edit enabled for Stage and Amount
- Row actions: View, Edit, Delete (Delete only for Manager)
- Pagination via "Load More" button at 50-record threshold

## 4. Scope

**In scope:** Column rendering, sort, inline edit, row actions, pagination, empty state, error

**Out of scope:** Apex query performance, bulk delete logic

## 5. Component Analysis

| Property | Details |
|----------|---------|
| Wire adapter | Custom Apex `getOpportunities(accountId)` |
| Columns | 5 + row actions |
| Events | `onsort`, `onrowaction`, `onsave` (inline edit) |
| Pagination | Client-side offset, Load More button |

## 6. Rendering Validation

| Scenario | Expected |
|----------|----------|
| Records exist | Datatable renders with correct columns and data |
| No records | "No opportunities found" empty state |
| Loading | Spinner while wire fetches |
| Error | Error banner if Apex fails |
| 50+ records | "Load More" button visible |

## 7. Interaction Testing

| Scenario | Action | Expected |
|----------|--------|----------|
| Sort by Amount | Click Amount header | Rows re-order descending |
| Inline edit Stage | Double-click Stage cell → select new value → Save | Toast: "Record updated" |
| Row action View | Click View | Navigates to Opportunity record |
| Row action Delete (Manager) | Click Delete → Confirm | Row removed, toast |
| Row action Delete (Rep) | — | Delete action not visible |
| Load More | Click button | Next 50 records append |

## 8. Accessibility Assessment

| Check | Expected |
|-------|----------|
| Grid role | `role="grid"` with proper row/cell structure |
| Sort indicator | `aria-sort` on sorted column |
| Inline edit | Focus to editable cell on activation |
| Row actions | Menu accessible via keyboard |

## 9. Flow Navigation Testing

N/A — standalone LWC.

## 10. Error & Edge Cases

| Scenario | Expected |
|----------|----------|
| Inline edit concurrent conflict | Error toast, cell reverts |
| Delete last row | Empty state renders |
| Column resize | Layout does not break |
| 500+ records total | Load More works iteratively |

## 11. Quality Gates

- [x] All columns and data types validated
- [x] Sort, inline edit, row actions covered
- [x] Persona-based action visibility (Delete)
- [x] Pagination tested
- [x] Empty and error states covered

## 12. Dependencies

| Dependency | Chain |
|------------|-------|
| 60+ Opportunity records | TDG |
| Sales Rep vs Manager profiles | PTA |

## 13. Recommended Next Actions

- Chain PWR for datatable Playwright automation
- Chain PTA for row action visibility matrix
