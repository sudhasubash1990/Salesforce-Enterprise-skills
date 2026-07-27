---
title: OmniStudio Journey Data
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.20.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [test-data-generator, example]
---

# OmniStudio Journey Data

## Business Scenario

JSON-shaped input payloads for OmniScript/DataRaptor rehearsal (advisory).

## Required Objects

Account, Contact, Case (targets); OmniStudio components as config (not data rows)

## Relationships

Payload maps to Account/Contact create then Case

## Sample Data (Synthetic)

Sample JSON keys: AccountName, ContactEmail=@example.test, CaseSubject

## Validation Rules

Confirm OmniStudio licensed; do not invent DataRaptor names as fact.

## Expected Results

Payload structure ready for SIT; objects creatable in order.

## Recommended SOQL

```sql
SELECT Id FROM Account WHERE Name = 'TDG Omni Test Account'
```

## QA Recommendations

Cross-link [OmniStudio QA (OSQA)](../../omnistudio-qa/SKILL.md) for journey QA; use this pack for synthetic Data JSON / seed design. Encyclopedia: [`../../../knowledge/clouds/omnistudio.md`](../../../knowledge/clouds/omnistudio.md).
