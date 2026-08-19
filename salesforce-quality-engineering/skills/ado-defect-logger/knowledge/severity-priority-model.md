---
title: Severity and Priority Model
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, severity-priority]
---

# Severity and Priority Model

## Severity Definitions

Severity measures the **technical impact** of the defect on the system.

| Severity | Label | Definition | Examples |
|----------|-------|------------|----------|
| **1** | Critical | System crash, data loss/corruption, no workaround, security breach | Apex unhandled exception halting business process; data corruption in production; unauthorized data access |
| **2** | High | Major feature broken, significant data impact, workaround is painful | Flow fails for specific record type; integration drops records silently; report returns wrong totals |
| **3** | Medium | Feature partially working, cosmetic with functional impact, workaround exists | Picklist missing value; page layout showing wrong fields; email template formatting broken |
| **4** | Low | Cosmetic, minor inconvenience, no business impact | Spelling error in label; alignment issue; non-critical field order |

## Priority Definitions

Priority measures the **business urgency** — how soon the defect must be fixed.

| Priority | Label | Definition | Fix Timeline |
|----------|-------|------------|-------------|
| **1** | Critical | Blocks release or production usage, no workaround | Immediate — current sprint |
| **2** | High | Significant business impact, workaround is temporary | Next sprint |
| **3** | Medium | Moderate impact, acceptable workaround exists | Backlog — within 2-3 sprints |
| **4** | Low | Minimal impact, fix when convenient | Backlog — no timeline pressure |

## Severity × Priority Decision Matrix

| | Priority 1 | Priority 2 | Priority 3 | Priority 4 |
|---|-----------|-----------|-----------|-----------|
| **Severity 1** | Fix NOW | Fix NOW | Unusual — validate | Unusual — validate |
| **Severity 2** | Fix this sprint | Fix next sprint | Backlog (high) | Review classification |
| **Severity 3** | Unusual — validate | Fix next sprint | Backlog | Backlog (low) |
| **Severity 4** | Unusual — validate | Review classification | Backlog (low) | Backlog (low) |

"Unusual — validate" means the combination is atypical; re-examine whether severity or priority is correctly assessed.

## Business Impact Assessment

| Impact Area | Questions to Assess |
|-------------|-------------------|
| **Revenue** | Does this block transactions, billing, or revenue recognition? |
| **Compliance** | Does this violate regulatory requirements (HIPAA, PCI, SOX)? |
| **User productivity** | How many users are affected? Is there a workaround? |
| **Data integrity** | Is data being corrupted, lost, or incorrectly calculated? |
| **Customer experience** | Does this affect external customers via portal/community? |
| **Go-live readiness** | Does this block UAT sign-off or release deployment? |

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
