---
title: Legacy CRM to Sales Cloud
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

# Legacy CRM to Sales Cloud

## Business Scenario

Migrate Accounts, Contacts, and Opportunities from legacy CRM to Sales Cloud.

## Source Data

Legacy Account/Contact/Opportunity tables with legacy keys.

## Target Data Model

Account, Contact, Opportunity; External ID LegacyCRM_Id__c.

## Mapping Rules

Legacy key → External ID; Owner map; Stage map.

## Transformation Rules

Currency normalize; closed date timezone; Stage picklist map.

## Validation Strategy

Counts by object; parent-child integrity; sample Opportunity amounts.

## SOQL Verification

SOVA stubs: COUNT by External ID; orphan Opportunity; duplicate External ID.

## Expected Results

Counts within tolerance; no orphans; stages mapped.

## Negative Scenarios

Duplicate External ID; inactive owner; missing parent Account.

## QA Recommendations

Chain MIA for External ID fields; PTA for sales personas; SOVA for section 16.
