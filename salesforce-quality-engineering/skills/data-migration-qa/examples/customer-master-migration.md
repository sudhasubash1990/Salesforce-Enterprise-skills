---
title: Customer Master Migration
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

# Customer Master Migration

## Business Scenario

Golden customer master load into Account (Household/Business).

## Source Data

MDM customer export with survivorship flags.

## Target Data Model

Account (+ record types); Contact optional link.

## Mapping Rules

MDM ID → External ID; record type map; address standardization.

## Transformation Rules

Survivorship rules; name/address cleanse.

## Validation Strategy

Uniqueness on External ID; DQ completeness; ownership.

## SOQL Verification

SOVA: duplicate External ID; null required Name.

## Expected Results

One Account per MDM ID; cleansed addresses.

## Negative Scenarios

Conflicting survivorship; blank Name; wrong record type.

## QA Recommendations

Chain TDG for masked dry-run; PTA for customer service visibility.
