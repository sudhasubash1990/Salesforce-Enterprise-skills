---
title: Experience Cloud User Migration
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

# Experience Cloud User Migration

## Business Scenario

Migrate community users and Contact/Account links.

## Source Data

Legacy portal users with email and profile keys.

## Target Data Model

User; Contact; Account; Profile/Permission Set assignment.

## Mapping Rules

Email → Username policy; Contact External ID; profile map.

## Transformation Rules

Activation flags; locale/timezone defaults.

## Validation Strategy

Login persona visibility; FLS; no PII leakage in error logs.

## SOQL Verification

SOVA: User-Contact link; duplicate Username.

## Expected Results

Users linked; profiles correct.

## Negative Scenarios

Guest sees restricted data; duplicate Username; inactive Contact.

## QA Recommendations

Chain PTA heavily; never migrate real passwords — document IdP approach TBC.
