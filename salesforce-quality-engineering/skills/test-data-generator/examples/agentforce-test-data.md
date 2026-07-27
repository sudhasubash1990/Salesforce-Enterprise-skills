---
title: Agentforce Test Data
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

# Agentforce Test Data

## Business Scenario

CRM records for Agentforce conversation actions (read/update Case).

## Required Objects

Account, Contact, Case, Knowledge (optional)

## Relationships

Case→Account/Contact; Knowledge for grounding (if used)

## Sample Data (Synthetic)

Case TDG-AF-001 Subject='Billing question TEST'; Knowledge title synthetic

## Validation Rules

No real customer utterances with PII.

## Expected Results

Agent can resolve Case Id via SOQL stub.

## Recommended SOQL

```sql
SELECT Id, Subject, Status FROM Case WHERE External_Id__c = 'TDG-AF-001'
```

## QA Recommendations

Chain AFT for conversation QA; TDG owns seed only.
