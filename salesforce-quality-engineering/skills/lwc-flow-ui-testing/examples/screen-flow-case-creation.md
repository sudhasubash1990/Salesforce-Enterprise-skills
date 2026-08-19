---
title: "Example: Screen Flow Case Creation"
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

# Example — Screen Flow Case Creation UI Testing

## 1. Intent

Test the `Create_New_Case` Screen Flow for navigation, input validation, decision routing, and fault handling.

## 2. Context

| Field | Value |
|-------|-------|
| Flow API Name | `Create_New_Case` |
| Flow Type | Screen Flow |
| Entry Point | Quick Action on Account record |
| Personas | Service Agent, Service Manager |
| Screens | 3 (Category Selection → Case Details → Confirmation) |
| Decision Elements | 1 (Category determines required fields on Screen 2) |

## 3. Assumptions

- Flow creates a Case record linked to the parent Account
- Category picklist drives conditional visibility on Case Details screen
- Fault connector handles DML errors

## 4. Scope

**In scope:** All 3 screens, navigation, validation, decision, fault path, persona behavior

**Out of scope:** Apex action internals, email notification testing

## 5. Component Analysis

| Screen | Input Components | Required | Conditional |
|--------|-----------------|----------|-------------|
| Screen 1 | Category picklist | Yes | — |
| Screen 2 | Subject (text), Description (textarea), Priority (picklist), Serial Number (text) | Subject, Description | Serial Number visible when Category = "Hardware" |
| Screen 3 | Display text (confirmation) | — | — |

## 6. Rendering Validation

| Screen | Condition | Expected |
|--------|-----------|----------|
| Screen 2 | Category = "Software" | Serial Number hidden |
| Screen 2 | Category = "Hardware" | Serial Number visible and required |
| Screen 3 | Successful save | Case Number displayed |

## 7. Interaction Testing

| Scenario | Screen | Action | Expected |
|----------|--------|--------|----------|
| Required bypass | 1 | Click Next without selecting Category | Validation error |
| Happy path | 1→2→3 | Complete all fields → Next → Finish | Case created |
| Conditional field | 2 | Category = Hardware | Serial Number appears |

## 8. Accessibility Assessment

| Check | Expected |
|-------|----------|
| Screen transition focus | Focus to first input on Screen 2 |
| Required field indicator | `aria-required="true"` on required inputs |
| Error on required bypass | Screen reader announces validation error |

## 9. Flow Navigation Testing

| Path | Steps | Expected |
|------|-------|----------|
| Happy | 1 → 2 → 3 (Finish) | Case created, confirmation |
| Back | 2 → Back → 1 | Category preserved |
| Cancel | Any → Cancel | No Case created |
| Fault | DML error on save | Fault screen with message |

## 10. Error & Edge Cases

| Scenario | Expected |
|----------|----------|
| Duplicate Case (validation rule) | Inline error on Screen 2 |
| Apex DML exception | Fault screen, retry available |
| 5000-char Description | Accepts or shows length error |

## 11. Quality Gates

- [x] All 3 screens documented
- [x] Decision branch covered (Software vs Hardware)
- [x] Fault path covered
- [x] Back/Cancel navigation tested
- [x] Persona variation: Manager can set Priority = Critical

## 12. Dependencies

| Dependency | Chain |
|------------|-------|
| Test Account record | TDG |
| Service Agent vs Manager profiles | PTA |

## 13. Recommended Next Actions

- Chain PWR for Playwright Flow automation
- Chain PTA for Manager-specific Priority options
