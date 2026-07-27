---
title: Flow Validation
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.16.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [soql-validation, example]
---

# Flow Validation

## Business Scenario

Flow creates Task on Case update.

## Validation Objective

Cases updated today have follow-up Task.

## Generated SOQL

```sql
SELECT Id FROM Case WHERE Id NOT IN (SELECT WhatId FROM Task WHERE CreatedDate = TODAY) AND Status = 'Working' LIMIT 20
```

## Expected Result

Sample set empty or explained by flow criteria.

## Negative Validation

Cases outside flow criteria.

## QA Recommendation

Tune filter to flow entry conditions.

## Related Documents

- [examples/README.md](README.md)
- [SKILL.md](../SKILL.md)
