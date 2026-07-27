---
title: Deployment Review
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

# Deployment Review

## Purpose

Review deployment package readiness from QE and release perspectives.

## Inputs

- package.xml or change set list
- Prior sandbox test evidence
- Rollback plan

## Workflow

- Validate manifest vs dependency graph.
- Check deployment ordering (fields before VR, etc.).
- Confirm smoke and regression evidence.
- Produce Deployment Risk Report.

## Decision Points

- Missing dependencies?
- Destructive changes?
- Test evidence sufficient?

## Outputs

- Deployment Risk Report
- Residual risk list

## Deliverables

- deployment-risk-report.md

## Escalation

- High deployment risk → Release Manager hold

## Related Documents

- [SKILL.md](../SKILL.md)
- [playbooks/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial playbook |
