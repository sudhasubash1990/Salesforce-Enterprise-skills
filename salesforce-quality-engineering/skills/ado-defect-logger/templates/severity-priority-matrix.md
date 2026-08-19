---
title: Severity-Priority Matrix Template
module: Salesforce Quality Engineering
category: QE Specialized Skill Template
document_type: Template
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, severity-priority-matrix]
---

# Severity × Priority Matrix

## Decision Matrix

| | Priority 1 (Critical) | Priority 2 (High) | Priority 3 (Medium) | Priority 4 (Low) |
|---|---|---|---|---|
| **Sev 1 (Critical)** | P1-S1: Fix immediately, war room | P1-S1: Fix immediately | Unusual — re-validate | Unusual — re-validate |
| **Sev 2 (High)** | Fix this sprint, daily status | Fix this/next sprint | Backlog (high priority) | Re-validate classification |
| **Sev 3 (Medium)** | Unusual — re-validate | Fix next sprint | Backlog | Backlog (low) |
| **Sev 4 (Low)** | Unusual — re-validate | Re-validate classification | Backlog (low) | Backlog (low) |

## Response Time Guidelines

| Classification | Initial Response | Fix Target |
|----------------|-----------------|------------|
| P1-S1 | Immediate | Same day |
| P1-S2 / P2-S1 | < 4 hours | Current sprint |
| P2-S2 | < 1 business day | Next sprint |
| P3-S3 | Triage meeting | Backlog prioritization |
| P4-S4 | Next triage cycle | When convenient |

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
