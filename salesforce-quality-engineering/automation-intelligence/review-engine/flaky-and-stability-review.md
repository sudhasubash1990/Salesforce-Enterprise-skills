---
title: Flaky Test Indicators and Stability Review
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# Flaky Test Indicators and Stability Review

## Purpose

Detect flake patterns and stability risks in existing automation estates.

## Business Context

Unstable suites train teams to ignore CI—fatal for Salesforce release confidence.

## Architecture

Stability metrics, quarantine list, failure classification (product/env/data/locator/timing), retry policy that does not hide bugs, ownership for flake burn-down.

## Decision Criteria

| Score | Signals |
|-------|---------|
| 5 | Stability ≥ program target; quarantine with SLA; classified fails; low flake |
| 3 | Some flakes; retries mask issues; weak quarantine |
| 1 | Chronic red/green flicker; no triage; retries everywhere |

**Do not invent flake %**—use provided metrics or qualitative evidence with Low confidence.

## Best Practices

- Apply Sprint 7 [QI-R-AUT-001](../../quality-intelligence/rules/automation-stability-rules.md).  
- Stabilize data/env before rewriting all locators.  

## Salesforce Considerations

- Async (Flow, batch, platform events) needs explicit sync strategies—not fixed sleeps.  

## Automation Considerations

- Link [../maintenance/flake-triage.md](../maintenance/flake-triage.md) and [../metrics/flaky-tests.md](../metrics/flaky-tests.md).  

## Common Pitfalls

- Disabling tests permanently without tickets.  
- Celebrating pass rate while flake rate rises.  

## Examples

Flake rate 12% with no quarantine → score 1–2; P0 stabilize.

## Interview Questions

- How do automation reviews treat retries?  

## Related Documents

- [Locator Robustness](locator-robustness.md)
- [Improvement Prioritization](improvement-prioritization.md)

## Navigation

- **Previous:** [reporting-observability.md](reporting-observability.md)
- **Next:** [governance-compliance-review.md](governance-compliance-review.md)

## Future Enhancements

- Flake taxonomy mapping table  
