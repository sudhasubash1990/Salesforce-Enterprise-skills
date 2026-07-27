---
title: Service Cloud Case Lifecycle
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.20.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [test-data-generator, example]
---

# Service Cloud Case Lifecycle

## Business Scenario

Case create→work→close with Account/Contact.

## Required Objects

Account, Contact, Case

## Relationships

Account→Case; Contact→Case

## Sample Data (Synthetic)

Case TDG-CASE-001 Status=New Origin=Phone; TDG-CASE-002 Status=Closed

## Validation Rules

Closed requires Reason (assumption — label if TBC).

## Expected Results

Statuses transition; Contact linked.

## Recommended SOQL

```sql
SELECT Id, Status, ContactId FROM Case WHERE Subject LIKE 'TDG%'
```

## QA Recommendations

Include entitlement only if licensed.
