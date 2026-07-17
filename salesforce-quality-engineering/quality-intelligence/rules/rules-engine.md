---
title: Quality Intelligence Rules Engine
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

# Quality Intelligence Rules Engine

## Purpose

Apply reusable decision rules to quality evidence so recommendations are **repeatable, explainable, and action-oriented**.

## Business Context

Experienced QE consultants do not stop at “leakage is high.” They translate signals into scope changes, reviews, and prevention. This engine encodes that judgment as transparent rules.

## Overview

```
Signals (metrics / patterns / clusters)
    ↓
Normalize inputs + thresholds (program or indicative defaults)
    ↓
Evaluate rules (all matching rules may fire)
    ↓
Deduplicate / merge recommendations
    ↓
Prioritize (P0–P3) + escalate if needed
    ↓
Output: Fired rules + actions + next analyses + confidence
```

## Inputs

| Input | Required |
|-------|----------|
| Metric values with formula period | Prefer; else mark TBC |
| Defect taxonomy / component tags | Prefer |
| Pattern list + confidence | Optional |
| Program thresholds | Optional (use indicative defaults) |
| Release/sprint context | Prefer |

## Outputs

1. **Fired rules** — Rule ID, condition summary, evidence used  
2. **Recommendations** — concrete actions (expand regression, security review, etc.)  
3. **Follow-on analyses** — RCA method, coverage review, hotspot drill-down  
4. **Priority & escalation** — per [recommendation-priority.md](recommendation-priority.md)  
5. **Assumptions / confidence** — never hide missing data  

## Process

1. Load [rule-schema.md](rule-schema.md) and [rule-evaluation-process.md](rule-evaluation-process.md).  
2. Collect evidence; **do not invent** metric values.  
3. Evaluate metric, reopen, platform, security, integration/cloud, automation, regression, and release-gate packs.  
4. Merge overlapping THEN actions (one “expand Flow regression” not three duplicates).  
5. Present as consultant advice: *signal → rule → action → owner suggestion → success check*.  

## Examples

**Signal:** Defect leakage 18% (program threshold 10%).  
**Rule:** QI-R-MET-001.  
**Action:** Expand regression scope; review requirement/scenario coverage for escaped areas; schedule RCA on escape cohort.

**Signal:** 40% of new defects tagged Flow.  
**Rule:** QI-R-PLT-001.  
**Action:** Targeted Flow regression suite + automation candidates for stable Flow paths; load 4A Flow knowledge.

## Best Practices

- Cite Rule IDs in advisory outputs for auditability.  
- Prefer program thresholds; label defaults as *indicative*.  
- Combine rules with RCA—rules trigger investigation, they do not assert root cause alone.  
- Tie Salesforce-specific rules to 4A/4B articles.

## Common Mistakes

- Firing recommendations without evidence (“assume leakage is high”).  
- Treating indicative thresholds as contractual SLAs.  
- Listing 20 actions with no priority.  
- Replacing human release decisions with rule output alone.

## Interview Questions

- How do you turn a metric breach into a test-scope decision?  
- When would you *not* expand regression after leakage rises?  
- How do you avoid alert fatigue from overlapping quality rules?

## Related Documents

- [Rule Schema](rule-schema.md)
- [Metric Threshold Rules](metric-threshold-rules.md)
- [Platform Hotspot Rules](platform-hotspot-rules.md)
- [../defect-intelligence-engine.md](../defect-intelligence-engine.md)

## Navigation

- **Previous:** [README.md](README.md)
- **Next:** [rule-schema.md](rule-schema.md)
- **See Also:** [rule-evaluation-process.md](rule-evaluation-process.md)

## Future Enhancements

- Machine-readable YAML rule pack export  
- Program-specific threshold overlays under `outputs/<project>/`  
