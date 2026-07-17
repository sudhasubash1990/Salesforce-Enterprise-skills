---
title: Review Scoring Model
module: Salesforce Quality Engineering
category: Automation Intelligence
document_type: Reference
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# Review Scoring Model

## Purpose

Provide a consistent 1–5 scale and weighting model for Automation Review Engine dimensions.

## Business Context

Comparable scores across engagements enable modernization roadmaps and executive reporting without fake precision.

## Overview

| Score | Meaning |
|-------|---------|
| **5** | Enterprise-ready; minor polish only |
| **4** | Solid; localized gaps |
| **3** | Partial; workable but debt accumulating |
| **2** | Weak; frequent pain / risk |
| **1** | Critical gap; blocks trust or safety |
| **N/A** | Insufficient evidence—do not invent |

### Default weights (adjust with program agreement)

| Dimension | Weight |
|-----------|--------|
| Architecture & modularity | 15% |
| POM / Screenplay quality | 10% |
| Locator robustness | 15% |
| Test data management | 10% |
| CI/CD readiness | 15% |
| Reporting & observability | 5% |
| Flaky / stability | 15% |
| Governance compliance | 5% |
| Security practices | 10% |

**Weighted score** = Σ (dimension_score × weight) / Σ weights_of_scored_dimensions  
Exclude N/A from denominator. State if security score ≤ 2 → cap overall narrative at “At Risk” regardless of average.

## Decision Criteria

- Evidence required for each score (path pattern, metric, or explicit gap).  
- Prefer conservative scoring when evidence is thin.  
- Confidence: High (rich evidence), Medium (partial), Low (mostly qualitative).  

## Advantages

- Transparent and auditable.  
- Supports prioritization across tools.  

## Limitations

- Not a substitute for runtime test quality or business coverage.  
- Weights are indicative defaults.  

## Best Practices

- Show both raw dimension table and weighted roll-up.  
- Call out P0 security/flake even if average looks “3”.  

## Salesforce Considerations

- Raise locator/stability expectations for Lightning vs static web apps.  

## Automation Considerations

- Do not equate high architecture score with high business value automation.  

## Common Pitfalls

- Averaging in N/A as zero.  
- Inflating scores to please stakeholders.  

## Examples

Locators 2, Security 1, others 3–4 → weighted ~2.7 but **At Risk** due to secrets; P0 = security.

## Interview Questions

- Why weight stability and locators highly for Salesforce UI?  
- When would you change default weights?  

## Related Documents

- [Maintainability Score](maintainability-score.md)
- [Automation Review Engine](automation-review-engine.md)

## Navigation

- **Previous:** [automation-review-engine.md](automation-review-engine.md)
- **Next:** [architecture-and-modularity.md](architecture-and-modularity.md)

## Future Enhancements

- Program weight overlay file  
