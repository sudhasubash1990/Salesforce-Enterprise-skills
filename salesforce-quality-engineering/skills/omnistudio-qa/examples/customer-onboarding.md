---
title: Customer Onboarding
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

# Customer Onboarding

## Business Scenario

New customer completes Industries onboarding guided flow across Account/Contact creation.

## OmniStudio Components

OmniScript Onboarding; DR Extract Account; DR Load Contact; IP CreateCustomer; FlexCard Status.

## Test Objectives

Validate end-to-end onboarding, Data JSON, CRM creates, and Experience access.

## Test Scenarios

Happy path steps; conditional KYC branch; Save for Later; submit success.

## Backend Validation

SOVA stubs: Account/Contact created with expected fields; IP response codes.

## Expected Results

Customer record created; OS completes; FlexCard shows Active.

## Negative Scenarios

Duplicate email; missing required; remote timeout; unauthorized Experience user.

## QA Recommendations

Chain PTA for Experience; TDG for seed; PWR for UI automation.
