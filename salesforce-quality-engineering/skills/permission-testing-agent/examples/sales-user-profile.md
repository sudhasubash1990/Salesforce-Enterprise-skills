---
title: Sales User Profile
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

# Sales User Profile

## Business Scenario

Inside sales reps manage own Opportunities.

## Security Requirement

Create/read/edit own Opportunities; no delete on Account.

## Validation Strategy

CRUD matrix for Sales User on Opportunity/Account; FLS on Amount field.

## Expected Result

Own records visible; cannot delete Account.

## Negative Validation

Cannot edit peer-owned Opportunity.

## Recommended SOQL

```sql
SELECT Id, OwnerId FROM Opportunity WHERE OwnerId != :currentUserId LIMIT 5
```

## QA Recommendations

Regression on Opportunity team if enabled.
