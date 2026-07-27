---
title: Regression Planning
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

# Regression Planning

## Purpose

Translate metadata impact into risk-based regression scope for the specialized skill context.

**Canonical ceremony pointer:** [../../playbooks/regression-planning.md](../../playbooks/regression-planning.md)

## Inputs

- Completed Metadata Impact Report
- Release timeline
- Automation estate overview

## Workflow

- Extract impacted components from dependency analysis.
- Classify scenarios In / Out / Conditional.
- Prioritize by risk rating and business criticality.
- Identify automation candidates (design only).

## Decision Points

- Can any High area be Out of scope?
- Automation vs manual balance?

## Outputs

- Regression Report
- Automation candidate list

## Deliverables

- regression-report.md

## Escalation

- Scope dispute → Test Lead + Release Manager

## Related Documents

- [SKILL.md](../SKILL.md)
- [playbooks/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial playbook |
