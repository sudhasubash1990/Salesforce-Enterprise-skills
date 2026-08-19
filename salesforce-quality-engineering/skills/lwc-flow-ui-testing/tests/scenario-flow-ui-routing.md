---
title: "Scenario: Flow UI Routing"
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

# Scenario — Flow UI Routing

## Purpose

Validate that Flow UI keywords route to LFUT skill.

## Test Cases

| # | Input | Expected Route | Pass/Fail |
|---|-------|---------------|-----------|
| 1 | "Test the Case Creation Screen Flow" | LFUT | |
| 2 | "Validate flow navigation back and cancel" | LFUT | |
| 3 | "Check flow input screen required fields" | LFUT | |
| 4 | "Test flow fault path error messages" | LFUT | |
| 5 | "Validate flow conditional visibility" | LFUT | |
| 6 | "Test flow resume behavior after pause" | LFUT | |

## Negative Cases

| # | Input | Expected Route |
|---|-------|---------------|
| 1 | "Review Playwright automation for flow" | PWR (not LFUT) |
| 2 | "Test OmniScript flow" | OmniStudio QA (not LFUT) |
