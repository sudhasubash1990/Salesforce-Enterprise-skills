---
title: Opportunity Migration
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

# Opportunity Migration

## Business Scenario

Migrate open and closed Opportunities with products optional.

## Source Data

Legacy Opportunity + line items (optional wave).

## Target Data Model

Opportunity; OpportunityLineItem if in scope.

## Mapping Rules

Stage/probability map; Amount; CloseDate; Account External ID.

## Transformation Rules

Closed Won/Lost reason map; currency convert.

## Validation Strategy

Amount aggregates; stage distribution; Account link.

## SOQL Verification

SOVA: SUM(Amount) by Stage; orphan Opportunity.

## Expected Results

Totals match fixtures; stages mapped.

## Negative Scenarios

Negative Amount; future CloseDate on Closed Won; missing Account.

## QA Recommendations

Do not invent pricing; use fixtures; chain PWR for quote-to-cash journeys if UI critical.
