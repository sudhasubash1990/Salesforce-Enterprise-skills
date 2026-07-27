---
title: Insurance Claim Submission
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

# Insurance Claim Submission

## Business Scenario

Insurance FNOL / claim submission guided journey.

## OmniStudio Components

OmniScript ClaimSubmit; DR Extract Policy; DR Load Claim; IP ValidateCoverage; FlexCard ClaimStatus.

## Test Objectives

Validate policy lookup, claim create, coverage validation.

## Test Scenarios

In-coverage claim; out-of-coverage; multi-claimant.

## Backend Validation

SOVA: Claim / Policy related objects (API TBC).

## Expected Results

In-coverage creates claim; out-of-coverage message.

## Negative Scenarios

Expired policy; remote coverage timeout; FLS on claim amount.

## QA Recommendations

Label insurance object model TBC; chain PTA/SOVA.
