---
title: Recommendation Priority
module: Salesforce Quality Engineering
category: Quality Intelligence
document_type: Guide
version: 0.9.1
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
tags: [quality-intelligence, sprint-7, rules-engine]
---

# Recommendation Priority

## Purpose

Sequence and escalate Quality Intelligence recommendations so teams act on the highest-risk items first.

## Business Context

Rule engines create noise unless priority and escalation are explicit.

## Overview

| Priority | Meaning | Typical triggers |
|----------|---------|------------------|
| **P0** | Immediate / release-blocking | Sev1, active prod cluster, unmet critical gate, suspected data exposure |
| **P1** | Same sprint / before release | Leakage breach, reopen surge, Flow/Apex/security dominance, integration cluster |
| **P2** | Near-term improvement | Defect template quality, UI hotspot, training/KT |
| **P3** | Backlog / CI opportunity | Nice-to-have suite hygiene, documentation polish |

## Inputs

Fired rules with default priorities; severity; release proximity.

## Outputs

Ordered action board (max recommend top 5 for executives; full list for QA Lead).

## Process

1. Start from each rule’s default priority.  
2. **Upgrade** if production + customer impact, security, or release < 48h.  
3. **Downgrade** if evidence weak (confidence Low) or already mitigated.  
4. Merge duplicates; keep Rule ID citations.  
5. Escalate P0 to Delivery/Release/Security as applicable.

### Suggested owner cues

| Action type | Suggested owner |
|-------------|-----------------|
| Expand regression / suites | QA Lead / Test Lead |
| Requirement coverage review | QE + BA |
| Security review | QE + Security/Arch |
| Fix verification practices | QA Lead + Dev Lead |
| Release readiness / gate | QA Lead + Release Manager |
| Automation stabilize | Automation Lead |

## Examples

Fired: QI-R-MET-001 (P1), QI-R-SEC-001 (P1→P0 for prod over-access), QI-R-DFQ-001 (P2).  
Present SEC first, then leakage/regression, then defect template coaching.

## Best Practices

- Executives: outcomes + top 3 actions + residual risk.  
- Always show confidence and threshold source.

## Common Mistakes

- All actions labeled P0.  
- No owner or success check.

## Interview Questions

- How do you prioritize competing quality recommendations?  
- When do you escalate a P1 to P0?

## Related Documents

- [Rules Engine](rules-engine.md)
- [Rule Evaluation Process](rule-evaluation-process.md)

## Navigation

- **Previous:** [release-gate-rules.md](release-gate-rules.md)
- **Next:** [README.md](README.md)

## Future Enhancements

- WSJF-style scoring for QI actions  
