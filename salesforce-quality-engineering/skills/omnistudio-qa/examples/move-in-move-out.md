---
title: Move In Move Out
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

# Move In Move Out

## Business Scenario

Utility Move In / Move Out guided journey.

## OmniStudio Components

OmniScript MoveInOut; DR Extract AccountService; IP TransferService; FlexCard Timeline.

## Test Objectives

Validate transfer logic, JSON, and CRM updates.

## Test Scenarios

Move In; Move Out; same-day both; Save for Later.

## Backend Validation

SOVA stubs for service dates and account linkage.

## Expected Results

Correct service dates; timeline card updates.

## Negative Scenarios

Overlapping dates; unauthorized user; remote fail.

## QA Recommendations

Primary reference journey for OSQA smoke demos.
