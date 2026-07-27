---
title: CI/CD Review Playbook
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

# CI/CD Review Playbook

## Objective

Review pipeline readiness for Playwright suites.

## Inputs

- YAML/pipeline
- Secrets approach
- Artifact publish

## Validation Workflow

- Check install/cache/browsers.
- Artifacts on fail.
- Smoke gate vs full suite.
- Score CI/CD Readiness.

## Decision Points

- ADO or GitHub Actions?

## Deliverables

- CI/CD Readiness Report

## Expected Results

- Secrets not in logs
- Artifacts available

## Escalation Rules

- No CI for critical smoke → DevOps
