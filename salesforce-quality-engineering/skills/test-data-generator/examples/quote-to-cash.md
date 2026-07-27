---
title: Quote to Cash
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

# Quote to Cash

## Business Scenario

Quote from Opportunity through Order handoff (synthetic).

## Required Objects

Account, Opportunity, Quote, QuoteLineItem, Order

## Relationships

Opp→Quote→QLI; Order from Opp/Account

## Sample Data (Synthetic)

Quote TDG-QT-001 Status=Draft; QLI for SKU-TEST-01

## Validation Rules

Synced quote fields org-specific — label assumptions.

## Expected Results

Quote lines reference valid PBE.

## Recommended SOQL

```sql
SELECT Id, QuoteId FROM QuoteLineItem WHERE Quote.External_Id__c = 'TDG-QT-001'
```

## QA Recommendations

CPQ objects only if licensed — otherwise standard Quote.
