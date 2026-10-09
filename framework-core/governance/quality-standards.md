---
title: Quality Standards
version: 0.2.0
tags: [framework-core]
status: draft
last_updated: 2026-10-09
---

# Quality Standards

## Purpose

Cross-module quality and anti-hallucination bar.

## Scope

**In:** Cross-module SEACF contracts reusable by BA, QE, SA, Developer, DevOps, and Production Support packs.  
**Out:** Module-specific deep knowledge (lives in each module); inventing client metrics or certifications.

## Business Context

SEACF modules must share one orchestration, governance, and evaluation language so agents and humans do not re-implement routing, standards, or certification differently per skill.

## Alignment

ISTQB / TMMi themes (QE) · Agile/SAFe quality · ITIL (ops) · TOGAF governance themes (SA) · Salesforce Well-Architected · Responsible AI · [docs/quality-framework.md](../../docs/quality-framework.md)

## Non-negotiables

1. Facts vs assumptions separated — apply [../grounding/grounding-policy.md](../grounding/grounding-policy.md) for material claims  
2. No invented regulatory, SLA, KPI %, maturity, or certification claims  
3. Traceable IDs where requirements/stories/defects exist  
4. Security/sharing respected — plus [../security/untrusted-content-policy.md](../security/untrusted-content-policy.md)  
5. Progressive disclosure — link deep packs  
6. Instruction precedence per [instruction-precedence.md](instruction-precedence.md)  
7. Responsible AI per [../responsible-ai/principles.md](../responsible-ai/principles.md)  
8. Material claims pass [../grounding/claim-validation.md](../grounding/claim-validation.md) (fail closed if `verified` without eligible evidence)  
9. Context classes A–H per [../orchestration/context-policy.md](../orchestration/context-policy.md); do not dump the repository  

## Module checklists

- BA: `salesforce-business-analyst/checklists.md` + brain validation  
- QE: `salesforce-quality-engineering/validation/` + skill Pre-Execution Gate  

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
- **Core root:** [../README.md](../README.md) 

## Related Documents

- [documentation-standards.md](documentation-standards.md)
- [instruction-precedence.md](instruction-precedence.md)
- [../grounding/grounding-policy.md](../grounding/grounding-policy.md)
- [../grounding/claim-validation.md](../grounding/claim-validation.md)
- [../orchestration/context-policy.md](../orchestration/context-policy.md)
- [../evaluation/scoring-model.md](../evaluation/scoring-model.md)

## Future Enhancements

- Machine-readable route schemas
- Shared CI hooks for all modules
