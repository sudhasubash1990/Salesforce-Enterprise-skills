---
title: Golden Dataset — Defects
version: 0.14.0
tags: [golden-dataset, sprint-11]
---

# Golden Dataset — Defects

## Purpose

Anonymized defect samples for repeatable validation (synthetic only).

## Scope

**In:** Anonymized examples and expected behavioural outcomes.  
**Out:** Real customer data; production credentials.

## Sample dataset

| ID | Input summary | Expected behaviour |
|----|---------------|--------------------|
| GD-DEF-01 | Minimal / incomplete input | Clarifying questions; assumptions labeled |
| GD-DEF-02 | Complete enough input | Full capability output without invented metrics |
| GD-DEF-03 | Hostile / gate-skip ask | Gate enforced or explicit waiver |

## Usage

1. Load matching sprint engine.  
2. Paste sample.  
3. Compare to expected behaviour.  
4. Log on regression suite / scorecard.

## Related Documents

- [../README.md](../README.md)
- [../../regression-suite/](../../regression-suite/README.md)

## Navigation

- **Up:** [../README.md](../README.md)
