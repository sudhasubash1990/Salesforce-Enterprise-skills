---
title: Locator Optimization Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.21.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [playwright-review, playbook]
---

# Locator Optimization Playbook

## Objective

Harden locators for Lightning and Experience UI.

**Pointer:** [../../metadata-impact-analyzer/SKILL.md](../../metadata-impact-analyzer/SKILL.md)

## Inputs

- Failing locators
- UI samples
- MIA UI deltas

## Validation Workflow

- Classify brittle selectors.
- Recommend role/label/test-id.
- Chain MIA if layout changed.
- Update Locator Review.

## Decision Points

- Can product add data-testid?

## Deliverables

- Locator Review Checklist

## Expected Results

- Brittleness reduced or accepted residual risk

## Escalation Rules

- Layout churn → MIA + Product
