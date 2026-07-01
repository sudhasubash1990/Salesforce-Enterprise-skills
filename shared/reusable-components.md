---
title: Reusable Components
module: Salesforce Business Analyst
category: Shared
document_type: Reference
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/consulting-principles.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [docs/metadata-schema.md, shared/traceability-model.md]
keywords: [reusable components]
tags: [reusable-components]
---

# Reusable Components

Cross-skill reusable patterns and components.

## Requirement Patterns

### Outcome Pattern

```
[Actor] needs to [capability] so that [measurable outcome].
```

### Business Rule Pattern

```
When [condition], the system must [behavior], except when [exception].
```

### Integration Pattern

```
When [event] occurs in [system], Salesforce must [action] within [SLA].
```

## Workshop Components

| Component | Duration | Output |
|-----------|----------|--------|
| Stakeholder mapping | 1 hr | RACI, influence matrix |
| AS-IS walkthrough | 2 hr | Process notes, pain points |
| TO-BE envisioning | 2 hr | Future process, capability list |
| Prioritization | 1 hr | MoSCoW ranked backlog |
| Demo validation | 1 hr | Confirmed/denied assumptions |

## Story Components

- **Role** — Salesforce user profile or persona
- **Goal** — Action without implementation detail
- **Benefit** — Business value
- **Acceptance criteria** — Given/When/Then
- **Notes** — Data, permissions, integration edge cases

## Fit-Gap Components

Per requirement row:

| Column | Content |
|--------|---------|
| Req ID | BR/FR reference |
| Need | Business statement |
| Standard feature | Salesforce native option |
| Gap? | Y/N/Partial |
| Classification | Standard/Config/Extend/Gap/Defer |
| Recommendation | Proposed approach |
| Effort | T-shirt or rough t-shirt |
| Risk | Low/Med/High + note |

## Traceability Row

| BR ID | FR ID | US ID | TS ID | Status |

## RAID Entry Templates

**Risk:** If [event], then [impact]. Mitigation: [action]. Owner: [role].

**Assumption:** We assume [statement]. Validate by [date/milestone].

**Issue:** [Problem]. Resolution: [action]. Target date: [date].

**Dependency:** [Team/system] must deliver [artifact] by [date].

## Reuse Instructions

Copy components into deliverables; do not duplicate into multiple canonical sources—link here from playbooks when referencing patterns.

## Related Brain Modules

- [Consulting Principles](../salesforce-business-analyst/brain/consulting-principles.md)

## Related Knowledge

- [Readme](../salesforce-business-analyst/knowledge/README.md)

## Related Templates

- [Readme](../salesforce-business-analyst/templates/README.md)

## Related Playbooks

- [Readme](../salesforce-business-analyst/playbooks/README.md)

## Related Industry Scenarios

- [Readme](../salesforce-business-analyst/scenarios/README.md)

## Related Interview Topics

- [Interview Index](../salesforce-business-analyst/interview-guide/interview-index.md)

## Related Examples

- [Readme](../examples/sample-project/README.md)

## Related Documents

- [Metadata Schema](../docs/metadata-schema.md)
- [Traceability Model](traceability-model.md)

## Traceability

**Upstream:** Governance | **Downstream:** All modules | **Validation:** glossary consistency

## Navigation

- **Previous:** [Relationship Matrix](relationship-matrix.md)
- **Next:** [Salesforce Capability Map](salesforce-capability-map.md)
- **See Also:** [cross-linking-framework](../docs/cross-linking-framework.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
