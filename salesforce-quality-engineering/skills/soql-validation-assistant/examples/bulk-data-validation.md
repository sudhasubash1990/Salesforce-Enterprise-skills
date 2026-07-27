---
title: Bulk Data Validation
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

# Bulk Data Validation

## Business Scenario

Data Loader upsert 10k Contacts.

## Validation Objective

No duplicate emails in batch scope.

## Generated SOQL

```sql
SELECT Email, COUNT(Id) FROM Contact WHERE LastModifiedDate = TODAY GROUP BY Email HAVING COUNT(Id) > 1
```

## Expected Result

Zero duplicate emails in scope.

## Negative Validation

Null emails grouped separately.

## QA Recommendation

Sample LIMIT if LDV.

## Related Documents

- [examples/README.md](README.md)
- [SKILL.md](../SKILL.md)
