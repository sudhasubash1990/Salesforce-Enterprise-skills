---
title: Lead Conversion
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

# Lead Conversion

## Business Scenario

Lead ready for conversion testing plus converted outcome set.

## Required Objects

Lead, Account, Contact, Opportunity

## Relationships

Conversion creates Account/Contact/Opp

## Sample Data (Synthetic)

Lead TDG-LEAD-001 Company=Test Co Email=lead@example.test

## Validation Rules

Required Company/Email; duplicate rules may block — plan unique emails.

## Expected Results

Convert succeeds; related records created.

## Recommended SOQL

```sql
SELECT Id, IsConverted, ConvertedAccountId FROM Lead WHERE Email = 'lead@example.test'
```

## QA Recommendations

Negative: duplicate Lead email.
