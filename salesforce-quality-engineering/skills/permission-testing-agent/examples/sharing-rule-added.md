---
title: Sharing Rule Added
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

# Sharing Rule Added

## Business Scenario

Criteria share opens Cases in Region West.

## Security Requirement

West region agents see additional Cases.

## Validation Strategy

Before/after visibility comparison.

## Expected Result

West Cases visible post rule.

## Negative Validation

East Cases unchanged.

## Recommended SOQL

```sql
SELECT Id, Region__c FROM Case WHERE Region__c = 'West' LIMIT 20
```

## QA Recommendations

Regression all personas in rule criteria.
