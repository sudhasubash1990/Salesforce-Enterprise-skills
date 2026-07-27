---
title: Utilities Billing Migration
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

# Utilities Billing Migration

## Business Scenario

Migrate customer and billing account history for utilities Industries org.

## Source Data

CIS billing accounts, service points, historical invoices (summarized).

## Target Data Model

Account, custom Billing objects (API TBC), Service Point references.

## Mapping Rules

CIS ID → External ID; service point lookup resolve.

## Transformation Rules

Tariff code map; invoice status map; amount scale.

## Validation Strategy

Financial aggregate reconcile; relationship integrity; sample invoice.

## SOQL Verification

SOVA: SUM(Amount) by period; unresolved service point lookups.

## Expected Results

Financial totals within tolerance; lookups resolved.

## Negative Scenarios

Currency scale error; orphan invoice; PII in free text.

## QA Recommendations

Label utility object APIs TBC; chain OSQA if Omni journeys consume billing data.
