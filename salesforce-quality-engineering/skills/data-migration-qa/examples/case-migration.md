---
title: Case Migration
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

# Case Migration

## Business Scenario

Migrate open and historical Cases to Service Cloud.

## Source Data

Legacy tickets with customer/account keys.

## Target Data Model

Case; Account/Contact lookups; Status/Origin maps.

## Mapping Rules

Legacy ticket # → External ID; Status map; Priority map.

## Transformation Rules

Closed Date rules; comment migration policy (TBC).

## Validation Strategy

Open vs closed counts; entitlement fields if any (TBC).

## SOQL Verification

SOVA: Case by Status; null AccountId; duplicate External ID.

## Expected Results

Statuses mapped; parents resolved.

## Negative Scenarios

Unauthorized agent sees Cases (PTA); attachment missing.

## QA Recommendations

Chain PTA for agent profiles; Sprint 9 if post-go-live Case Sev1.
