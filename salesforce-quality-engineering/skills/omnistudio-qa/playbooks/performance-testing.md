---
title: Performance Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.22.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [omnistudio-qa, playbook]
---

# Performance Testing

## Objective

Assess OmniStudio performance risks with evidence or labeled assumptions.

**Pointer:** knowledge/performance-best-practices.md

## Inputs

- Component inventory
- Known bottlenecks
- Any measured timings (optional)

## Validation Workflow

- Identify chatty DR/IP and oversized JSON.
- Note FlexCard nesting/refresh risks.
- Recommend measurement approach.
- Populate Performance Assessment without inventing %.

## Decision Points

- Any numeric SLA without evidence → remove or label assumption.

## Deliverables

- Performance Assessment section
- Risks for known bottlenecks

## Expected Results

- Assumptions labeled; no invented SLA %

## Escalation Rules

- Prod latency Sev1 → Production support / Omni Architect
