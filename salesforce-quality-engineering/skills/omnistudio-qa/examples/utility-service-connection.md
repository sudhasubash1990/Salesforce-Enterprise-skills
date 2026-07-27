---
title: Utility Service Connection
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

# Utility Service Connection

## Business Scenario

Utility customer requests new service connection at premises.

## OmniStudio Components

OmniScript ServiceConnect; DR Extract Premises; IP CreateServicePoint; Decision Matrix Eligibility.

## Test Objectives

Validate eligibility decision, premises data, and service point create.

## Test Scenarios

Eligible premises; ineligible premises; multi-service select.

## Backend Validation

SOVA: ServicePoint / related utility objects as configured.

## Expected Results

Eligible path creates service point; ineligible shows message.

## Negative Scenarios

Invalid premise ID; IP branch failure; FLS on premise fields.

## QA Recommendations

Chain SOVA + PTA; label utility object API names TBC if unknown.
