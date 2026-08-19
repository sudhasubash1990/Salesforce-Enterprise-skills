---
title: Cross-Skill Chain Test
module: Salesforce Quality Engineering
category: QE Specialized Skill Test Scenario
document_type: Test Scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, test-scenario]
---

# Cross-Skill Chain Test

## Objective

Verify that SFT correctly chains downstream skills (PTA, SOVA, TDG, PWR) rather than duplicating their capabilities inline.

## Pass Criteria

- Permission scenarios reference PTA with explicit chain instruction
- Backend verification references SOVA with SOQL context
- Test data prerequisites reference TDG with data requirements
- UI automation references PWR with flow description
- No inline CRUD/FLS matrix generated (PTA responsibility)
- No inline SOQL queries generated (SOVA responsibility)

## Fail Criteria

- Full CRUD/FLS permission matrix generated inside SFT output
- SOQL queries written inline instead of chaining SOVA
- Test data creation steps detailed instead of chaining TDG
- Playwright locators or scripts included instead of chaining PWR
