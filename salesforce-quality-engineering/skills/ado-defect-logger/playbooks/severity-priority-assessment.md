---
title: Severity & Priority Assessment Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, severity-priority-assessment]
---

# Severity & Priority Assessment Playbook

## Step 1 — Assess Severity (Technical Impact)

Ask these questions in order:

1. **Does the defect cause data loss or corruption?** → Severity 1
2. **Does it crash the system or block a critical business process with no workaround?** → Severity 1
3. **Does it break a major feature but a workaround exists?** → Severity 2
4. **Does it cause incorrect results (reports, calculations, integrations)?** → Severity 2
5. **Is it a partial malfunction with limited impact?** → Severity 3
6. **Is it purely cosmetic with no functional impact?** → Severity 4

## Step 2 — Assess Priority (Business Urgency)

Ask these questions:

1. **Does this block UAT sign-off or release deployment?** → Priority 1
2. **Is this affecting production users right now?** → Priority 1
3. **Does this have compliance or regulatory implications?** → Priority 1-2
4. **How many users are affected?** → Higher count = higher priority
5. **Is there an acceptable workaround?** → Lowers priority by one level
6. **What is the cost of delay?** → Revenue, reputation, compliance risk

## Step 3 — Validate the Combination

Check the [severity-priority matrix](../knowledge/severity-priority-model.md). If the combination is marked "Unusual — validate," re-examine:

- Is severity over/under-stated?
- Is priority driven by emotion rather than evidence?
- Does the workaround actually work reliably?

## Step 4 — Document Justification

For Severity 1-2 or Priority 1-2 defects, include a brief justification:

```
Severity justification: [Why this severity level]
Priority justification: [Why this priority level]
Business impact: [Specific impact statement]
```

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
