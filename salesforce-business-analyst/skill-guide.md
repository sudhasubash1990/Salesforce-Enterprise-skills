---
title: Enterprise Skill Guide
module: Salesforce Business Analyst
category: Root
document_type: Guide
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
keywords: [skill guide]
tags: [skill-guide, onboarding, governance]
---

# Salesforce Business Analyst Skill — Enterprise Implementation Guide

**Repository:** Salesforce-Enterprise-Skills  
**Module:** Salesforce Business Analyst  
**Version:** 1.3.0

## Audience

- Business Analysts, Senior BAs, Lead BAs
- Functional Consultants, Solution Architects, Technical Architects
- Salesforce Consultants, Delivery Managers, QA Leads
- Product Owners, Scrum Masters, AI Engineers
- Organizations implementing Salesforce

## Welcome

Welcome to the Salesforce Business Analyst Skill.

This repository is much more than a collection of prompts or markdown files. It is an **Enterprise Consulting Knowledge System** that teaches AI and Business Analysts how to think, analyze, document, validate, and recommend solutions in enterprise Salesforce implementations.

The repository replicates the working methodology of experienced consultants from global consulting organizations while remaining modular, reusable, and AI-friendly.

Whether you are a new Business Analyst or an experienced consultant, this framework provides a consistent way to perform business analysis activities across Salesforce projects.

For day-to-day agent orchestration, start with [skill.md](skill.md). This guide provides the full narrative, architecture, and adoption guidance.

## Purpose

The purpose of this repository is to create a reusable Business Analyst operating system that:

- Standardizes business analysis practices
- Improves documentation quality
- Reduces project inconsistencies
- Accelerates requirement discovery
- Supports AI-assisted consulting
- Produces enterprise-grade deliverables
- Enables reusable consulting knowledge
- Encourages continuous improvement

## Repository Philosophy

Traditional prompt libraries answer questions. **This repository teaches how to think.**

The Business Analyst Skill is based on five principles:

1. **Business before technology**
2. **Configuration before customization**
3. **Traceability from requirement to deployment**
4. **Reuse before recreation**
5. **Continuous validation before recommendation**

Every document contributes to these principles.

## Repository Architecture

```
Salesforce-Enterprise-Skills/
├── docs/
├── shared/
├── examples/
├── scripts/
└── salesforce-business-analyst/
    ├── skill.md
    ├── skill-guide.md          ← this document
    ├── ba-maturity-model.md
    ├── brain/
    ├── knowledge/
    ├── templates/
    ├── playbooks/
    ├── scenarios/
    ├── interview-guide/
    ├── validation/
    ├── implementation/
    └── learning-paths/
```

Each folder has a specific purpose and should not duplicate another. See [docs/architecture.md](../docs/architecture.md) for the full architecture reference.

## Repository Components

### skill.md — Orchestration Layer

**Responsibilities:**

- Controls reasoning flow
- Coordinates modules
- Determines AI behaviour
- Selects appropriate outputs
- Validates recommendations

Think of it as the **brain coordinator**. Load [skill.md](skill.md) first for any BA task.

### brain/ — How the AI Thinks

Defines consulting behaviour. Includes identity, consulting principles, reasoning, communication, decision making, validation, and anti-hallucination.

**Purpose:** Teach consulting behaviour.  
**Index:** [brain/README.md](brain/README.md)

### knowledge/ — What the AI Knows

Reusable business analysis concepts: requirements, BPMN, user stories, risk, governance, Salesforce capability mapping, security, integration, data migration.

**Purpose:** Provide authoritative business knowledge.  
**Index:** [knowledge/README.md](knowledge/README.md)

### templates/ — How Documentation Is Produced

Enterprise templates for BRD, FRD, user stories, RTM, RAID, process flows, business case, deployment checklists.

**Purpose:** Standardize project documentation.  
**Index:** [templates/README.md](templates/README.md)

### playbooks/ — Consulting Methodologies

Discovery workshops, requirement workshops, sprint planning, governance meetings, executive presentations, production readiness.

**Purpose:** Standardize consulting execution.  
**Index:** [playbooks/README.md](playbooks/README.md)

### scenarios/ — Industry Thinking

Supported industries: Utilities, Retail, Healthcare, Insurance, Telecom, Banking.

**Purpose:** Help the AI understand business context instead of relying only on Salesforce terminology.  
**Index:** [scenarios/README.md](scenarios/README.md)

### interview-guide/ — Interview Intelligence

Technical, functional, behavioural questions, whiteboard exercises, case studies, executive communication.

**Purpose:** Support interview preparation and interviewer assessments.  
**Index:** [interview-guide/interview-index.md](interview-guide/interview-index.md)

### validation/ — Enterprise Readiness

Repository validation, quality checks, benchmark scenarios, certification reports.

**Purpose:** Ensure enterprise readiness.  
**Index:** [validation/README.md](validation/README.md)

### implementation/ — Extension Governance

Sprint specifications, repository governance, design decisions, build standards.

**Purpose:** Enable future contributors to extend the framework consistently.  
**Index:** [implementation/README.md](implementation/README.md)

### learning-paths/ — Career Progression

Ordered reading lists and exercises mapped to [ba-maturity-model.md](ba-maturity-model.md) levels L1–L5.

