---
title: Historical Billing Data Migration
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

# Historical Billing Data Migration

## Business Scenario

Archive/historical invoice lines into Salesforce custom objects or Big Object (TBC).

## Source Data

Multi-year invoice history extracts.

## Target Data Model

Custom historical objects or Big Object (confirm with Architect).

## Mapping Rules

Invoice # + line → External ID; Account External ID.

## Transformation Rules

Period bucketing; amount scale; status archive map.

## Validation Strategy

Volume reconcile by year; sample line accuracy; performance assumptions labeled.

## SOQL Verification

SOVA: COUNT by Year__c; SUM(Amount); unresolved Account.

## Expected Results

Yearly totals within tolerance; samples accurate.

## Negative Scenarios

LDV timeout (label assumption); wrong year bucket; PII in memo.

## QA Recommendations

Do not invent load duration; chain LDV knowledge; confirm Big Object vs custom.
