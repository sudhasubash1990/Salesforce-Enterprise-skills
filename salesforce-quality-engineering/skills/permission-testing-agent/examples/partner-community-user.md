---
title: Partner Community User
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

# Partner Community User

## Business Scenario

Partners see shared Opportunities.

## Security Requirement

Read/edit shared Opportunities only.

## Validation Strategy

Sharing set / criteria sharing tests.

## Expected Result

Shared opps visible.

## Negative Validation

Non-shared opps hidden.

## Recommended SOQL

```sql
SELECT Id FROM Opportunity WHERE Id NOT IN (SELECT ParentId FROM PartnerNetworkRecordConnection LIMIT 100)
```

## QA Recommendations

Critical regression on sharing set deploy.
