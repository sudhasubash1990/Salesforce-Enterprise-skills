---
title: Apex Sharing
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

# Apex Sharing

## Business Scenario

Apex without sharing creates shared custom object rows.

## Security Requirement

Users see records created by batch job per sharing model.

## Validation Strategy

Identify Apex keyword; test resulting visibility.

## Expected Result

Records visible per sharing design.

## Negative Validation

Wrong keyword → over-exposure.

## Recommended SOQL

```sql
Document Apex class sharing mode; manual record checks
```

## QA Recommendations

Code review + QA visibility matrix.
