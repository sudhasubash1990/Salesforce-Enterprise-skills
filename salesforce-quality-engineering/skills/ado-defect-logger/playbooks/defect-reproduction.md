---
title: Defect Reproduction Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-defect-logger, defect-reproduction]
---

# Defect Reproduction Playbook

Guide for reproducing and validating reported Salesforce defects.

## Step 1 — Gather Reproduction Context

- Which environment (sandbox name, org ID)?
- Which user profile / permission set?
- What test data was used?
- What browser / device?
- What time did the issue occur?
- Is there a screenshot, video, or log?

## Step 2 — Attempt Reproduction

1. Log in to the specified environment with the specified profile
2. Follow the reported steps exactly as described
3. Use the same test data if provided
4. Document each step outcome
5. Capture screenshots at each significant step

## Step 3 — Classify Reproducibility

| Classification | Criteria |
|----------------|----------|
| **Always** | Reproduced on every attempt (3+ attempts) |
| **Intermittent** | Reproduced on some attempts, not all |
| **Once** | Could not reproduce, but original evidence is credible |
| **Cannot reproduce** | Multiple attempts failed, no evidence of issue |

## Step 4 — Investigate Non-Reproduction

If the defect cannot be reproduced:

1. Confirm environment matches (same sandbox, same data)
2. Confirm user profile matches (same permissions)
3. Check if a deployment changed behavior since the report
4. Check for time-dependent conditions (batch jobs, scheduled Flows)
5. Check for data-dependent conditions (specific record types, field values)
6. Ask the reporter for additional details or screen recording

## Step 5 — Document Results

Update the defect with:
- Reproducibility classification
- Environment used for reproduction
- Any deviations from original steps
- Additional evidence gathered

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial creation |
