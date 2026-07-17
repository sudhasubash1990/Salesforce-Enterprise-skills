---
title: Automation Stability Rules
module: Salesforce Quality Engineering
category: Quality Intelligence
document_type: Reference
version: 0.9.1
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
tags: [quality-intelligence, sprint-7, rules-engine]
---

# Automation Stability Rules

## Purpose

Respond to automation instability with stabilization and scope discipline—not blind suite growth.

## Business Context

Flaky automation erodes trust, hides real product fails, and wastes triage time.

## Overview

Use automation stability / flake signals from metrics and patterns.

## Inputs

Automation pass/fail, flake rate, quarantine list, failure classification.

## Outputs

Fired `QI-R-AUT-*` recommendations.

## Process

---

### QI-R-AUT-001 — Automation Instability Elevated

| Field | Content |
|-------|---------|
| **IF** | Automation Stability below threshold **or** flake pattern confidence Medium+ |
| **Indicative default** | Stability < 90% **or** flake rate > 5% |
| **THEN** | 1) Quarantine top flaky tests 2) Classify fails: product vs env vs data vs locator/timing 3) Pause new automation expansion until stability recovers 4) Fix data/env pipelines before rewriting all scripts |
| **Priority** | P1 |
| **Related** | [automation-instability](../defect-patterns/automation-instability.md), [automation-stability](../quality-metrics/automation-stability.md) |

---

### QI-R-AUT-002 — High Automation Coverage but Rising Leakage

| Field | Content |
|-------|---------|
| **IF** | Automation Coverage high **and** Defect Leakage / escapes rising |
| **THEN** | 1) Challenge automation value (wrong layer / missing negatives) 2) Add risk-based manual/exploratory on escape areas 3) Realign automation candidates to business-critical paths |
| **Priority** | P1 |
| **Related** | QI-R-MET-001 |

## Examples

Flake rate 12% → QI-R-AUT-001: quarantine 8 unstable UI tests; stabilize shared test user/data; do not add 20 new UI scripts this sprint.

## Best Practices

- Protect CI signal quality over coverage vanity.  
- Prefer API/integration automation for stable Salesforce backends where appropriate.

## Common Mistakes

- Disabling failing tests permanently without ticket.  
- Counting flaky passes as quality evidence.

## Interview Questions

- What do you do when automation is unstable?  
- Can high automation coverage coexist with high leakage? Why?

## Related Documents

- [Regression and Coverage Rules](regression-and-coverage-rules.md)
- [Platform Hotspot Rules](platform-hotspot-rules.md)

## Navigation

- **Previous:** [integration-and-cloud-cluster-rules.md](integration-and-cloud-cluster-rules.md)
- **Next:** [regression-and-coverage-rules.md](regression-and-coverage-rules.md)

## Future Enhancements

- Flake taxonomy codes  
