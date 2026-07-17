---
title: Improvement Prioritization
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# Improvement Prioritization

## Purpose

Sequence remediation so teams fix safety and trust first, then structure, then acceleration.

## Business Context

Brownfield Salesforce automation modernization fails when teams rewrite frameworks while secrets and flakes remain.

## Overview

| Priority | Focus | Typical findings |
|----------|-------|------------------|
| **P0** | Safety / trust blockers | Secrets in repo; Sev CI unusable; no smoke in pipeline |
| **P1** | Stability & release protection | Flakes, brittle locators, missing data cleanup, weak gates |
| **P2** | Structure & scale | Layering, POM quality, reporting gaps, governance |
| **P3** | Optimization | Nice-to-have refactors, optional tool migration spikes |

### Recommended sequence

```
Secure secrets → Restore CI signal (quarantine/stabilize)
    → Fix data isolation → Harden locators/waits
    → Improve architecture/POM → Enrich reporting
    → Consider framework migration only if justified
```

## Decision Criteria

- Prefer stabilize-in-place over rewrite when score gaps are secrets/flake/CI.  
- Tool migration (e.g., Selenium → Playwright) is rarely P0 unless framework is unmaintainable **and** skills/budget exist.  

## Best Practices

- Max 5 executive actions; full backlog for Automation Lead.  
- Each action: owner cue, success check, related dimension.  

## Salesforce Considerations

- Persona/auth and integration smoke often unlock more value than UI rewrite.  

## Common Pitfalls

- “Big bang Playwright rewrite” as first recommendation.  

## Examples

P0: purge secrets + vault; P1: quarantine top 10 flakes + API data factories; P2: introduce COM for Lightning widgets.

## Interview Questions

- Why isn’t framework migration usually P0?  

## Related Documents

- [Maintainability Score](maintainability-score.md)
- [Automation Review Engine](automation-review-engine.md)

## Navigation

- **Previous:** [maintainability-score.md](maintainability-score.md)
- **Next:** [review-report-template.md](review-report-template.md)

## Future Enhancements

- 30/60/90-day remediation plan template  
