---
title: Grounding Policy
version: 0.2.0
tags: [framework-core, grounding]
status: draft
last_updated: 2026-10-09
---

# Grounding Policy

## Purpose

Ensure material business, technical, compliance, and quantitative claims are grounded, classified, and not silently invented.

## Normative rules

1. Agents **MUST** identify the **source class** for material business, technical, compliance, and quantitative claims. See [source-authority.md](source-authority.md).
2. Agents **MUST** label unsupported but necessary working statements as **assumptions** (or open questions), not as verified facts.
3. Agents **MUST NOT** convert examples, templates, historical artifacts, or model knowledge into project facts.
4. Agents **MUST** surface conflicting authoritative sources rather than silently selecting one. See [conflict-resolution.md](conflict-resolution.md).
5. Agents **SHOULD** prefer current approved project evidence over generic repository guidance for project-specific conclusions.
6. Agents **MUST** treat official product documentation and approved project artifacts according to the configured source-authority policy.
7. Agents **MUST NOT** present invented SLAs, coverage percentages, maturity scores, or certification levels as evidence.
8. Agents **MAY** use repository guidance and model knowledge for recommendations when clearly labelled `recommendation` or `repository-guidance`.

## Claim classification (summary)

| Classification | Use when |
|----------------|----------|
| `verified` | Supported by project-approved or official-product evidence with locator |
| `requirement-derived` | Stated or clearly implied by approved requirements under analysis |
| `repository-guidance` | From SEACF-approved pack without project confirmation |
| `assumption` | Necessary for progress; not evidenced |
| `recommendation` | Advisory proposal; not an approved decision |
| `open-question` | Needs stakeholder clarification |
| `unverified` | Appears in content but not yet validated |

Full field list: [evidence-schema.md](evidence-schema.md).

## Acceptance criteria (cross-module)

- A generated BRD **MUST** separate requirement-derived facts from BA recommendations.
- A test strategy **MUST NOT** present an invented SLA or coverage percentage as evidence.
- Two conflicting requirements **MUST** produce an explicit conflict record and clarification/escalation path.
- Examples and templates **MUST NOT** be promoted to authoritative project facts.

## Module application

- BA: apply via [anti-hallucination.md](../../salesforce-business-analyst/brain/anti-hallucination.md) and [validation-framework.md](../../salesforce-business-analyst/brain/validation-framework.md).
- QE: apply via skill Pre-Execution Gate and Engine validation packs; do not invent KPI % or certification without scored evidence.

## Related Documents

- [source-authority.md](source-authority.md)
- [../governance/quality-standards.md](../governance/quality-standards.md)
- [../governance/instruction-precedence.md](../governance/instruction-precedence.md)
