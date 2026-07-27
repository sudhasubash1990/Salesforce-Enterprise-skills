---
title: Custom Field Added
module: Salesforce Quality Engineering
category: Specialized Skill Example
document_type: Example
version: 0.15.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [metadata-impact-analyzer, example]
---

# Custom Field Added

## Input

**Change:** New custom picklist field `Account.Service_Tier__c` on Account; added to Account page layout and one Record-Triggered Flow entry criteria.

Package adds `Account.Service_Tier__c` (Picklist). Layout: Account-Enterprise Layout. Flow: `Account_Tier_Routing` (Record-Triggered, Update).

## Expected Analysis (Dependency First)

- Field referenced by Flow entry criteria — Flow must deploy after field.
- Layout section change affects Enterprise persona UI only if layout assignment unchanged.
- Reports using Account fields may need new column — scan report dependencies.

## Expected Regression

| Scope | Rationale |
|-------|-----------|
| In | Account create/update with each picklist value |
| In | Flow routing when Service_Tier changes |
| Conditional | Report exports if finance reports use Account |

## Expected Risk

**Rating:** Medium

## Expected SOQL Validations

```sql
SELECT Id, Service_Tier__c FROM Account WHERE Service_Tier__c != null LIMIT 10
```
```sql
SELECT Id, MasterLabel, Status FROM Flow WHERE Definition.DeveloperName = 'Account_Tier_Routing'
```

## Related Documents

- [SKILL.md](../SKILL.md)
- [examples/README.md](README.md)
