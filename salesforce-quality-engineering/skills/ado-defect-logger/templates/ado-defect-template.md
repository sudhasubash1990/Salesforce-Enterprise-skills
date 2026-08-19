---
title: ADO Defect Template
module: Salesforce Quality Engineering
category: QE Specialized Skill Template
document_type: Template
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, ado-defect-template]
---

# ADO Defect Template

Use this template for every ADO Bug work item.

---

## Title

`[Component] Short defect summary` (max 128 characters)

## Severity

`1-Critical | 2-High | 3-Medium | 4-Low`

## Priority

`1 | 2 | 3 | 4`

## Area Path

`<Project>\<Module>\<Component>`

## Iteration Path

`<Project>\<Release>\<Sprint>`

## Tags

`<Salesforce Cloud>; <Component Type>; <Defect Category>; Regression (if applicable)`

## Found In Build

`<Build number or release version>`

## Found By

`<Tester name>`

## Assigned To

`<Developer/Admin for resolution>`

---

## Description

### Context
<!-- Business context, affected module, user persona -->

### Business Impact
<!-- Revenue, compliance, user productivity, data integrity -->

### Technical Impact
<!-- System stability, performance, security, integration -->

### Environment
<!-- Sandbox name, org type, browser, device, OS -->

---

## Repro Steps

1. Log in to `[Environment]` as `[Persona/Profile]`
2. Navigate to `[Object/Page/Tab]`
3. `[Specific action with specific data]`
4. `[Specific action]`
5. Observe `[specific element/field/message]`

## Expected Result

<!-- What should happen per requirement or design -->

## Actual Result

<!-- What actually happens — include error message, screenshot reference -->

---

## Evidence

| Type | Reference |
|------|-----------|
| Screenshot | `[Attached: filename.png]` |
| Error message | `[Full error text]` |
| Debug log | `[Attached: log file or excerpt]` |
| SOQL result | `[Query and result]` |
| API response | `[Status code, response body]` |

---

## Root Cause Hypothesis

- **Category:** Configuration | Metadata | Code | Integration | Data | Permission
- **Hypothesis:** `[Specific hypothesis]`
- **Confidence:** High | Medium | Low
- **Evidence needed:** `[Additional investigation required]`

## Related Items

| Relation | ID | Title |
|----------|----|-------|
| Related Requirement | `[User Story / Requirement ID]` | `[Title]` |
| Related Test Case | `[Test Case ID]` | `[Title]` |
| Related Defect | `[Bug ID]` | `[Title]` |

## Regression Impact

- **Is this a regression?** Yes / No
- **Previously working in:** `[Build/Release]`
- **Release impact:** Blocks release / Workaround available / Deferrable

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
