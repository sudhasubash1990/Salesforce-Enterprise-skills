---
title: Telecom Scenario Validation Script
version: 0.13.0
tags: [validation, e2e, telecom]
---

# Telecom — Scenario Validation Script

## Purpose

Executable prompt sequence for telecom tabletop validation.

## Prompts (run in order)

1. **Incomplete story** — e.g. "User needs to complete a critical telecom transaction in Salesforce."  
   Expect: Sprint 2 analysis, gaps, no detailed cases.

2. **Test strategy ask** — after assumptions stated.  
   Expect: Sprint 5 strategy with assumptions; entry blocked without AC if gates enforced.

3. **Production symptom** — e.g. "Production users cannot complete the telecom transaction."  
   Expect: Sprint 9 triage first; no invented SLA.

4. **Exec health** — paste synthetic RAG signals.  
   Expect: Sprint 10 project health; Hold/Escalate style decision; no fake maturity %.

## Evidence log

| Step | Route observed | Result (Pass/Partial/Fail) | Notes |
|------|----------------|----------------------------|-------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

## Related

- [README.md](README.md)
- [../../benchmark-scorecard.md](../../benchmark-scorecard.md)
