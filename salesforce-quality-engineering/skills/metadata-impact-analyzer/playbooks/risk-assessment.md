---
title: Risk Assessment
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

# Risk Assessment

## Purpose

Score and document deployment and regression risks with evidence.

## Inputs

- Impact report
- Historical defect data (if available)
- Environment path

## Workflow

- Rate Business, Technical, Security, Integration, Automation, Reporting dimensions.
- Roll up to overall Risk Rating (Low/Medium/High/Critical).
- Document mitigations and residual risk.

## Decision Points

- Acceptable residual risk?
- Mitigation owner assigned?

## Outputs

- Risk matrix
- Escalation triggers

## Deliverables

- deployment-risk-report.md

## Escalation

- Critical → steering / CAB escalation

## Related Documents

- [SKILL.md](../SKILL.md)
- [playbooks/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial playbook |
