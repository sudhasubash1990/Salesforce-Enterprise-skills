---
title: Rule Evaluation Process
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

# Rule Evaluation Process

## Purpose

Define how the AI evaluates Quality Intelligence rules against evidence before recommending actions.

## Business Context

Without a disciplined evaluation order, consultants either over-recommend or miss critical signals (e.g., permission defects buried under volume).

## Overview

Evaluation order (recommended):

1. **Data sufficiency** — can the rule fire?  
2. **Release / production safety signals** (gates, leakage, prod clusters)  
3. **Defect quality signals** (reopen, reopen trend)  
4. **Hotspot / taxonomy dominance** (Flow, Apex, security, integration, cloud)  
5. **Automation & regression effectiveness**  
6. **Merge, prioritize, escalate**

## Inputs

Evidence pack + optional program threshold table.

## Outputs

Fired rule set + prioritized action board.

## Process

### Step 1 — Sufficiency gate

| Evidence state | Behaviour |
|----------------|-----------|
| Metric/count provided | Evaluate numeric rules |
| Only qualitative (“many Flow bugs”) | Fire pattern/cluster rules with **Low–Medium** confidence; ask for counts |
| Missing critical data | Do **not** invent; list rules that *would* apply if data supplied |

### Step 2 — Evaluate packs

Load and apply:

- [metric-threshold-rules.md](metric-threshold-rules.md)  
- [reopen-and-defect-quality-rules.md](reopen-and-defect-quality-rules.md)  
- [platform-hotspot-rules.md](platform-hotspot-rules.md)  
- [security-permission-rules.md](security-permission-rules.md)  
- [integration-and-cloud-cluster-rules.md](integration-and-cloud-cluster-rules.md)  
- [automation-stability-rules.md](automation-stability-rules.md)  
- [regression-and-coverage-rules.md](regression-and-coverage-rules.md)  
- [release-gate-rules.md](release-gate-rules.md)  

### Step 3 — Merge

Collapse duplicate THEN actions; keep all Rule IDs as sources.

### Step 4 — Prioritize

Apply [recommendation-priority.md](recommendation-priority.md).

### Step 5 — Present

For each top action: evidence → Rule ID(s) → action → suggested owner → verification check.

## Examples

Given: Leakage 15%, reopen rate rising, Flow tags dominant.  
Fire: QI-R-MET-001, QI-R-REO-001, QI-R-PLT-001.  
Merged actions: expand regression (escape + Flow), reopen quality review, Flow automation candidates—prioritized P0/P1.

## Best Practices

- Show suppressed rules when “Do not fire if” applies.  
- Prefer fewer high-impact actions over exhaustive lists.

## Common Mistakes

- Evaluating only the first matching rule.  
- Ignoring escalation for production clusters.

## Interview Questions

- How do you sequence metric vs hotspot rules?  
- What is a sufficiency gate in quality analytics?

## Related Documents

- [Rules Engine](rules-engine.md)
- [Recommendation Priority](recommendation-priority.md)

## Navigation

- **Previous:** [rule-schema.md](rule-schema.md)
- **Next:** [metric-threshold-rules.md](metric-threshold-rules.md)

## Future Enhancements

- Weighted scoring model across fired rules  
