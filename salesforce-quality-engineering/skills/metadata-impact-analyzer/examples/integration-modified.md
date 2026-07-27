---
title: Integration Modified
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

# Integration Modified

## Input

**Change:** Named Credential `ERP_Sync` endpoint URL changed; Connected App callback updated for OAuth.

Apex class `ErpSyncBatch` uses Named Credential. Experience Cloud login uses Connected App.

## Expected Analysis (Dependency First)

- URL change affects all callouts using NC.
- OAuth callback mismatch breaks login.
- Certificate rotation may be required — confirm with integration team.

## Expected Regression

| Scope | Rationale |
|-------|-----------|
| In | ErpSyncBatch successful callout |
| In | OAuth login to Experience Cloud |
| In | Negative: invalid credential handling |

## Expected Risk

**Rating:** Critical

## Expected SOQL Validations

```sql
SELECT Id, DeveloperName, Endpoint FROM NamedCredential WHERE DeveloperName = 'ERP_Sync'
```

## Related Documents

- [SKILL.md](../SKILL.md)
- [examples/README.md](README.md)
