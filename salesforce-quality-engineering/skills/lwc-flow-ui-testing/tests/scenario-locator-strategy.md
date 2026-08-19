---
title: "Scenario: Locator Strategy"
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

# Scenario — Locator Strategy Enforcement

## Purpose

Validate that LFUT enforces semantic locator preference and flags anti-patterns.

## Test Cases

| # | Input | Expected Behavior | Pass/Fail |
|---|-------|-------------------|-----------|
| 1 | Component with labeled inputs | Recommend `getByRole`/`getByLabel` locators | |
| 2 | Component with `data-id` attributes | Accept as tier-3 stable alternative | |
| 3 | User proposes deep CSS: `.slds-grid > div:nth-child(3) > lightning-input` | Flag as brittle; recommend semantic alternative | |
| 4 | User proposes XPath: `//div[@class='slds-form']//input[2]` | Flag as anti-pattern; recommend label-based | |
| 5 | Shadow DOM component | Recommend semantic locators; note shadow boundary | |

## Anti-Pattern Detection

- [ ] No absolute XPath recommended
- [ ] No index-based CSS selectors recommended
- [ ] No `waitForTimeout()` as primary sync strategy
- [ ] Hard waits flagged with condition-based alternative
