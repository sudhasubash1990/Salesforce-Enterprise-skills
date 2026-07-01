---
title: Design Decisions
module: Salesforce Business Analyst
category: Root
document_type: Reference
version: 1.3.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/README.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [docs/cross-linking-framework.md, ROADMAP.md]
keywords: [design decisions]
tags: [ADR, architecture, design-decisions]
---

# Design Decision Records

Key architecture decisions for the Salesforce Business Analyst Skill repository.

## ADR-001: Brain Modularization (Sprint 1)

**Decision:** Split consulting behaviour into discrete `brain/` modules rather than a single monolithic prompt.

**Rationale:** Progressive loading reduces token use; agents load only modules needed per task type.

**Consequences:** `skill.md` acts as orchestrator with explicit Brain Loading Order table.

## ADR-002: Generator-Based Content at Scale (Sprint 6)

**Decision:** Use Python generators for large repetitive content (670 interview items across 24 files).

**Rationale:** Maintainability — update `TOPIC_META` and regenerate rather than hand-edit hundreds of Q&A blocks.

**Consequences:** `scripts/generate_sprint_6_interview_guide.py` is source of truth for interview structure.

## ADR-003: Metadata Schema and Enrichment (Sprint 7)

**Decision:** Mandatory YAML frontmatter + 8 Related sections on all Markdown; automated enrichment and validation.

**Rationale:** Enterprise knowledge graph requires consistent cross-links for AI routing and human navigation.

**Consequences:** `enrich_sprint_7_metadata.py` and `validate_metadata.py` gate merges.

## ADR-004: Progressive Disclosure — skill.md vs skill-guide.md (Sprint 9)

**Decision:** Keep `skill.md` as lean agent orchestrator; full narrative in `skill-guide.md`.

**Rationale:** Agent context windows favour concise orchestrators; humans and onboarding need full guide.

**Consequences:** `skill.md` gets pointer sections only for Skill Guide, Maturity Model, Learning Paths.

## ADR-005: Two-Layer Validation (Sprint 8)

**Decision:** Separate repository validation (structure, metadata, links) from deliverable validation (BRD, stories, fit-gap).

**Rationale:** CI can gate repo health independently of project artifact quality.

**Consequences:** `validation/` hub + `validate_repository.py` orchestrates structure; `brain/validation-framework.md` gates deliverables.

## ADR-006: Maturity-Aligned Learning Paths (Sprint 9)

**Decision:** Five learning path files map 1:1 to maturity levels L1–L5 with concrete repository module links.

**Rationale:** Career progression tied to real assets, not abstract curricula.

**Consequences:** `ba-maturity-model.md`, `learning-paths/`, and `validation/certification-report-template.md` cross-link.

## Adding New ADRs

1. Assign next ADR number
2. Document decision, rationale, consequences
3. Link from [sprint-index.md](sprint-index.md) if sprint-related
4. Run enrichment and validation before merge

## Related Brain Modules

- [Readme](../brain/README.md)

## Related Knowledge

- [Readme](../knowledge/README.md)

## Related Templates

- [Readme](../templates/README.md)

## Related Playbooks

- [Readme](../playbooks/README.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Interview Index](../interview-guide/interview-index.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Cross Linking Framework](../../docs/cross-linking-framework.md)
- [Roadmap](../../ROADMAP.md)

## Traceability

**Upstream:** — | **Downstream:** All skills | **Validation:** ROADMAP alignment

## Navigation

- **Previous:** [Build Standards](build-standards.md)
- **Next:** [Sprint Index](sprint-index.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
