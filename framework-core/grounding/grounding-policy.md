---
title: Grounding Policy
version: 0.3.0
tags: [framework-core, grounding]
status: draft
last_updated: 2026-10-09
---

# Grounding Policy

> **Alias:** This file is the framework-level grounding contract (spec name `GROUNDING-CONTRACT.md`). Do not create a duplicate file.

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
9. Agents **MUST NOT** invent Salesforce objects, fields, integrations, SLAs, personas, environments, volumes, or business rules when evidence is missing — record an unknown or labelled assumption instead.
10. When required evidence is missing, agents **MUST** record the unknown and **MAY** continue only with clearly labelled assumptions where safe for the task risk level.

## Grounding envelope (session / artifact summary)

For material deliverables, agents **SHOULD** maintain an aggregate envelope that summarizes what the session may rely on. The envelope is a **summary view**; per-claim detail remains in [evidence-schema.md](evidence-schema.md). Assumption and unknown list shapes: [uncertainty-records.md](uncertainty-records.md).

```yaml
grounding:
  facts: []            # verified or requirement-derived statements
  evidence: []         # evidence IDs / locators supporting facts
  assumptions: []      # A-### records (see uncertainty-records)
  unknowns: []         # U-### records (see uncertainty-records)
  conflicts: []        # conflict IDs per conflict-resolution
  recommendations: []  # labelled recommendations (not approved decisions)
```

Rules:

1. Envelope entries **MUST NOT** silently promote assumptions or recommendations into `facts`.
2. Critical recommendations **SHOULD** retain evidence references or provenance identifiers when the framework can supply them.
3. Agents **MAY** omit an empty envelope section from business-facing prose, but **MUST** retain IDs in diagnostics/traces when observability is enabled.

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
- [uncertainty-records.md](uncertainty-records.md)
- [claim-validation.md](claim-validation.md)
- [../governance/quality-standards.md](../governance/quality-standards.md)
- [../governance/instruction-precedence.md](../governance/instruction-precedence.md)
