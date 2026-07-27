---
title: Contact Migration
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.23.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [data-migration-qa, example]
---

# Contact Migration

## Business Scenario

Migrate Contacts linked to migrated Accounts.

## Source Data

Legacy Contact with Account foreign key.

## Target Data Model

Contact; AccountId via External ID upsert.

## Mapping Rules

Email/phone normalize; Account External ID resolve.

## Transformation Rules

Primary flag; email lowercase; phone E.164 (if required).

## Validation Strategy

Parent resolve; duplicate email policy; FLS on email.

## SOQL Verification

SOVA: Contacts with null AccountId; duplicate Email.

## Expected Results

All Contacts linked; duplicates per policy.

## Negative Scenarios

Missing parent; invalid email; PII in notes.

## QA Recommendations

Chain PTA for email FLS; SOVA for orphans.
