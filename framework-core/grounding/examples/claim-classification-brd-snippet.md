---
title: Claim Classification BRD Snippet (Non-Authoritative Example)
version: 0.2.0
tags: [framework-core, grounding, example]
status: draft
last_updated: 2026-10-09
---

# Claim Classification — Mini BRD Snippet

**WARNING:** This file is a **historical-example** for training and tests only. It **MUST NOT** be treated as project-approved requirements.

## Sample statements

| claim_id | claim | classification | source_class | notes |
|----------|-------|----------------|--------------|-------|
| CLM-001 | Agents shall log customer complaints as Cases linked to Account | requirement-derived | project-approved | From fictional BR-010 |
| CLM-002 | Omni-Channel routing is recommended for skill-based distribution | recommendation | seacf-approved | BA proposal; not approved decision |
| CLM-003 | Average handle time target is 4 minutes | assumption | model-knowledge | No project evidence; review_required |
| CLM-004 | Case object supports Status and Priority fields | verified | official-product | Standard Salesforce Case capability |

## Conflict example

- Source A (workshop notes): Priority Must include chat channel in Phase 1
- Source B (approved scope deck): Chat deferred to Phase 2  
→ Record CFG-001 per conflict-resolution; escalate to Product Owner; do not silently choose.
