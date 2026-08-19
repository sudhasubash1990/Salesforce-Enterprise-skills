---
title: ADO Test Case Template
module: Salesforce Quality Engineering
category: QE Specialized Skill Template
document_type: Template
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, template, ado-format]
---

# ADO Test Case Template

Default Azure DevOps test case format. Used when user does not provide a custom template.

---

## Test Case ID

`TC-XXX` (or ADO auto-assigned)

## Title

`[Object/Feature] — [Action] — [Scenario Type]`

Example: `Account — Create with Required Fields — Positive`

## Area Path

`\[Project]\[Module]\[Feature]`

## Iteration Path

`\[Project]\Sprint [N]`

## Test Suite

`[Suite Name]`

## Priority

`1` (Critical) | `2` (High) | `3` (Medium) | `4` (Low)

## Test Type

`Functional` | `Regression` | `Integration` | `E2E` | `Smoke` | `UAT` | `Security` | `Performance`

## Tags

`[tag1]; [tag2]; [tag3]`

## Requirement / User Story

`[US-XXX or BR-XXX or FR-XXX]`

## Preconditions

- [Required system state]
- [Required data setup]
- [Required user login / persona]

## Test Data

| Data Item | Value |
|-----------|-------|
| [Field 1] | [Value] |
| [Field 2] | [Value] |

## Test Steps

| Step # | Action | Expected Result |
|--------|--------|-----------------|
| 1 | [Specific user action] | [Measurable, observable outcome] |
| 2 | [Specific user action] | [Measurable, observable outcome] |
| 3 | [Specific user action] | [Measurable, observable outcome] |

> **Rule:** Expected Result must NEVER be "Verify it works", "Check functionality", "Validate successfully", or "Ensure correct behavior". Every expected result must describe a specific, observable system state or UI element.

## Parameters

| @Param1 | @Param2 | @ExpectedResult |
|---------|---------|-----------------|
| [Value set 1] | [Value set 1] | [Expected 1] |
| [Value set 2] | [Value set 2] | [Expected 2] |

_(Include only if test is data-driven)_

## Post Conditions

- [Expected system state after test execution]

## Automation Candidate

`Yes` | `No` | `Partial` — [Rationale]

## Persona

`[Role name]` (e.g., Sales Rep, System Admin, Service Agent)

## Environment

`SIT` | `UAT` | `Staging` | `Production`

## Risk

`[Risk level]` — `[Risk ID if applicable]`

## Business Criticality

`High` | `Medium` | `Low`

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
