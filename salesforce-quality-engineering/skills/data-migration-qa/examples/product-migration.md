---
title: Product Migration
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

# Product Migration

## Business Scenario

Migrate Product2 / PricebookEntry catalog.

## Source Data

Legacy product catalog and price lists.

## Target Data Model

Product2; Pricebook2; PricebookEntry.

## Mapping Rules

SKU → ProductCode/External ID; pricebook map.

## Transformation Rules

Active flags; currency; unit of measure.

## Validation Strategy

SKU uniqueness; pricebook completeness.

## SOQL Verification

SOVA: duplicate ProductCode; missing standard PBE.

## Expected Results

Catalog complete per scope; prices match fixtures.

## Negative Scenarios

Inactive product still sold; currency mismatch.

## QA Recommendations

Chain MIA for product custom fields; CPQ example if package data.
