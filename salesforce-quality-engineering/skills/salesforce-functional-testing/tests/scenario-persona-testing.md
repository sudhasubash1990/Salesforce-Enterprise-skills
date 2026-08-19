---
title: Persona Testing Test
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

# Persona Testing Test

## Objective

Verify that persona-based prompts produce a persona matrix with positive, negative, and cross-persona scenarios per profile/permission set combination.

## Pass Criteria

- Persona matrix table generated with Profile, Permission Sets, Role, Key Permissions
- Positive scenarios confirm permitted actions per persona
- Negative scenarios confirm restricted actions are blocked per persona
- Cross-persona record visibility scenarios included
- PTA chained for detailed CRUD/FLS matrix

## Fail Criteria

- Testing performed only with System Administrator profile
- No negative persona scenarios (only happy path)
- Role hierarchy assumed to grant field-level access
- Guest user / external user persona omitted when Experience Cloud in scope
