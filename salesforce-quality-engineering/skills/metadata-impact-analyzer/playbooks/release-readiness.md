---
title: Release Readiness
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

# Release Readiness

## Purpose

Assemble metadata-impact evidence into release readiness and Go-Live gates.

**Canonical ceremony pointer:** [../../knowledge/release/release-readiness.md](../../knowledge/release/release-readiness.md)

## Inputs

- Impact report
- Regression evidence
- Deployment risk report
- Open defects

## Workflow

- Complete Release Readiness Checklist.
- Confirm Go/No-Go recommendation alignment.
- Hand off to production validation playbook if Go.

## Decision Points

- All Critical risks mitigated?
- Rollback tested?

## Outputs

- Release Readiness Checklist
- Go/No-Go decision

## Deliverables

- release-readiness-checklist.md
- go-live-checklist.md

## Escalation

- No-Go → Release Manager communicates hold

## Related Documents

- [SKILL.md](../SKILL.md)
- [playbooks/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.15.0 | 2026-07-27 | QE Practice Lead | Initial playbook |
