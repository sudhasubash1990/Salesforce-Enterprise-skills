---
title: Quote Generation
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

# Quote Generation

## Business Scenario

Sales quote generation through Industries guided flow.

## OmniStudio Components

OmniScript QuoteGen; DR Load QuoteLine; IP SubmitQuote; Decision Table Discounts.

## Test Objectives

Validate quote lines, discounts, and submit.

## Test Scenarios

Standard quote; discount path; multi-product.

## Backend Validation

SOVA: Quote / QuoteLineItem fields.

## Expected Results

Quote submitted; lines match JSON.

## Negative Scenarios

Discount over limit; submit failure; FLS on amount.

## QA Recommendations

Chain PTA for amount fields; SOVA for CRM proof.
