---
title: Overall Maintainability Score
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# Overall Maintainability Score

## Purpose

Roll up dimension scores into an overall maintainability rating with clear narrative bands.

## Business Context

Executives need a single view; engineers need the dimension breakdown behind it.

## Overview

| Weighted score | Band | Meaning |
|----------------|------|---------|
| 4.5 – 5.0 | **Excellent** | Enterprise-ready; continuous improvement only |
| 3.5 – 4.4 | **Good** | Fit for purpose; targeted debt |
| 2.5 – 3.4 | **Fair** | Usable but modernization required |
| 1.5 – 2.4 | **Poor** | High cost / low trust |
| 1.0 – 1.4 | **Critical** | Rebuild or major remediation |

**Overrides:**

- Security ≤ 2 → status **At Risk** (regardless of band)  
- Stability ≤ 2 → cannot claim “release-ready automation”  
- Multiple N/A → reduce confidence; do not fake precision  

## Process

1. Score dimensions per [review-scoring-model.md](review-scoring-model.md).  
2. Compute weighted average.  
3. Apply overrides.  
4. Attach top 5 improvements from [improvement-prioritization.md](improvement-prioritization.md).  

## Outputs

```markdown
## Maintainability Score
- **Weighted score:** 2.8 (Fair)
- **Status:** At Risk (Security = 1)
- **Confidence:** Medium
- **Top improvements:** …
```

## Best Practices

- Always show dimension table beside the roll-up.  
- Separate score from migration recommendation (tool change is optional).  

## Salesforce Considerations

- Modernization initiatives: compare current score vs target band after 90-day remediation.  

## Common Pitfalls

- Reporting only the average and hiding security/flake.  

## Examples

Architecture 4, Locators 2, Security 1, CI 2, Stability 2 → ~2.3 Poor + At Risk.

## Interview Questions

- How do overrides protect executives from misleading averages?  

## Related Documents

- [Review Scoring Model](review-scoring-model.md)
- [Review Report Template](review-report-template.md)

## Navigation

- **Previous:** [security-practices-review.md](security-practices-review.md)
- **Next:** [improvement-prioritization.md](improvement-prioritization.md)

## Future Enhancements

- Target-band OKRs for automation health  