**Index:** [learning-paths/README.md](learning-paths/README.md)

## How the Business Analyst Skill Thinks

The AI follows a structured consulting workflow:

```
Receive Requirement
    ↓
Understand Business Context
    ↓
Identify Business Problem
    ↓
Identify Stakeholders
    ↓
Ask Clarifying Questions
    ↓
Analyze Current State
    ↓
Design Future State
    ↓
Gap Analysis
    ↓
Capability Mapping
    ↓
Configuration vs Customization
    ↓
Risk Assessment
    ↓
Documentation
    ↓
Validation
    ↓
Recommendation
```

Full detail: [brain/reasoning-framework.md](brain/reasoning-framework.md). Every recommendation should follow this sequence unless the request explicitly requires otherwise.

## End-to-End Traceability

Every requirement should remain traceable through the project lifecycle:

```
Business Requirement → Current State → Future State → Gap Analysis
    → Capability Mapping → Epic → Feature → User Story
    → Acceptance Criteria → Test Scenario → RTM
    → Deployment Checklist → Production Validation → Lessons Learned
```

Full model: [shared/traceability-model.md](../shared/traceability-model.md). Traceability is a core design principle.

## How to Use the Repository

| Step | Action |
|------|--------|
| 1 | Understand the business problem — never begin with a Salesforce solution |
| 2 | Use [brain/](brain/) modules to determine the reasoning approach |
| 3 | Use [knowledge/](knowledge/) to understand concepts |
| 4 | Execute the appropriate [playbook](playbooks/README.md) |
| 5 | Generate deliverables using [templates/](templates/README.md) |
| 6 | Reference [industry scenarios](scenarios/README.md) when domain knowledge is required |
| 7 | Validate outputs using [validation/](validation/README.md) and [brain/validation-framework.md](brain/validation-framework.md) |

## How to Use with Cursor

For the best results:

1. Open the repository as the workspace root
2. Keep the folder structure unchanged
3. Preserve metadata and cross-links
4. Ask Cursor to reference existing documents before creating new ones
5. Extend canonical documents instead of duplicating content
6. Review AI-generated updates before merging

See [.cursor/instructions.md](../.cursor/instructions.md) and [.cursor/routing.md](../.cursor/routing.md).

## Recommended Workflow for Business Analysts

1. Understand the problem
2. Review relevant Knowledge articles
3. Execute the appropriate Playbook
4. Capture requirements using Templates
5. Validate against Brain principles
6. Ensure traceability
7. Review risks and assumptions
8. Finalize deliverables
9. Conduct peer review
10. Archive and version the artifacts

## Recommended Workflow for AI Agents

The AI should:

- Ask clarifying questions
- Identify missing information
- Recommend standard Salesforce capabilities first
- Explain trade-offs
- Produce traceable documentation
- Validate recommendations before presenting them
- Never invent unsupported Salesforce functionality
- Explicitly state assumptions

See [brain/anti-hallucination.md](brain/anti-hallucination.md).

## Contribution Guidelines

When adding new content:

- Follow [docs/metadata-schema.md](../docs/metadata-schema.md)
- Use the standard document structure
- Update cross-links per [docs/cross-linking-framework.md](../docs/cross-linking-framework.md)
- Avoid duplicate knowledge
- Update version history
- Reference canonical documents
- Pass `scripts/validate_repository.py` before merge

See [implementation/build-standards.md](implementation/build-standards.md).

## Governance Principles

Every document should be:

- Enterprise-ready, business accurate, Salesforce aligned
- Technically accurate, reusable, maintainable
- AI-friendly, Cursor optimized, GitHub ready, version controlled

See [docs/continuous-knowledge-management.md](../docs/continuous-knowledge-management.md).

## Common Use Cases

This repository supports:

- Discovery workshops and requirement elicitation
- User story creation and backlog refinement
- Executive presentations and Salesforce solution analysis
- Business capability mapping and AI-assisted documentation
- Interview preparation, team onboarding, knowledge sharing
- Enterprise consulting and career progression ([ba-maturity-model.md](ba-maturity-model.md))

## Success Metrics

Organizations adopting this repository should measure:

- Requirement quality and documentation consistency
- Traceability coverage and reuse of templates
- Reduction in rework and stakeholder satisfaction
- AI adoption effectiveness and repository health
- Review compliance and delivery quality

## Future Roadmap

The repository is designed for continuous growth. See [ROADMAP.md](../ROADMAP.md).

Planned enhancements include:

- Additional Salesforce roles (Administrator, Developer, Architect, QA, DevOps, AI, Agentforce)
- Additional industry packs
- Automated governance validation
- AI-assisted knowledge gap detection
- Semantic search, repository analytics, interactive learning paths

## Conclusion

The Salesforce Business Analyst Skill functions as an enterprise consulting framework rather than a prompt collection. It combines structured reasoning, reusable knowledge, standardized documentation, repeatable methodologies, industry-specific expertise, validation, and governance into a single, maintainable system.

By following this guide, Business Analysts deliver consistent, high-quality outcomes across Salesforce implementations while organizations gain a scalable foundation for knowledge management, AI-assisted consulting, onboarding, and continuous improvement.

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

- **Previous:** [References](references.md)
- **Next:** [Skill](skill.md)
- **See Also:** [skill.md](skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
