---
title: Reasoning Pipeline
version: 0.1.0
tags: [framework-core]
status: draft
last_updated: 2026-07-18
---

# Reasoning Pipeline

## Purpose

Shared think → decide → deliver pipeline for all SEACF agents.

## Scope

**In:** Cross-module SEACF contracts reusable by BA, QE, SA, Developer, DevOps, and Production Support packs.  
**Out:** Module-specific deep knowledge (lives in each module); inventing client metrics or certifications.

## Business Context

SEACF modules must share one orchestration, governance, and evaluation language so agents and humans do not re-implement routing, standards, or certification differently per skill.


## Pipeline

```
Receive request
    → Route (request-router)
    → Assemble context (context-manager)
    → Module Pre-Execution Gate
    → Reason (facts vs assumptions; risks; options)
    → Decide (proceed / clarify / escalate)
    → Deliver (template-aligned artifact)
    → Self-check (anti-hallucination; traceability)
```

## Hard rules (all modules)

1. Never invent regulatory requirements, SLA/KPI %, or certification levels without evidence.  
2. Separate **Facts** vs **Assumptions**.  
3. Prefer platform-native Salesforce solutions before custom.  
4. Do not bypass security/sharing controls in recommendations.  
5. Pause on multi-cloud scope, undefined compliance, or material buy/build decisions.


## Inputs

- User request / module intent
- Module `skill.md` and brain (when loaded)
- Optional evidence pack

## Outputs

- Route / context / workflow decisions
- References into module engines
- Governance-compliant artifacts

## Navigation

- **Up:** [README.md](../README.md) or parent folder README
- **Core root:** [../../README.md](../../README.md) (adjust depth as needed)

## Related Documents

- [../governance/quality-standards.md](../governance/quality-standards.md)
- BA brain / QE brain module files

## Future Enhancements

- Machine-readable route schemas
- Shared CI hooks for all modules
