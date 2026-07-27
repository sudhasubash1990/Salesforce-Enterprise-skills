---
title: Permission Set Updated
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.17.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [permission-testing, example]
---

# Permission Set Updated

## Business Scenario

Grant Edit on WorkOrder to Dispatchers.

## Security Requirement

Dispatchers edit WorkOrder priority field.

## Validation Strategy

PS assignment + FLS verification.

## Expected Result

Dispatcher edits succeed.

## Negative Validation

Technician without PS cannot edit.

## Recommended SOQL

```sql
SELECT AssigneeId FROM PermissionSetAssignment WHERE PermissionSet.Name = 'Dispatcher'
```

## QA Recommendations

PSG assignment smoke test.
