---
title: Data Mapping Review Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.23.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [data-migration-qa, playbook]
---

# Data Mapping Review Playbook

## Objective

Review field and relationship mapping completeness and correctness.

**Pointer:** knowledge/data-mapping-best-practices.md

## Inputs

- Mapping workbook
- Target schema
- Mandatory fields / VRs

## Validation Workflow

- Trace source→target for in-scope objects.
- Validate picklist/record type maps.
- Flag gaps on required fields.
- Chain MIA if new metadata needed.

## Decision Points

- Required field unmapped → Block Cutover.

## Deliverables

- Data Mapping Review section
- Transformation Validation notes

## Expected Results

- Mapping coverage documented

## Escalation Rules

- Schema mismatch blocking load → Data Architect
