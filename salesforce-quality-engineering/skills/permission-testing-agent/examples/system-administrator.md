---
title: System Administrator
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

# System Administrator

## Business Scenario

Admin deploy — verify least privilege not expanded accidentally.

## Security Requirement

Admin retains full access — use only for setup proof not business sign-off.

## Validation Strategy

Document admin vs business persona separation.

## Expected Result

Admin can access all test records.

## Negative Validation

Business user matrix is authoritative for UAT.

## Recommended SOQL

```sql
N/A — use business persona SOQL
```

## QA Recommendations

Never sign off business rules as admin only.
