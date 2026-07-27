---
title: Experience Cloud Users
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

# Experience Cloud Users

## Business Scenario

Community user seed linked to Contact/Account for portal tests.

## Required Objects

Account, Contact, User (community), Profile/Perm Set refs

## Relationships

User→Contact→Account

## Sample Data (Synthetic)

Contact portal.user@example.test; User Username unique in org

## Validation Rules

License and profile must exist — do not invent.

## Expected Results

User active and linked to Contact.

## Recommended SOQL

```sql
SELECT Id, ContactId, IsActive FROM User WHERE Username LIKE 'portal.user%@example.test'
```

## QA Recommendations

Chain PTA for guest vs member access; never real emails.
