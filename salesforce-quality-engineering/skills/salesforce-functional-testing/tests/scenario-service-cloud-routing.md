---
title: Service Cloud Routing Test
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

# Service Cloud Routing Test

## Objective

Verify that prompts containing Service Cloud keywords (case, escalation, Omni-Channel, Email-to-Case, Web-to-Case, entitlement, SLA) route to the SFT skill and load Service Cloud knowledge.

## Pass Criteria

- SFT skill activated when prompt mentions "case assignment testing"
- Service Cloud testing knowledge loaded
- Output contains Case object in Object/Feature Coverage
- Positive, negative, and boundary scenarios generated for case lifecycle
- PTA chained when personas with different case access are specified

## Fail Criteria

- Skill not activated for Service Cloud keywords
- Output missing negative or boundary scenarios
- Permission scenarios generated inline instead of chaining PTA
- Vague expected results (e.g., "case works correctly")
- Coverage percentage invented without evidence
