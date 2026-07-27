---
title: Experience Cloud Security Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.17.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [permission-testing, playbook]
---

# Experience Cloud Security Playbook

## Objective

Validate external user and guest access.

## Inputs

- Community profiles
- Sharing sets
- Guest user config

## Validation Workflow

- Separate matrix for external users.
- Test portal record visibility.
- Guest — minimal access verification.

## Decision Points

- Guest user in scope?
- Partner vs customer community?

## Deliverables

- Experience Cloud Security Checklist

## Expected Results

- External users cannot access internal records
- Guest cannot escalate

## Escalation Rules

- Guest change → Critical — Release Manager
