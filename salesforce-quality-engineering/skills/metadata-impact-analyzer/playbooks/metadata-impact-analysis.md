---
title: Metadata Impact Analysis
module: Salesforce Quality Engineering
category: Specialized Skill Playbook
document_type: Playbook
version: 0.15.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [metadata-impact-analyzer, playbook]
---

# Metadata Impact Analysis

## Purpose

Execute end-to-end metadata dependency and impact analysis before test design.

## Inputs

- Change manifest or diff
- Target environment context
- Persona list
- Release window

## Workflow

- Load SKILL.md and classify metadata types.
- Build dependency graph (objects → fields → automation → security → integration → reporting).
- Produce 16-section impact report using template.
- Derive regression scope In/Out/Conditional.
- Issue Go/No-Go with evidence.

## Decision Points

- Is dependency graph complete?
- Any Critical security or integration risk?
- Destructive change present?

## Outputs

- Metadata Impact Report
- Risk rating
- SOQL validation pack

## Deliverables

- metadata-impact-report.md
- regression-report.md

## Escalation

- Critical risk → Solution Architect
- Security model change → Security Architect

## Related Documents

- [SKILL.md](../SKILL.md)
- [playbooks/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial playbook |
