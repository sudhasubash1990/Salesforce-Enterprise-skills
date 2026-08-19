---
title: ADO Test Case Model
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, ado-model]
---

# ADO Test Case Model

Reference for Azure DevOps Test Case work item structure, test suite organization, and test plan hierarchy.

## Test Plan Hierarchy

```
Test Plan
 └── Test Suite (Static / Requirement-Based / Query-Based)
      └── Test Case
           └── Test Steps (Step #, Action, Expected Result)
                └── Shared Steps (reusable across test cases)
           └── Parameters (data-driven rows)
           └── Attachments (screenshots, logs, evidence)
```

## Test Case Work Item Fields

### System Fields

| Field | ADO Field Name | Type | Description |
|-------|---------------|------|-------------|
| ID | `System.Id` | Integer | Auto-assigned by ADO |
| Title | `System.Title` | String | Concise, action-oriented test case name |
| State | `System.State` | String | Design / Ready / Closed |
| Area Path | `System.AreaPath` | TreePath | Organizational area |
| Iteration Path | `System.IterationPath` | TreePath | Sprint/iteration |
| Tags | `System.Tags` | String | Semicolon-separated tags |
| Assigned To | `System.AssignedTo` | Identity | Test executor |

### Test-Specific Fields

| Field | ADO Field Name | Type | Description |
|-------|---------------|------|-------------|
| Priority | `Microsoft.VSTS.Common.Priority` | Integer | 1–4 |
| Automation Status | `Microsoft.VSTS.TCM.AutomationStatus` | String | Not Automated / Planned / Automated |
| Steps | `Microsoft.VSTS.TCM.Steps` | HTML | Structured test steps |
| Parameters | `Microsoft.VSTS.TCM.Parameters` | HTML | Data-driven parameter table |
| Local Data Source | `Microsoft.VSTS.TCM.LocalDataSource` | HTML | Parameter data rows |

### Custom/Extended Fields (Recommended)

| Field | Purpose |
|-------|---------|
| Test Type | Functional / Regression / Integration / E2E / Smoke / UAT / Security |
| Preconditions | Required state before test execution |
| Test Data | Specific data values or references |
| Post Conditions | Expected system state after execution |
| Persona | Role executing the test |
| Environment | SIT / UAT / Staging / Production |
| Risk | Risk level and ID |
| Business Criticality | High / Medium / Low |
| Automation Candidate | Yes / No / Partial |

## Test Suite Types

| Type | Description | Use When |
|------|-------------|----------|
| **Static** | Manually organized collection | Ad hoc grouping, smoke suites |
| **Requirement-Based** | Auto-linked to requirement work items | Traceability-driven testing |
| **Query-Based** | Dynamic membership via work item query | Regression suites, tag-based selection |

## Test Step Structure (HTML Format)

ADO stores test steps as HTML in `Microsoft.VSTS.TCM.Steps`:

```html
<steps id="0" last="3">
  <step id="1" type="ActionStep">
    <parameterizedString isformatted="true">Navigate to Accounts tab</parameterizedString>
    <parameterizedString isformatted="true">Accounts list view is displayed with default columns</parameterizedString>
  </step>
  <step id="2" type="ActionStep">
    <parameterizedString isformatted="true">Click "New" button</parameterizedString>
    <parameterizedString isformatted="true">New Account form opens with required fields marked (*)</parameterizedString>
  </step>
</steps>
```

## Parameters (Data-Driven Testing)

Parameters enable the same test steps to run with multiple data sets:

```html
<parameters>
  <param name="AccountName" bind="default" />
  <param name="Industry" bind="default" />
  <param name="ExpectedResult" bind="default" />
</parameters>
```

Referenced in steps as `@AccountName`, `@Industry`.

## Test Run and Results

| Entity | Description |
|--------|-------------|
| Test Run | Execution instance of a test plan/suite |
| Test Result | Pass/Fail/Blocked/Not Applicable per test case |
| Test Point | Assignment of test case + configuration |
| Configuration | Environment/browser/device combination |

## Linking

| Link Type | From | To |
|-----------|------|-----|
| Tests / Tested By | Test Case | User Story / Requirement |
| Parent / Child | Test Suite | Test Case |
| Related | Test Case | Bug / Defect |

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
