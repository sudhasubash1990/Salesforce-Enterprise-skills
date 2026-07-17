---
title: BA Competency and Maturity Framework
module: Salesforce Business Analyst
category: Root
document_type: Framework
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
keywords: [ba maturity model]
tags: [maturity, competency, career, certification]
---

# Enterprise Business Analyst Competency & Maturity Framework

**Repository:** Salesforce-Enterprise-Skills  
**Module:** Salesforce Business Analyst  
**Version:** 1.3.0

## 1. Objective

Establish a globally reusable Business Analyst Competency & Maturity Framework for Salesforce Business Analysts.

This framework enables:

- Individual learning and organizational capability development
- AI-assisted coaching and competency assessments
- Enterprise consulting readiness and career progression planning
- Knowledge governance aligned with the repository

## 2. Design Principles

The maturity framework shall:

- Be role-based and competency-driven
- Support continuous learning
- Integrate with the Salesforce Business Analyst Skill repository
- Encourage consulting behaviours
- Measure capability rather than years of experience
- Be reusable by organizations worldwide

## 3. Maturity Levels

Five maturity levels:

```
Level 1 (Associate) → Level 2 (Analyst) → Level 3 (Senior)
    → Level 4 (Lead) → Level 5 (Principal)
```

Each level expands knowledge, responsibilities, leadership, and consulting capability.

**Learning paths:** [learning-paths/README.md](learning-paths/README.md)

## 4. Maturity Model Overview

| Level | Role | Primary Repository Modules |
|-------|------|---------------------------|
| L1 | Associate Business Analyst | [knowledge/](knowledge/), [templates/](templates/) |
| L2 | Business Analyst | L1 + [playbooks/](playbooks/), [scenarios/](scenarios/) |
| L3 | Senior Business Analyst | L2 + [brain/](brain/), [decision-framework.md](brain/decision-framework.md) |
| L4 | Lead Business Analyst | L3 + governance, [validation/](validation/) |
| L5 | Principal / Consulting BA | Full repo, [implementation/](implementation/), contribution |

## 5. Level 1 — Associate Business Analyst

**Purpose:** Build strong business analysis fundamentals — concepts, terminology, documentation, structured thinking.

**Responsibilities:** Requirement documentation, workshop support, meeting notes, process documentation, user story creation, acceptance criteria drafting, stakeholder support.

**Repository usage — primary modules:**

| Order | Resource |
|-------|----------|
| 1 | [knowledge/business-analysis-fundamentals.md](knowledge/business-analysis-fundamentals.md) |
| 2 | [knowledge/requirement-types.md](knowledge/requirement-types.md) |
| 3 | [knowledge/user-stories.md](knowledge/user-stories.md) |
| 4 | [knowledge/acceptance-criteria.md](knowledge/acceptance-criteria.md) |
| 5 | [knowledge/business-rules.md](knowledge/business-rules.md) |
| 6 | [knowledge/stakeholder-analysis.md](knowledge/stakeholder-analysis.md) |
| 7 | [templates/user-story-template.md](templates/user-story-template.md) |
| 8 | [templates/meeting-minutes-template.md](templates/meeting-minutes-template.md) |

**Learning path:** [learning-paths/level-1-associate.md](learning-paths/level-1-associate.md)

**Expected competencies:** Business terminology, documentation, basic Salesforce awareness, communication, requirement elicitation, process understanding.

**Deliverables:** Meeting minutes, user stories, acceptance criteria, BRD sections, workshop notes.

**AI usage:** Learn concepts, generate first drafts, validate documentation, understand Salesforce terminology.

**Exit criteria — ready for L2 when able to:**

- Document complete requirements
- Produce quality user stories
- Facilitate simple workshops
- Understand business processes

## 6. Level 2 — Business Analyst

**Purpose:** Apply business analysis skills independently.

**Responsibilities:** Facilitate workshops, manage stakeholders, analyze current/future state, gap analysis, prioritization, scope management.

**Repository usage — primary modules:**

| Module | Key resources |
|--------|---------------|
| Knowledge | [current-state-analysis.md](knowledge/current-state-analysis.md), [moscow-prioritization.md](knowledge/moscow-prioritization.md) |
| Templates | [brd-template.md](templates/brd-template.md), [frd-template.md](templates/frd-template.md), [rtm-template.md](templates/rtm-template.md) |
| Playbooks | [discovery-workshop-playbook.md](playbooks/discovery-workshop-playbook.md), [requirement-workshop-playbook.md](playbooks/requirement-workshop-playbook.md) |
| Scenarios | [scenarios/README.md](scenarios/README.md) — any industry folder |

**Learning path:** [learning-paths/level-2-analyst.md](learning-paths/level-2-analyst.md)

