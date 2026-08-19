---
title: ADO Defect Model
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, ado-defect-model]
---

# ADO Bug Work Item Model

Reference for Azure DevOps Bug work item type — fields, workflows, states, and transitions.

## Bug Work Item Fields

### Required Fields

| Field | ADO API Field | Type | Notes |
|-------|---------------|------|-------|
| Title | `System.Title` | String (max 256) | `[Component] Short summary` format |
| State | `System.State` | String | Default: New |
| Severity | `Microsoft.VSTS.Common.Severity` | String | 1-Critical, 2-High, 3-Medium, 4-Low |
| Priority | `Microsoft.VSTS.Common.Priority` | Integer | 1, 2, 3, 4 |

### Recommended Fields

| Field | ADO API Field | Type | Notes |
|-------|---------------|------|-------|
| Repro Steps | `Microsoft.VSTS.TCM.ReproSteps` | HTML | Numbered reproduction steps |
| System Info | `Microsoft.VSTS.TCM.SystemInfo` | HTML | Environment, browser, device |
| Area Path | `System.AreaPath` | TreePath | Module/component path |
| Iteration Path | `System.IterationPath` | TreePath | Sprint path |
| Assigned To | `System.AssignedTo` | Identity | Developer for resolution |
| Found In | `Microsoft.VSTS.Build.FoundIn` | String | Build/release version |
| Tags | `System.Tags` | String | Semicolon-separated |
| Description | `System.Description` | HTML | Full defect description |

### Custom Fields (Salesforce Programs)

| Field | Purpose |
|-------|---------|
| Salesforce Cloud | Sales, Service, Experience, etc. |
| Salesforce Component | Object, Flow, LWC, Apex class |
| Root Cause Category | Configuration, Code, Data, Integration, Permission, Metadata |
| Business Impact | Revenue, compliance, productivity statement |
| Regression | Yes / No |

## Bug States and Transitions

```
New → Active → Resolved → Closed
         ↓         ↑
         └─────────┘ (Reactivated)
```

| State | Meaning |
|-------|---------|
| **New** | Defect logged, not yet triaged |
| **Active** | Accepted by dev team, work in progress |
| **Resolved** | Fix applied, awaiting verification |
| **Closed** | Fix verified by QA |

### State Transition Rules

| From | To | Trigger |
|------|----|---------|
| New | Active | Dev accepts and begins work |
| Active | Resolved | Developer marks fix complete |
| Resolved | Closed | QA verifies fix in target environment |
| Resolved | Active | QA rejects fix (reactivation) |
| Closed | Active | Regression found (reopen) |

## Linking

| Link Type | Usage |
|-----------|-------|
| **Tested By** | Link Bug to Test Case that found it |
| **Related** | Link to related User Story or Requirement |
| **Parent** | Link to parent Feature or Epic |
| **Duplicate** | Link to duplicate Bug |
| **Successor/Predecessor** | Dependency between Bugs |

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
