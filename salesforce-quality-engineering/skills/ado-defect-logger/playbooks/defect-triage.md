---
title: Defect Triage Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, defect-triage]
---

# Defect Triage Playbook

Process for triaging and prioritizing logged defects.

## Triage Checklist

### 1. Classification

- Is this a valid defect, duplicate, enhancement, or question?
- Which defect category applies? (Functional, UI, Integration, etc.)
- Which Salesforce Cloud / module is affected?

### 2. Severity Assessment

- What is the technical impact? (data loss, crash, partial failure, cosmetic)
- How many users are affected?
- Is there a workaround?
- See [severity-priority-model](../knowledge/severity-priority-model.md)

### 3. Priority Assessment

- What is the business urgency?
- Does this block release or UAT?
- Is there a compliance or regulatory dimension?
- What is the cost of delay?

### 4. Assignment

- Which team or individual should own the fix?
- Is additional investigation needed before assignment?
- Are there dependencies on other defects or stories?

### 5. Escalation Check

| Condition | Action |
|-----------|--------|
| Sev1 in production | Escalate to Release Manager + Production Support |
| Security vulnerability | Escalate to Security Architect |
| Data corruption | Escalate to Data Architect |
| Blocks go-live | Escalate to Program Manager |

### 6. Disposition

| Disposition | When |
|-------------|------|
| Fix this sprint | Sev1-2 / Priority 1-2 |
| Fix next sprint | Priority 2-3 with workaround |
| Backlog | Priority 3-4, non-blocking |
| Reject | Not a defect, duplicate, or by design |
| Defer | Valid but out of current scope |

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
