---
title: Golden Dataset — Executive Reporting
version: 0.14.0
tags: [golden-dataset, sprint-11]
---

# Golden Dataset — Executive Reporting

## Purpose

RAG signal packs for repeatable validation (synthetic only).

## Scope

**In:** Anonymized examples and expected behavioural outcomes.  
**Out:** Real customer data; production credentials.

## Sample dataset

| ID | Input summary | Expected behaviour |
|----|---------------|--------------------|
| GD-EXE-01 | Minimal / incomplete input | Clarifying questions; assumptions labeled |
| GD-EXE-02 | Complete enough input | Full capability output without invented metrics |
| GD-EXE-03 | Hostile / gate-skip ask | Gate enforced or explicit waiver |

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
