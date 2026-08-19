---
title: "Scenario: LWC Routing"
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test Scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [lwc-flow-ui-testing, test]
---

# Scenario — LWC Routing

## Purpose

Validate that LWC-related keywords route to LFUT skill.

## Test Cases

| # | Input | Expected Route | Pass/Fail |
|---|-------|---------------|-----------|
| 1 | "Test the customerSearchLWC component" | LFUT | |
| 2 | "Validate lightning-datatable rendering" | LFUT | |
| 3 | "Check Shadow DOM behavior for custom LWC" | LFUT | |
| 4 | "Review toast message after record save in LWC" | LFUT | |
| 5 | "Test lightning-input validation in my component" | LFUT | |
| 6 | "Analyze conditional rendering in Lightning Web Component" | LFUT | |
| 7 | "Test Lightning Message Service communication" | LFUT | |

## Negative Cases

| # | Input | Expected Route |
|---|-------|---------------|
| 1 | "Review my Playwright test scripts" | PWR (not LFUT) |
| 2 | "Generate permission matrix for Service Agent" | PTA (not LFUT) |
| 3 | "Validate SOQL query returns correct accounts" | SOVA (not LFUT) |
