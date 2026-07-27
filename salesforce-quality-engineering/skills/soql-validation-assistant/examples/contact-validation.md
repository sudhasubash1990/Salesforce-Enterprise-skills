---
title: Contact Validation
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

# Contact Validation

## Business Scenario

Primary contact flag unique per Account.

## Validation Objective

At most one Primary_Contact__c per Account.

## Generated SOQL

```sql
SELECT AccountId, COUNT(Id) cnt FROM Contact WHERE Primary_Contact__c = true GROUP BY AccountId HAVING COUNT(Id) > 1
```

## Expected Result

Zero groups.

## Negative Validation

Accounts with zero primary — business rule dependent.

## QA Recommendation

Fix duplicate primaries before release.

## Related Documents

- [examples/README.md](README.md)
- [SKILL.md](../SKILL.md)
