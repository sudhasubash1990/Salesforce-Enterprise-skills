---
title: Automation Decision Engine
version: 0.10.0
tags: [automation-intelligence, sprint-8]
---

# Automation Decision Engine

## Purpose

Answer structured automation questions with reasoning and confidence scores.

## Questions the AI must answer

| Question | Output |
|----------|--------|
| Should this be automated? | Yes / No / Later + why |
| Why? | Business + technical rationale |
| Which framework? | Tool + alternatives |
| Estimated effort? | T-shirt / range + assumptions (not fake hours certainty) |
| Expected ROI? | Qualitative + formula inputs needed |
| Risk level? | Low/Medium/High |
| Maintenance complexity? | Low/Medium/High |
| CI/CD readiness? | Ready / Gaps |
| Regression impact? | Pack impact statement |
| Automation priority? | P0–P3 |

## Decision flow

```
Is the path stable and oracle clear?
  No → Manual / Later + stabilize first
  Yes ↓
Is frequency/risk high enough?
  No → Manual exploratory / checklist
  Yes ↓
Prefer API/service over UI when possible
  ↓
Select framework (Playwright-first unless constraints)
  ↓
Score effort, maintenance, CI readiness, ROI inputs
  ↓
Priority + roadmap placement
```

## Confidence

Always state **Low / Medium / High** confidence with missing-data notes.

## Related

- [automation-intelligence-engine.md](automation-intelligence-engine.md)
- [automation-strategy/automation-feasibility.md](automation-strategy/automation-feasibility.md)
- [framework-comparison/README.md](framework-comparison/README.md)
- [metrics/roi.md](metrics/roi.md)
