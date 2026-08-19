---
title: Flow UI Test Report Template
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

# Flow UI Test Report — [Flow Name]

## 1. Intent

*What Flow behavior is being tested and why.*

## 2. Context

| Field | Value |
|-------|-------|
| Flow API Name | |
| Flow Type | Screen Flow / Auto-launched (UI entry) |
| Entry Point | Record Page / Button / Quick Action / URL |
| Personas | |
| Screens Count | |
| Decision Elements | |

## 3. Assumptions

- [ ] *List assumptions about org config, data, profiles*

## 4. Scope

**In scope:** *Navigation paths, input validation, fault paths*

**Out of scope:** *Backend logic, Apex action internals*

## 5. Component Analysis

| Screen | Input Components | Required Fields | Conditional Visibility |
|--------|-----------------|-----------------|----------------------|
| | | | |

## 6. Rendering Validation

| Screen | Condition | Expected Rendering | Status |
|--------|-----------|-------------------|--------|
| *Screen 1* | Default load | All fields visible | |
| *Screen 2* | Choice = X | Section Y hidden | |

## 7. Interaction Testing

| Scenario | Screen | Action | Expected | Status |
|----------|--------|--------|----------|--------|
| *Required field* | | Leave blank → Next | Validation error | |
| *Picklist select* | | Choose option | Next screen updates | |

## 8. Accessibility Assessment

| Check | Expected | Status |
|-------|----------|--------|
| Focus on screen transition | Moves to first input/heading | |
| Navigation buttons keyboard | Tab + Enter works | |
| Error announcement | Screen reader announces | |
| Screen title | Announced as heading | |

## 9. Flow Navigation Testing

| Path | Steps | Expected Outcome | Status |
|------|-------|-------------------|--------|
| Happy path | Screen 1 → 2 → 3 → Finish | Record created, success message | |
| Back navigation | Screen 2 → Back → Screen 1 | Data preserved | |
| Cancel | Any screen → Cancel | Flow exits, no record created | |
| Resume | Pause → Resume | Correct screen, data intact | |
| Fault path | DML error | Fault screen with user message | |

## 10. Error & Edge Cases

| Scenario | Trigger | Expected | Status |
|----------|---------|----------|--------|
| *DML failure* | | Fault screen | |
| *Apex exception* | | Error message | |
| *Validation rule* | | Inline error | |

## 11. Quality Gates

- [ ] All screens documented
- [ ] Navigation paths (next, back, cancel, resume, finish) covered
- [ ] Decision branches each have test scenario
- [ ] Fault paths covered
- [ ] Persona variations identified

## 12. Dependencies

| Dependency | Type | Status |
|------------|------|--------|
| *Test data* | Chain TDG | |
| *Permissions* | Chain PTA | |

## 13. Recommended Next Actions

- [ ] Chain PWR for Playwright automation of Flow UI
- [ ] Chain PTA for persona-specific Flow entry/visibility
- [ ] Chain TDG for prerequisite records