**Expected competencies:** Requirement discovery, BPMN, process improvement, prioritization, risk awareness, Salesforce capability mapping.

**Deliverables:** BRD, FRD, RTM, current/future state, process maps, stakeholder matrix.

**AI usage:** Generate workshop questions, draft documentation, analyze gaps, recommend Salesforce capabilities.

**Exit criteria — ready for L3 when able to lead medium-sized Salesforce projects independently.**

## 7. Level 3 — Senior Business Analyst

**Purpose:** Lead enterprise business analysis activities.

**Responsibilities:** Business capability assessment, enterprise workshops, solution recommendations, executive communication, decision facilitation, complex stakeholder management.

**Repository usage — primary modules:**

| Module | Key resources |
|--------|---------------|
| Brain | [brain/README.md](brain/README.md), [decision-framework.md](brain/decision-framework.md), [reasoning-framework.md](brain/reasoning-framework.md) |
| Playbooks | [gap-analysis-playbook.md](playbooks/gap-analysis-playbook.md), [solution-recommendation-playbook.md](playbooks/solution-recommendation-playbook.md) |
| Knowledge | [governance-framework.md](knowledge/governance-framework.md), [integration-patterns.md](knowledge/integration-patterns.md) |

**Learning path:** [learning-paths/level-3-senior.md](learning-paths/level-3-senior.md)

**Expected competencies:** Enterprise consulting, Salesforce solution analysis, configuration vs customization, risk analysis, governance awareness, integration understanding.

**Deliverables:** Executive recommendations, capability assessments, gap analysis, business cases, solution options, roadmaps.

**AI usage:** Use AI as a consulting assistant; validate recommendations before presentation.

**Exit criteria — ready for L4 when able to lead multiple teams and influence enterprise decisions.**

## 8. Level 4 — Lead Business Analyst

**Purpose:** Provide delivery leadership and governance.

**Responsibilities:** BA governance, team mentoring, quality assurance, enterprise standards, executive stakeholder management, portfolio oversight, review and approval.

**Repository usage — primary modules:**

| Module | Key resources |
|--------|---------------|
| Governance | [docs/cross-linking-framework.md](../docs/cross-linking-framework.md), [docs/quality-framework.md](../docs/quality-framework.md) |
| Validation | [validation/README.md](validation/README.md), [validation/enterprise-validation-framework.md](validation/enterprise-validation-framework.md) |
| Playbooks | [steering-committee-playbook.md](playbooks/steering-committee-playbook.md), [production-readiness-playbook.md](playbooks/production-readiness-playbook.md) |
| Brain | [validation-framework.md](brain/validation-framework.md), [enterprise-behaviors.md](brain/enterprise-behaviors.md) |

**Learning path:** [learning-paths/level-4-lead.md](learning-paths/level-4-lead.md)

**Expected competencies:** Leadership, coaching, delivery governance, risk management, quality assurance, strategic thinking.

**Deliverables:** Approve BRDs, FRDs, architecture alignment, solution recommendations, governance reports.

**AI usage:** Review documentation, identify inconsistencies, coach team members, maintain repository quality.

**Exit criteria — ready for L5 when able to influence enterprise strategy and knowledge management.**

## 9. Level 5 — Principal / Consulting Business Analyst

**Purpose:** Lead enterprise consulting strategy and knowledge evolution.

**Responsibilities:** Consulting leadership, enterprise transformation, AI strategy, repository governance, knowledge architecture, industry frameworks, organizational capability development.

**Repository usage:** Entire repository. Responsible for repository extension, AI coaching, governance, continuous improvement, industry expansion.

| Area | Resource |
|------|----------|
| Implementation | [implementation/README.md](implementation/README.md), [build-standards.md](implementation/build-standards.md) |
| Knowledge governance | [docs/continuous-knowledge-management.md](../docs/continuous-knowledge-management.md) |
| Contribution | [implementation/design-decisions.md](implementation/design-decisions.md) |

**Learning path:** [learning-paths/level-5-principal.md](learning-paths/level-5-principal.md)

**Expected competencies:** Executive consulting, enterprise architecture awareness, portfolio strategy, AI-assisted consulting, knowledge governance, organizational transformation.

**Deliverables:** Enterprise strategies, capability roadmaps, transformation programs, repository evolution, AI governance.

**Success criteria:** Recognized as a trusted advisor capable of shaping enterprise Salesforce delivery and organizational BA practices.

## 10. Competency Matrix

Assess competencies across maturity levels (✓ = expected proficiency).

