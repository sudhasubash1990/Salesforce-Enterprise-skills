---
title: Experience Cloud Routing Test
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

# Experience Cloud Routing Test

## Objective

Verify that prompts containing Experience Cloud keywords (portal, guest user, community, self-service, experience builder) route to the SFT skill and load Experience Cloud knowledge.

## Pass Criteria

- SFT skill activated when prompt mentions "portal case creation testing"
- Experience Cloud testing knowledge loaded
- Output includes guest user restriction scenarios
- Negative authorization scenarios present
- PTA chained for external user CRUD/FLS validation

## Fail Criteria

- Skill not activated for Experience Cloud keywords
- Guest user testing omitted
- Negative authorization missing (e.g., accessing other users' records)
- Internal user profiles used instead of external user profiles
- Permission matrix duplicated instead of chaining PTA
