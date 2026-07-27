---
title: CRUD Validation Playbook
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

# CRUD Validation Playbook

## Objective

Validate object CRUD per persona across channels.

**Pointer:** [../../knowledge/security/object-level-security.md](../../knowledge/security/object-level-security.md)

## Inputs

- Persona list
- Object inventory
- Channel UI/API

## Validation Workflow

- Build CRUD matrix.
- Execute positive/negative per cell.
- Document gaps and excessive access.

## Decision Points

- All objects in scope?
- API tested separately?

## Deliverables

- CRUD Matrix
- Permission Validation Report

## Expected Results

- Matrix complete with Pass/Fail
- No unexplained Modify All

## Escalation Rules

- Excessive CRUD → Security Architect