| Competency | L1 | L2 | L3 | L4 | L5 |
|------------|:--:|:--:|:--:|:--:|:--:|
| Requirement Elicitation | ✓ | ✓ | ✓ | ✓ | ✓ |
| User Stories | ✓ | ✓ | ✓ | ✓ | ✓ |
| Process Analysis | ✓ | ✓ | ✓ | ✓ | ✓ |
| BPMN | | ✓ | ✓ | ✓ | ✓ |
| Salesforce Capability Mapping | | ✓ | ✓ | ✓ | ✓ |
| Enterprise Consulting | | | ✓ | ✓ | ✓ |
| Governance | | | | ✓ | ✓ |
| AI Coaching | | | | ✓ | ✓ |
| Knowledge Governance | | | | | ✓ |
| Repository Contribution | | | ✓ | ✓ | ✓ |

**Assessment template:** [templates/competency-assessment-template.md](templates/competency-assessment-template.md)

## 11. Recommended Learning Path

Progressive repository usage:

```
Knowledge → Templates → Playbooks → Industry Scenarios
    → BA Brain → Decision Framework → Governance → Validation
    → Repository Extension → AI Coaching
```

Each level builds upon the previous. See [learning-paths/README.md](learning-paths/README.md).

## 12. Assessment Framework

Organizations may evaluate BAs using:

- Knowledge assessments and scenario-based exercises
- Workshop facilitation and documentation reviews
- Stakeholder simulations, case studies, whiteboard sessions
- Executive presentations

**Primary assessment resource:** [interview-guide/interview-index.md](interview-guide/interview-index.md) (Sprint 6 Interview Intelligence Framework).

**Benchmarks:** [validation/benchmark-scenarios.md](validation/benchmark-scenarios.md)

## 13. Certification Path

Suggested certification progression:

| Tier | Focus | Validation |
|------|-------|------------|
| 1 | Internal Repository Fundamentals | L1 learning path + interview topics |
| 2 | Enterprise Business Analysis | L2 benchmarks + BRD/story deliverables |
| 3 | Salesforce Business Analysis | L3 brain/decision + platform interview topics |
| 4 | Industry Specialist | Domain scenario + fit-gap exercise |
| 5 | Enterprise Consulting Leader | L4/L5 governance + certification report |

**Report template:** [validation/certification-report-template.md](validation/certification-report-template.md)

## 14. Organizational Adoption

Recommended use cases:

- Onboarding new Business Analysts
- Career progression and performance reviews
- Mentoring programs and skills gap analysis
- Training plans, interview preparation
- Consulting capability development

## 15. Success Metrics

Track:

- Competency assessment scores and repository adoption
- Documentation quality and workshop effectiveness
- Stakeholder satisfaction and reuse of repository assets
- AI-assisted productivity and promotion readiness

## 16. Cross-Linking — Sprint Alignment

| Sprint | Module |
|--------|--------|
| Sprint 1 | [brain/](brain/) — BA Brain |
| Sprint 2 | [knowledge/](knowledge/) — Knowledge Base |
| Sprint 3 | [templates/](templates/) — Template Library |
| Sprint 4 | [playbooks/](playbooks/) — Playbooks |
| Sprint 5 | [scenarios/](scenarios/) — Industry Scenarios |
| Sprint 6 | [interview-guide/](interview-guide/) — Interview Intelligence |
| Sprint 7 | [docs/cross-linking-framework.md](../docs/cross-linking-framework.md) — Metadata |
| Sprint 8 | [validation/](validation/) — Enterprise Validation |
| Sprint 9 | [implementation/](implementation/), [skill-guide.md](skill-guide.md) — Continuous KM |

## 17. Definition of Done

This maturity model is complete when:

- Every BA can identify their current maturity level
- Required repository modules are mapped to each level
- Competencies are measurable via matrix and assessment template
- Learning paths are clearly defined per level
- Organizations can adopt the framework for career development, mentoring, performance evaluation, and AI-assisted coaching

## Related Brain Modules

- [Readme](brain/README.md)

## Related Knowledge

- [Readme](knowledge/README.md)

## Related Templates

- [Readme](templates/README.md)

## Related Playbooks

- [Readme](playbooks/README.md)

## Related Industry Scenarios

- [Readme](scenarios/README.md)

## Related Interview Topics

- [Interview Index](interview-guide/interview-index.md)

## Related Examples

- [Readme](../examples/sample-project/README.md)

## Related Documents

- [Cross Linking Framework](../docs/cross-linking-framework.md)
- [Roadmap](../ROADMAP.md)

## Traceability

**Upstream:** — | **Downstream:** All skills | **Validation:** ROADMAP alignment

## Navigation

- **Previous:** [Readme](README.md)
- **Next:** [Changelog](CHANGELOG.md)
- **See Also:** [skill.md](skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
