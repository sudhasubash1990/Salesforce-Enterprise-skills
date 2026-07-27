---
title: Product Configuration
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.22.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [omnistudio-qa, example]
---

# Product Configuration

## Business Scenario

CPQ/EPC-style product configuration via OmniStudio.

## OmniStudio Components

OmniScript ProductConfig; Decision Matrix Options; Calculation Procedure Price; FlexCard Cart.

## Test Objectives

Validate option rules and calculation accuracy with fixtures.

## Test Scenarios

Base + add-on; incompatible options; quantity edges.

## Backend Validation

Expected calc fixtures from TDG; no invented prices.

## Expected Results

Cart totals match fixtures; incompatible blocked.

## Negative Scenarios

Zero quantity; missing price book; expression error.

## QA Recommendations

Do not invent EPC catalog — label TBC.
