---
title: "Scenario: Playwright Chain"
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

# Scenario — Playwright Chain

## Purpose

Validate that LFUT correctly chains to PWR for automation and does not generate Playwright scripts itself.

## Test Cases

| # | Trigger | Expected LFUT Behavior | Expected PWR Chain |
|---|---------|----------------------|-------------------|
| 1 | "Generate Playwright tests for my LWC" | Produce 13-section test analysis with locator map | Recommend chaining PWR; do not generate scripts |
| 2 | "Automate the case creation flow" | Produce Flow UI test report with sync patterns | Recommend PWR chain for automation |
| 3 | "I need Playwright page objects for datatable" | Provide component analysis and locator strategy | Hand off to PWR for POM generation |

## Anti-Pattern Detection

| # | Input | Anti-Pattern | Expected |
|---|-------|-------------|----------|
| 1 | User asks LFUT for Playwright code | Generating `.spec.ts` files | LFUT must not produce Playwright code; chain PWR |
| 2 | User asks LFUT for CI config | Generating pipeline YAML | LFUT must not produce CI config; chain PWR |
