---
title: Opportunity Sales Pipeline
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

# Opportunity Sales Pipeline

## Business Scenario

UAT pipeline with Open and Closed Won opportunities.

## Required Objects

Account, Contact, Opportunity, OpportunityContactRole

## Relationships

Account→Opportunity; Contact via OCR

## Sample Data (Synthetic)

Opp TDG-OPP-001 Stage=Prospecting; TDG-OPP-002 Stage=Closed Won Amount=10000

## Validation Rules

Amount required when Closed Won (assume org VR).

## Expected Results

Stages valid; Closed Won has Amount.

## Recommended SOQL

```sql
SELECT Id, StageName, Amount FROM Opportunity WHERE External_Id__c LIKE 'TDG-OPP-%'
```

## QA Recommendations

Negative pack: Closed Won with null Amount.
