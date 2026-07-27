---
title: Crew Management Testing Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.19.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [field-service-testing, playbook]
---

# Crew Management Testing Playbook

## Objective

Validate crew composition and multi-resource scheduling.

## Inputs

- Crews
- Members
- Capacity rules

## Validation Workflow

- Schedule crew SA.
- Remove member mid-plan.
- Validate capacity.

## Decision Points

- Mixed skill crews?

## Deliverables

- Crew section in FSL report

## Expected Results

- Unavailable member blocked

## Escalation Rules

- Capacity defect → FSL Architect
