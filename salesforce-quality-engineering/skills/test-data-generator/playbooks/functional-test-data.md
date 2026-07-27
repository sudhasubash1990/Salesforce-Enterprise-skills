---
title: Functional Test Data Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.20.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [test-data-generator, playbook]
---

# Functional Test Data Playbook

## Objective

Generate happy-path and key negative data for functional tests.

## Inputs

- AC / scenarios
- Record types
- Known VRs

## Validation Workflow

- Map scenarios to objects.
- Build compliant positive rows.
- Add targeted negatives.
- Provide SOQL stubs.

## Decision Points

- Automation side effects unknown?

## Deliverables

- Data Generation Report
- Sample CSV/JSON

## Expected Results

- Referential integrity held
- Positive rows VR-compliant

## Escalation Rules

- Org VR unknown → Admin/BA
