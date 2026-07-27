---
title: Service User Profile
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

# Service User Profile

## Business Scenario

Agents work Cases for assigned queue.

## Security Requirement

Read/edit Case; no Account delete.

## Validation Strategy

Queue membership + Case CRUD; record access via queue.

## Expected Result

Queue Cases editable.

## Negative Validation

Non-queue Case not editable.

## Recommended SOQL

```sql
SELECT Id, OwnerId FROM Case WHERE OwnerId = :queueId LIMIT 10
```

## QA Recommendations

Omni-channel assignment separate test.
