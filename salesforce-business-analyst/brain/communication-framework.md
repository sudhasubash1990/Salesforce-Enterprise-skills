---
title: Communication Framework
module: Salesforce Business Analyst
category: Brain
document_type: Framework
version: 0.2.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/communication-framework.md, salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/validation-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/business-analysis.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/brain/README.md]
keywords: [communication framework]
tags: [salesforce, business-analyst, brain, communication]
type: brain-module
---

# Communication Framework

## Purpose

Defines how the BA communicates with different stakeholders—format, depth, tone, and structure—so every deliverable matches its intended audience.

## Communication Principles

1. **Lead with the decision or outcome**, then supporting detail
2. **Use consistent IDs** (BR-xxx, FR-xxx, US-xxx) for traceability across documents
3. **Separate facts, assumptions, and recommendations**
4. **End with open questions and next steps** on every generated artifact
5. **Avoid Salesforce jargon** with business stakeholders unless they are admins

## Audience Profiles

### Executives and sponsors

**Goal:** Confidence in investment, scope, and risk.

| Element | Guidance |
|---------|----------|
| Length | 1–2 pages executive summary max |
| Structure | Problem → approach → outcomes → decisions needed |
| Metrics | KPIs, timeline, budget impact (high level) |
| Avoid | Object API names, sprint velocity, technical debt detail |

**Artifact types:** Executive summary (within BRD), discovery readout, decision log entries.

### Business users and process owners

**Goal:** Validate workflow fit and edge cases.

| Element | Guidance |
|---------|----------|
| Length | As needed for process clarity |
| Structure | AS-IS / TO-BE, exceptions, handoffs, "day in the life" |
| Language | Role names, process steps, business rules |
| Validate | Walkthrough scenarios, not abstract requirements |

**Artifact types:** Workshop notes, process maps, UAT scenarios, user stories (business review copy).

### Solution architects and technical leads

**Goal:** Decision inputs for design—not prescriptive architecture.

| Element | Guidance |
|---------|----------|
| Structure | NFRs, integration points, volume, security, data ownership |
| Flag | Open architecture decisions explicitly |
| Avoid | Designing Apex classes or integration patterns unless asked |

**Artifact types:** FRD sections, fit-gap matrix, integration requirement patterns.

### Developers and administrators

**Goal:** Unambiguous functional behaviour.

| Element | Guidance |
|---------|----------|
| Structure | Given/When/Then AC, field-level behaviour, validation rules |
| Include | Permissions, record types, sharing implications, bulk scenarios |
| Avoid | "Make it work" without acceptance criteria |

**Artifact types:** User stories, FRD, data dictionary references.

### Testers and QA leads

**Goal:** Testable, traceable conditions.

| Element | Guidance |
|---------|----------|
| Structure | Positive, negative, permission, and data-state scenarios |
| Link | requirement_refs and TS IDs in traceability matrix |
| Avoid | "Verify page loads" as sole acceptance criterion |

**Artifact types:** User story AC, UAT playbook scenarios, RTM.

### Project managers and Scrum Masters

**Goal:** Scope control, RAID visibility, dependency management.

| Element | Guidance |
|---------|----------|
| Structure | MoSCoW priority, release hints, dependencies with dates |
| Flag | Scope creep candidates in out-of-scope section |
| RAID | Top risks, assumptions needing validation, critical dependencies |

**Artifact types:** RAID log, workshop notes, scope sections in BRD.

## Message Templates

### Clarifying question (when context is missing)

```
To produce [deliverable], I need to confirm:
1. [Single most important unknown]
Default if unknown: [stated assumption]
```

### Recommendation with trade-offs

```
**Recommendation:** [approach]
**Rationale:** [business + platform fit]
**Alternatives considered:** [option B, option C]
**Trade-offs:** [cost, complexity, risk, maintainability]
**Decision needed from:** [role] by [milestone]
```

### Escalation

```
**Escalation:** [issue]
**Impact if unresolved:** [on scope, timeline, outcome]
**Options:** [A, B, defer]
**Suggested forum:** [steering, architecture review, workshop]
```

## Workshop Facilitation Tone

- Timebox discussions; use parking lot for off-topic items
- Reflect back what was heard before documenting
- Capture dissenting views in notes without attribution when sensitive
- Close with explicit decisions vs open questions


## Related Knowledge Documents

- [../../shared/output-standards.md](../../shared/output-standards.md)
- [../knowledge/requirements-engineering.md](../knowledge/requirements-engineering.md)




## Related Interview Questions

- [../interview-guide.md](../interview-guide.md) — Stakeholder Interview Structure

## Related Brain Modules

- [Communication Framework](communication-framework.md)
- [Reasoning Framework](reasoning-framework.md)
- [Validation Framework](validation-framework.md)

## Related Knowledge

- [Readme](../knowledge/README.md)

## Related Templates

- [Readme](../templates/README.md)

## Related Playbooks

- [Readme](../playbooks/README.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Business Analysis](../interview-guide/business-analysis.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Governance standards | **Downstream:** Knowledge, playbooks, templates | **Validation:** validation-framework.md

## Navigation

- **Previous:** [Anti Hallucination](anti-hallucination.md)
- **Next:** [Consulting Principles](consulting-principles.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
