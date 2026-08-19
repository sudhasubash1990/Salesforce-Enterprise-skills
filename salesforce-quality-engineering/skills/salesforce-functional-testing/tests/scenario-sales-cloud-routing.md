---
title: Sales Cloud Routing Test
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

# Sales Cloud Routing Test

## Objective

Verify that prompts containing Sales Cloud keywords (lead conversion, opportunity stages, campaign, forecast, price book) route to the SFT skill and load Sales Cloud knowledge.

## Pass Criteria

- SFT skill activated when prompt mentions "lead conversion testing"
- Sales Cloud testing knowledge loaded
- Output contains Lead and Opportunity in Object/Feature Coverage
- Lead conversion scenarios include new and existing Account matching
- SOVA chained for post-conversion record verification

## Fail Criteria

- Skill not activated for Sales Cloud keywords
- Lead conversion tested only with new records
- Forecast validation missing after stage change scenarios
- Expected results not measurable
- Coverage percentage invented
