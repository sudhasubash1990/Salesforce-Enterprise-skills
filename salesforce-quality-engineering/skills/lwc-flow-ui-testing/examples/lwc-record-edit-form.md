---
title: "Example: LWC Record Edit Form"
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

# Example — Lightning Record Edit Form Testing

## 1. Intent

Test a `lightning-record-edit-form` component for field rendering, validation, save behavior, and error handling on a Contact record page.

## 2. Context

| Field | Value |
|-------|-------|
| Component | `lightning-record-edit-form` (standard base component) |
| Object | Contact |
| Org Type | Lightning App |
| Parent Page | Contact Record Page |
| Personas | Sales Rep, Sales Manager |

## 3. Assumptions

- Form displays: First Name, Last Name, Email, Phone, Account (lookup)
- Server-side validation rule: Email is required when Phone is blank
- FLS controls field visibility per profile

## 4. Scope

**In scope:** Field rendering, required validation, save, cancel, server-side errors, FLS impact

**Out of scope:** Lookup component internal search (standard behavior), Playwright scripts

## 5. Component Analysis

| Property | Details |
|----------|---------|
| Object API Name | Contact |
| Fields rendered | FirstName, LastName, Email, Phone, AccountId |
| Events | `onsuccess`, `onerror`, `onsubmit` |
| Record type | Default |

## 6. Rendering Validation

| Scenario | Expected |
|----------|----------|
| Initial load | All 5 fields render with current values |
| FLS — Sales Rep no Phone access | Phone field hidden |
| Read-only field | Account field non-editable for Sales Rep |

## 7. Interaction Testing

| Scenario | Action | Expected |
|----------|--------|----------|
| Valid save | Update Last Name → Save | Toast: "Contact saved" |
| Cancel | Click Cancel | Reverts to view mode, no save |
| Required bypass | Clear Last Name → Save | Client-side error on Last Name |
| Server validation | Clear Email and Phone → Save | Server error: "Email required when Phone is blank" |

## 8. Accessibility Assessment

| Check | Expected |
|-------|----------|
| Field labels | Each `lightning-input-field` has visible label |
| Error association | Validation error linked via `aria-describedby` |
| Save button | Keyboard accessible, `role="button"` |
| Toast | Announced via live region |

## 9. Flow Navigation Testing

N/A — not embedded in Flow.

## 10. Error & Edge Cases

| Scenario | Expected |
|----------|----------|
| Concurrent edit | "Record modified" error on save |
| Network loss | Error toast, form data preserved |
| Max field length | Truncation or validation error |

## 11. Quality Gates

- [x] All fields and validation paths covered
- [x] Server-side error scenario included
- [x] FLS impact documented
- [x] Accessibility assessed

## 12. Dependencies

| Dependency | Chain |
|------------|-------|
| Test Contact + Account | TDG |
| Sales Rep vs Manager FLS | PTA |

## 13. Recommended Next Actions

- Chain PTA for FLS matrix across profiles
- Chain PWR for save/cancel automation
