---
title: Release Validation Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.16.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [soql-validation, playbook]
---

# Release Validation Playbook

## Objective

Post-deploy SOQL verification for release gate.

## Inputs

- Release notes
- Deploy manifest
- Smoke personas

## Validation Workflow

- Execute release validation checklist queries.
- Compare to pre-deploy baseline where available.
- Support Go/No-Go with evidence.

## Decision Points

- Production query allowed?
- [../../knowledge/release/production-verification.md](../../knowledge/release/production-verification.md)

## Deliverables

- Release Validation Checklist
- SOQL Validation Report

## Expected Results

- Critical metrics green
- No orphan or duplicate anomalies

## Escalation Rules

- Production anomaly → Release Manager Sev2

## Related Documents

- [SKILL.md](../SKILL.md)
