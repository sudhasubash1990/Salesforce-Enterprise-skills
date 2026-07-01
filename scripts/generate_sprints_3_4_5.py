"""Generate Sprint 3 templates, Sprint 4 playbooks, and Sprint 5 industry scenarios."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "salesforce-business-analyst"
TPL = ROOT / "templates"
PB = ROOT / "playbooks"
SC = ROOT / "scenarios"

def yaml_block(title, tid, dtype, clouds="Platform", knowledge=None, playbooks=None, tags=None):
    knowledge = knowledge or []
    playbooks = playbooks or []
    tags = tags or []
    return f"""---
title: {title}
template-id: {tid}
module: Salesforce Business Analyst
category: Template
document-type: {dtype}
version: 0.4.0
status: approved
owner: BA Practice Lead
last-reviewed: 2026-07-02
review-cycle: quarterly
industry: all
salesforce-cloud: {clouds}
related-knowledge: {knowledge}
related-playbooks: {playbooks}
related-brain-modules: [output-framework.md, validation-framework.md]
related-examples: [../examples/fit-gap-excerpt.md]
tags: {tags}
---

"""

def pb_yaml(title, tags):
    return f"""---
title: {title}
module: Salesforce Business Analyst
category: Playbook
document-type: Consulting Methodology
version: 0.5.0
status: approved
owner: BA Practice Lead
last-reviewed: 2026-07-02
review-cycle: quarterly
related-brain-modules: [reasoning-framework.md, enterprise-behaviors.md, decision-framework.md]
related-knowledge: [../knowledge/README.md]
related-templates: [../templates/README.md]
related-examples: [../../examples/sample-project/README.md]
tags: {tags}
---

"""

def sc_yaml(title, industry, domain, clouds, difficulty="intermediate", size="enterprise"):
    return f"""---
title: {title}
module: Salesforce Business Analyst
category: Industry Scenario
document-type: Enterprise Scenario
industry: {industry}
business-domain: {domain}
salesforce-cloud: {clouds}
version: 0.6.0
status: approved
owner: BA Practice Lead
last-reviewed: 2026-07-02
review-cycle: semi-annual
difficulty: {difficulty}
implementation-size: {size}
related-brain-modules: [reasoning-framework.md, decision-framework.md]
related-knowledge: [../knowledge/salesforce-clouds-overview.md, ../knowledge/integration-patterns.md]
related-playbooks: [../playbooks/discovery-workshop-playbook.md, ../playbooks/solution-recommendation-playbook.md]
related-templates: [../templates/brd-template.md, ../templates/user-story-template.md]
related-examples: [../../examples/sample-project/README.md]
tags: [{industry}, {domain}, scenario]
---

"""

def tpl_wrap(title, tid, dtype, audience, prerequisites, inputs, body, knowledge=None, playbooks=None, tags=None):
    k = knowledge or ["../knowledge/README.md"]
    p = playbooks or []
    t = tags or [tid]
    return yaml_block(title, tid, dtype, tags=t) + f"""# {title}

## Purpose

{body.get('purpose', 'Standardized enterprise deliverable scaffold for Salesforce BA programs.')}

## When to Use

{body.get('when', 'When producing this artifact type during discovery, design, delivery, or governance.')}

## Intended Audience

{audience}

## Prerequisites

{prerequisites}

## Inputs

{inputs}

## Completion Instructions

1. Complete YAML metadata and document control fields.
2. Replace `{{placeholders}}` with engagement-specific content.
3. Assign unique IDs (BR-, FR-, US-, etc.) per [../../shared/taxonomy.md](../../shared/taxonomy.md).
4. Cross-reference related requirements in RTM.
5. Run [../checklists.md](../checklists.md) and [../brain/validation-framework.md](../brain/validation-framework.md) before review.

---

## Document Body

{body.get('content', '[Complete sections per engagement]')}

---

## Review Checklist

- [ ] Metadata complete
- [ ] Unique IDs assigned
- [ ] Assumptions and out-of-scope documented
- [ ] Terminology matches [../../shared/glossary.md](../../shared/glossary.md)
- [ ] Traceability links verified
- [ ] Anonymized—no client PII

## Approval Section

| Role | Name | Signature / Date |
|------|------|------------------|
| Business Owner | | |
| BA Lead | | |
| Solution Architect | | |

## Related Documents

- Knowledge: {', '.join(k)}
- Playbooks: {', '.join(p) if p else 'See ../playbooks/README.md'}
- Brain: [../brain/output-framework.md](../brain/output-framework.md)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.4.0 | 2026-07-02 | Sprint 3 enterprise template |
"""

def pb_wrap(title, methodology, deliverables, activities, tags):
    return pb_yaml(title, tags) + f"""# {title}

## Purpose

Repeatable consulting methodology for enterprise Salesforce programs.

## Business Objectives

- Execute {title.lower()} with consistent quality and governance
- Produce traceable deliverables aligned to brain reasoning framework
- Reduce rework through defined decision gates

## Success Criteria

- All deliverables completed and reviewed
- RAID/decisions updated
- Stakeholder sign-off where required

## Scope

Applies to Salesforce implementation programs using Agile, hybrid, or waterfall delivery.

## Prerequisites

- Sponsor and key stakeholders identified
- Access to [../brain/reasoning-framework.md](../brain/reasoning-framework.md)
- Relevant templates from [../templates/README.md](../templates/README.md)

## Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| BA Lead | Facilitate, document, trace |
| Business Owner | Prioritize, approve |
| Solution Architect | Feasibility, fit-gap validation |
| PM | Schedule, RAID, dependencies |

## Inputs

- Project charter or SOW
- Prior workshop notes / artifacts
- Industry scenario context if applicable

## Entry Criteria

- [ ] Objectives defined or draft charter available
- [ ] Participants confirmed
- [ ] Agenda distributed (if workshop)

## Methodology Overview

{methodology}

## Detailed Activities

{activities}

## Deliverables

{deliverables}

## Decision Gates

| Gate | Criteria | Owner |
|------|----------|-------|
| Proceed | Objectives met; open questions logged | BA Lead |
| Escalate | Scope, risk, or conflict unresolved | PM / Sponsor |

## Risks

| Risk | Mitigation |
|------|------------|
| Incomplete attendance | Reschedule; document assumptions |
| Scope creep in session | Parking lot; change control |
| Technical feasibility unknown | Architect follow-up within 5 days |

## Mitigation Strategies

Timebox discussions; pre-reads; decision log; RAID updates same day.

## Quality Checks

- [ ] [../brain/validation-framework.md](../brain/validation-framework.md)
- [ ] [../checklists.md](../checklists.md) applicable sections

## Outputs

Listed under Deliverables; file in project repository with metadata.

## Exit Criteria

- [ ] Deliverables published
- [ ] Actions assigned with owners and dates
- [ ] Next session scheduled or handoff defined

## Lessons Learned

Capture at retrospective: what worked, what to improve next engagement.

## Best Practices

- Prepare with brain modules and knowledge articles
- Label assumptions explicitly
- Standard before custom in fit-gap discussions

## Anti-Patterns

- No documented decisions
- Improvised formats when template exists
- Skipping architect on Extend/Gap items

## AI Execution Guidance

**Ask before proceeding:** industry, clouds, deliverable type, constraints, stakeholders.

**Decision points:** scope boundaries, MoSCoW, fit-gap classification.

**Escalate when:** regulatory implication, material licensing cost, conflicting Must-haves.

**Validate:** anti-hallucination + validation framework before client delivery.

## Related Documents

- [../skill.md](../skill.md)
- [../knowledge/README.md](../knowledge/README.md)
- [../templates/README.md](../templates/README.md)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.5.0 | 2026-07-02 | Sprint 4 enterprise playbook |
"""

def sc_wrap(meta_yaml, exec_summary, problem, objectives, sf_map, epics, stories, ac_sample):
    return meta_yaml + f"""# {meta_yaml.split('title: ')[1].split(chr(10))[0]}

## Executive Summary

{exec_summary}

## Industry Context

Fictional enterprise scenario for BA training and AI-assisted delivery. Company names and data are synthetic.

## Business Problem

{problem}

## Business Objectives

{objectives}

## Scope

**In scope:** Core process on Salesforce clouds listed in metadata.

**Out of scope:** Adjacent systems replacement unless noted in integration landscape.

## Business Capabilities

See capability mapping in Salesforce Capability Mapping section.

## Stakeholders

| Role | Interest |
|------|----------|
| Executive Sponsor | Outcomes, ROI |
| Operations | Workflow fit |
| IT / Integration | APIs, data |
| Compliance | Controls (TBC Legal) |

## Current State

Legacy processes, manual handoffs, fragmented customer data, limited self-service.

## Pain Points

- High manual effort and error rates
- Poor visibility across channels
- SLA breaches and customer dissatisfaction

## Future State

Digitized workflow on Salesforce with integration to systems of record, self-service where appropriate, and measurable KPIs.

## Business Process Flow

```mermaid
flowchart LR
    Start([Trigger]) --> Process[Core Process]
    Process --> Integrate[Integration]
    Integrate --> Complete([Outcome])
```

## Salesforce Capability Mapping

{sf_map}

## Integration Landscape

| System | Role | Pattern |
|--------|------|---------|
| ERP / BSS | System of record | Batch / API TBC |
| IAM | Authentication | SSO SAML/OIDC |
| Data warehouse | Analytics | Batch export |

## Data Considerations

Master data ownership, external IDs, duplicate rules, retention—document in data dictionary.

## Security Considerations

Role-based access, FLS, external user model for portals. See [../knowledge/security-model.md](../knowledge/security-model.md).

## Regulatory & Compliance Considerations

Industry controls documented as TBC with Legal/Compliance—BA does not certify compliance.

## Risks

| ID | Risk | Mitigation |
|----|------|------------|
| R-001 | Integration delay | Mock services for SIT |

## Assumptions

| ID | Assumption | Validate by |
|----|------------|-------------|
| A-001 | API availability | Integration workshop |

## Constraints

Budget, timeline, license edition—confirm with sponsor.

## Dependencies

| ID | Dependency | Needed by |
|----|------------|-----------|
| DEP-001 | IAM SSO | UAT start |

## Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-001 | Core capability for this scenario | Must |

## Non-Functional Requirements

| ID | Category | Requirement |
|----|----------|-------------|
| NFR-001 | Performance | P95 response within agreed SLA |

## Example Epics

{epics}

## Example Features

| Feature | Epic | Value |
|---------|------|-------|
| Core workflow | EP-001 | Primary outcome |

## Example User Stories

{stories}

## Acceptance Criteria

{ac_sample}

## Example Test Scenarios

| TS ID | US ID | Scenario |
|-------|-------|----------|
| TS-001 | US-001 | Happy path end-to-end |

## RTM Example

| BR | FR | US | TS | Status |
|----|----|----|-----|--------|
| BR-001 | FR-001 | US-001 | TS-001 | Proposed |

## Recommended Deliverables

BRD, FRD, process maps, RAID, RTM, UAT pack—see [../templates/README.md](../templates/README.md).

## Solution Recommendation

Standard → Config → Flow before Extend; document in fit-gap. Use [../playbooks/solution-recommendation-playbook.md](../playbooks/solution-recommendation-playbook.md).

## Success Metrics

| KPI | Baseline | Target |
|-----|----------|--------|
| Cycle time | TBC | -20% |
| Customer satisfaction | TBC | +10 pts |

## Lessons Learned

- Validate integration early
- Thin-slice releases
- Security workshops before portal stories

## Best Practices

Load industry scenario + [../brain/reasoning-framework.md](../brain/reasoning-framework.md) before elicitation.

## Common Anti-Patterns

- Screen-first requirements
- Ignoring compliance TBC
- Big-bang go-live

## AI Guidance

**Ask:** volume, channels, systems of record, regulations, release timeline.

**Escalate:** compliance claims, high-volume integration, multi-cloud without priority.

**Outputs:** BRD sections, stories with AC, fit-gap rows, RAID entries.

## Related Documents

- [../scenarios/README.md](../scenarios/README.md)
- [../knowledge/industry-patterns.md](../knowledge/industry-patterns.md)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.6.0 | 2026-07-02 | Sprint 5 industry scenario |
"""

# --- SPRINT 3 TEMPLATES ---
TEMPLATES = {
    "nfr-template.md": tpl_wrap("Non-Functional Requirements", "nfr", "Non-Functional Requirements",
        "Architect, BA, QA, operations", "BRD/FRD in draft", "Business objectives, volume estimates",
        {"content": "### Performance\n| ID | Requirement | Target |\n|----|-------------|--------|\n| NFR-001 | | |\n\n### Availability / Scalability / Security / Compliance / Maintainability / DR\n[Complete per FRD NFR section]"},
        knowledge=["../knowledge/requirement-types.md"], tags=["nfr", "quality"]),
    "solution-scope-template.md": tpl_wrap("Solution Scope", "solution-scope", "Solution Scope",
        "Sponsor, steering, BA", "Charter or discovery complete", "Objectives, constraints",
        {"content": "## Vision\n\n## Business Objectives\n\n## In Scope\n\n## Out of Scope\n\n## Deliverables\n\n## Success Metrics"}),
    "vision-document-template.md": tpl_wrap("Vision Document", "vision", "Vision Document",
        "Executives, steering", "Strategy alignment workshop", "Business drivers",
        {"content": "## Vision Statement\n\n## Business Drivers\n\n## Expected Outcomes\n\n## Strategic Alignment\n\n## Benefits"}),
    "business-case-template.md": tpl_wrap("Business Case", "business-case", "Business Case",
        "Sponsor, finance, steering", "Problem validated", "Cost estimates, options",
        {"content": "## Problem Statement\n\n## Options\n\n## Costs\n\n## Benefits\n\n## ROI\n\n## Risks\n\n## Recommendation"}),
    "workshop-agenda-template.md": tpl_wrap("Workshop Agenda", "workshop-agenda", "Workshop Agenda",
        "Facilitator, participants", "Stakeholders invited", "Objectives, pre-reads",
        {"content": "## Objectives\n\n## Participants\n\n## Pre-reads\n\n## Agenda (timeboxed)\n\n## Decisions\n\n## Actions"},
        playbooks=["../playbooks/discovery-workshop-playbook.md"]),
    "meeting-minutes-template.md": tpl_wrap("Meeting Minutes", "meeting-minutes", "Meeting Minutes",
        "PM, BA, core team", "Meeting held", "Agenda, attendees",
        {"content": "## Date / Attendees\n\n## Agenda\n\n## Discussion\n\n## Decisions\n\n## Actions (owner, date)"}),
    "epic-template.md": tpl_wrap("Epic", "epic", "Epic",
        "PO, BA, architect", "BR approved themes", "Capability map, release plan",
        {"content": "## Epic ID: EP-xxx\n\n## Business Goal\n\n## Scope\n\n## Features\n\n## Dependencies\n\n## Risks\n\n## Acceptance Criteria"},
        knowledge=["../knowledge/epic-design.md"]),
    "feature-template.md": tpl_wrap("Feature", "feature", "Feature",
        "PO, BA", "Epic defined", "Epic ref",
        {"content": "## Feature Description\n\n## Business Value\n\n## Dependencies\n\n## Acceptance Criteria"}),
    "acceptance-criteria-template.md": tpl_wrap("Acceptance Criteria", "acceptance-criteria", "Acceptance Criteria",
        "BA, QA, dev", "User story drafted", "Story, business rules",
        {"content": "## Story ref: US-xxx\n\n### Positive\n1. Given / When / Then\n\n### Negative\n1. Given / When / Then\n\n### Validation rules"},
        knowledge=["../knowledge/acceptance-criteria.md"]),
    "business-rules-template.md": tpl_wrap("Business Rules Catalogue", "business-rules", "Business Rules",
        "BA, admin, architect", "FRD/BRD themes", "Workshop decisions",
        {"content": "| Rule ID | Description | Source | Owner | Priority | Validation |\n|---------|-------------|--------|-------|----------|------------|"},
        knowledge=["../knowledge/business-rules.md"]),
    "decision-log-template.md": tpl_wrap("Decision Log", "decision-log", "Decision Log",
        "Steering, architect, BA", "Decisions occurring", "Options analysis",
        {"content": "| ID | Decision | Rationale | Alternatives | Date | Owner | Impact |\n|----|----------|-----------|--------------|------|-------|--------|"}),
    "rtm-template.md": tpl_wrap("Requirements Traceability Matrix", "rtm", "Traceability Matrix",
        "BA, QA, PM", "Requirements and stories exist", "BRD, FRD, backlog",
        {"content": "| BR | FR | US | TS | Defect | Deployment | Status |\n|----|----|----|----|--------|------------|--------|"},
        knowledge=["../knowledge/requirement-types.md"]),
    "risk-register-template.md": tpl_wrap("Risk Register", "risk-register", "Risk Register",
        "PM, BA, steering", "RAID started", "Workshop outputs",
        {"content": "| ID | Description | Probability | Impact | Severity | Mitigation | Contingency | Owner | Status |"},
        knowledge=["../knowledge/risk-management.md"]),
    "issue-log-template.md": tpl_wrap("Issue Log", "issue-log", "Issue Log",
        "PM, BA", "Issues identified", "RAID",
        {"content": "| ID | Description | Severity | Status | Resolution | Owner | Target date |"}),
    "assumption-log-template.md": tpl_wrap("Assumption Log", "assumption-log", "Assumption Log",
        "BA, PM", "Discovery underway", "Workshop notes",
        {"content": "| ID | Assumption | Validation method | Owner | Review date | Status |"},
        knowledge=["../knowledge/assumptions-management.md"]),
    "dependency-log-template.md": tpl_wrap("Dependency Log", "dependency-log", "Dependency Log",
        "PM, BA", "Plan drafted", "RAID, schedule",
        {"content": "| ID | Dependency | Type | Critical path | Owner | Needed by | Status |"},
        knowledge=["../knowledge/dependency-management.md"]),
    "current-state-template.md": tpl_wrap("Current State Assessment", "current-state", "Current State",
        "BA, business SMEs", "Discovery scheduled", "Interviews, systems list",
        {"content": "## Existing Process\n\n## Systems\n\n## Pain Points\n\n## Metrics\n\n## Opportunities"},
        knowledge=["../knowledge/current-state-analysis.md"]),
    "future-state-template.md": tpl_wrap("Future State Design", "future-state", "Future State",
        "BA, business, architect", "AS-IS documented", "TO-BE workshop",
        {"content": "## Proposed Process\n\n## Automation\n\n## Benefits\n\n## KPIs\n\n## Risks"},
        knowledge=["../knowledge/future-state-design.md"]),
    "process-flow-template.md": tpl_wrap("Process Flow", "process-flow", "Process Flow",
        "BA, business", "AS-IS/TO-BE scope", "Workshop notes",
        {"content": "## Narrative\n\n## Swimlanes / BPMN / Mermaid\n\n```mermaid\nflowchart LR\n    A[Step] --> B[Step]\n```"},
        knowledge=["../knowledge/process-mapping.md", "../knowledge/bpmn.md"]),
    "raci-template.md": tpl_wrap("RACI Matrix", "raci", "RACI",
        "BA, PM", "Processes identified", "Stakeholder list",
        {"content": "| Activity | R | A | C | I |\n|----------|---|---|---|---|"},
        knowledge=["../knowledge/stakeholder-analysis.md"]),
    "stakeholder-matrix-template.md": tpl_wrap("Stakeholder Matrix", "stakeholder-matrix", "Stakeholder Matrix",
        "BA, PM", "Stakeholders identified", "Org context",
        {"content": "| Stakeholder | Role | Influence | Interest | Engagement strategy |"},
        knowledge=["../knowledge/stakeholder-analysis.md"]),
    "data-dictionary-template.md": tpl_wrap("Data Dictionary", "data-dictionary", "Data Dictionary",
        "BA, admin, integration", "Object model draft", "ERD, field list",
        {"content": "| Object | Field | Description | Type | Source | Validation | Owner |"}),
    "api-catalogue-template.md": tpl_wrap("API Catalogue", "api-catalogue", "API Catalogue",
        "BA, architect, integration", "Integration scope", "API specs TBC",
        {"content": "| API | Purpose | Method | Auth | Source | Target | Error handling |"},
        knowledge=["../knowledge/integration-patterns.md"]),
    "migration-plan-template.md": tpl_wrap("Data Migration Plan", "migration-plan", "Migration Plan",
        "BA, data lead", "Migration scope", "Data assessment",
        {"content": "## Strategy\n\n## Mapping\n\n## Validation\n\n## Reconciliation\n\n## Cutover\n\n## Rollback"},
        knowledge=["../knowledge/data-migration.md"]),
    "deployment-checklist-template.md": tpl_wrap("Deployment Checklist", "deployment-checklist", "Deployment Checklist",
        "Release manager, BA, admin", "Release candidate", "Test sign-off",
        {"content": "## Preconditions\n\n## Validation steps\n\n## Deployment tasks\n\n## Rollback\n\n## Sign-off"}),
    "go-live-checklist-template.md": tpl_wrap("Go-Live Checklist", "go-live-checklist", "Go-Live Checklist",
        "Steering, PM, BA", "Deployment complete", "Readiness report",
        {"content": "## Readiness review\n\n## Communication\n\n## Monitoring\n\n## Support / Hypercare\n\n## Exit criteria"},
        knowledge=["../knowledge/release-management.md"]),
    "lessons-learned-template.md": tpl_wrap("Lessons Learned", "lessons-learned", "Lessons Learned",
        "PM, BA, steering", "Phase or project end", "Retrospective inputs",
        {"content": "## Successes\n\n## Challenges\n\n## Root causes\n\n## Recommendations\n\n## Action items"}),
}

# Upgrade headers for key existing templates (prepend sprint 3 sections)
UPGRADE_HEADER = """## Purpose

Enterprise {name} template for Salesforce BA deliverables.

## When to Use

{when}

## Intended Audience

{audience}

## Prerequisites

{prereq}

## Inputs

{inputs}

## Completion Instructions

1. Complete metadata and document control.
2. Replace placeholders; assign unique IDs.
3. Run [../checklists.md](../checklists.md) before review.

---

"""

PLAYBOOKS = {
    "discovery-workshop-playbook.md": ("Discovery Workshop", "Initiate engagement; identify stakeholders; define objectives and scope.", "| Discovery summary | Stakeholder list | Initial scope | Objectives | RAID |", "1. Prepare agenda\n2. Facilitate AS-IS pain\n3. Capture TO-BE themes\n4. MoSCoW draft\n5. Close with decisions", ["discovery", "workshop"]),
    "requirement-workshop-playbook.md": ("Requirement Workshop", "Elicit and prioritize requirements in structured workshop.", "| Workshop notes | Stories | AC | Business rules | Open questions |", "1. Review pre-reads\n2. Elicit FR/NFR\n3. Resolve conflicts\n4. Prioritize\n5. Publish notes", ["requirements", "workshop"]),
    "sprint-planning-playbook.md": ("Sprint Planning", "Plan sprint goal, capacity, and backlog commitment.", "| Sprint backlog | Sprint goal | Risks | Dependencies |", "1. Review DoR stories\n2. Capacity plan\n3. Commit\n4. Identify deps", ["agile", "sprint"]),
    "backlog-grooming-playbook.md": ("Backlog Grooming", "Refine backlog ordering and story readiness.", "| Refined backlog | Split stories | Priority updates |", "1. Review epic map\n2. Split large stories\n3. Update WSJF/MoSCoW", ["backlog", "grooming"]),
    "story-refinement-playbook.md": ("Story Refinement", "INVEST refinement with AC and data notes.", "| Ready stories | AC | Test notes |", "1. Walk through INVEST\n2. Add AC\n3. Architect flags", ["stories", "refinement"]),
    "uat-planning-playbook.md": ("UAT Planning", "Plan business UAT scope, data, and sign-off.", "| UAT plan | Scenarios | Entry/exit | Sign-off template |", "1. Map RTM\n2. Draft scenarios\n3. Schedule business testers", ["uat", "testing"]),
    "current-state-assessment-playbook.md": ("Current State Assessment", "Document AS-IS processes and systems.", "| AS-IS maps | Pain list | Systems landscape |", "1. Interview\n2. Observe\n3. Synthesize", ["as-is", "discovery"]),
    "gap-analysis-playbook.md": ("Gap Analysis", "AS-IS vs TO-BE gap and fit-gap classification.", "| Gap list | Fit-gap matrix | Recommendations |", "1. Compare states\n2. Classify Standard/Config/Extend/Gap\n3. Recommend", ["fit-gap", "gap"]),
    "value-stream-mapping-playbook.md": ("Value Stream Mapping", "End-to-end value stream and waste identification.", "| VSM diagram | Improvements | KPI baseline |", "1. Map stream\n2. Identify waste\n3. Prioritize improvements", ["value-stream"]),
    "business-capability-assessment-playbook.md": ("Business Capability Assessment", "Capability map and maturity assessment.", "| Capability map | Maturity | Roadmap |", "1. Identify capabilities\n2. Heat map\n3. Align to releases", ["capability"]),
    "executive-presentation-playbook.md": ("Executive Presentation", "Prepare executive messaging and decision requests.", "| Executive deck | Decision summary | Actions |", "1. Audience analysis\n2. Value/risk narrative\n3. Decision asks", ["executive"]),
    "solution-recommendation-playbook.md": ("Solution Recommendation", "Options analysis and Salesforce recommendation.", "| Recommendation report | Decision matrix | Roadmap |", "1. Problem framing\n2. Options\n3. Fit-gap\n4. Recommend", ["solution", "recommendation"]),
    "governance-meeting-playbook.md": ("Governance Meeting", "Run architecture/governance forum.", "| Minutes | Decision log | Actions |", "1. RAID review\n2. Standards check\n3. Decisions", ["governance"]),
    "steering-committee-playbook.md": ("Steering Committee", "Executive steering pack and approvals.", "| Steering pack | Executive summary | RAID review |", "1. Status\n2. Budget/timeline\n3. Decisions", ["steering"]),
    "production-readiness-playbook.md": ("Production Readiness", "Go-live readiness and hypercare prep.", "| Readiness report | Go-live checklist | Risk assessment |", "1. Env validation\n2. Migration sign-off\n3. Hypercare plan", ["go-live", "readiness"]),
}

SCENARIOS = {
    "utilities": [
        ("customer-onboarding.md", "Utilities Customer Onboarding", "Customer registration, property validation, meter assignment, welcome comms", "Reduce onboarding time 30%", "Service Cloud, Experience Cloud, Platform", "EP-001 Onboarding", "US-001 As a new customer I want to complete registration online so that service starts on time", "Given valid address When submit Then account created"),
        ("meter-to-cash.md", "Utilities Meter-to-Cash", "Meter read through billing and payment", "Improve billing accuracy", "Service Cloud, Revenue Cloud, Platform", "EP-002 Meter-to-Cash", "US-002 As billing ops I want validated reads ingested so that bills are accurate", "Given estimated read When actual received Then bill recalculated"),
        ("billing.md", "Utilities Billing", "Billing cycles, tariffs, adjustments, rebills", "Reduce rebill rate", "Service Cloud, Platform", "EP-003 Billing", "US-003 As customer I want transparent bill breakdown", "Given bill generated When view portal Then line items shown"),
        ("complaints.md", "Utilities Complaints", "Complaint intake, investigation, SLA, escalation", "Meet regulatory SLA", "Service Cloud, Omni-Channel", "EP-004 Complaints", "US-004 As customer I want to log complaint and track status", "Given complaint submitted When SLA breached Then escalate"),
        ("field-service.md", "Utilities Field Service", "Work orders, dispatch, mobile workforce", "First-time fix rate up", "Field Service, Service Cloud", "EP-005 Field Service", "US-005 As dispatcher I want optimized schedule", "Given emergency When dispatch Then nearest tech assigned"),
        ("outages.md", "Utilities Outages", "Incident, impact, comms, restoration", "Restore faster", "Service Cloud, Experience Cloud, Marketing Cloud", "EP-006 Outages", "US-006 As customer I want outage notifications", "Given outage When registered Then SMS sent"),
        ("collections.md", "Utilities Collections", "Debt, payment plans, dunning", "Reduce write-offs", "Service Cloud, Platform", "EP-007 Collections", "US-007 As agent I want payment plan offers", "Given overdue When contact Then plan options shown"),
    ],
    "retail": [
        ("order-management.md", "Retail Order Management", "Omnichannel order capture and fulfillment", "OTIF improvement", "Commerce Cloud, Service Cloud, Platform", "EP-101 OMS", "US-101 As shopper I want buy online pickup in store", "Given order placed When ready Then notify customer"),
        ("returns.md", "Retail Returns", "Returns, refunds, exchanges", "Faster refunds", "Service Cloud, Commerce Cloud", "EP-102 Returns", "US-102 As customer I want return label online", "Given return initiated When received Then refund in 3 days"),
        ("loyalty.md", "Retail Loyalty", "Points, tiers, rewards", "Increase repeat purchase", "Marketing Cloud, Sales Cloud", "EP-103 Loyalty", "US-103 As member I want see points balance", "Given purchase When complete Then points credited"),
        ("promotions.md", "Retail Promotions", "Campaigns, pricing, eligibility", "Campaign ROI", "Marketing Cloud, Commerce Cloud", "EP-104 Promotions", "US-104 As marketer I want segment promotions", "Given segment When campaign runs Then offer applied"),
        ("inventory.md", "Retail Inventory Visibility", "Stock visibility across channels", "Reduce stockouts", "Commerce Cloud, Data Cloud", "EP-105 Inventory", "US-105 As associate I want real-time stock", "Given SKU When query Then ATP returned"),
    ],
    "healthcare": [
        ("patient-onboarding.md", "Healthcare Patient Onboarding", "Registration, consent, insurance capture", "Reduce intake time", "Health Cloud, Experience Cloud", "EP-201 Onboarding", "US-201 As patient I want digital intake forms", "Given referral When complete intake Then chart created"),
        ("appointments.md", "Healthcare Appointments", "Scheduling, reminders, cancellations", "No-show reduction", "Health Cloud, Service Cloud", "EP-202 Scheduling", "US-202 As patient I want book appointment online", "Given slot When book Then confirmation sent"),
        ("claims.md", "Healthcare Claims", "Claims intake and status", "Faster adjudication visibility", "Health Cloud, Platform", "EP-203 Claims", "US-203 As member I want claim status", "Given claim filed When update Then portal shows status"),
        ("care-management.md", "Healthcare Care Management", "Care plans, care team coordination", "Care plan adherence", "Health Cloud, Service Cloud", "EP-204 Care Mgmt", "US-204 As care manager I want care plan tasks", "Given plan When task due Then notify team"),
    ],
    "insurance": [
        ("quote-to-bind.md", "Insurance Quote to Bind", "Quote, rate, bind policy", "Quote conversion", "Sales Cloud, Industries Cloud", "EP-301 Quote-Bind", "US-301 As agent I want generate quote", "Given risk data When rate Then premium shown"),
        ("fnol.md", "Insurance FNOL", "First notice of loss", "FNOL digital adoption", "Service Cloud, Experience Cloud", "EP-302 FNOL", "US-302 As policyholder I want file claim online", "Given incident When submit FNOL Then claim created"),
        ("claims.md", "Insurance Claims Management", "Investigation, adjustment, payment", "Cycle time reduction", "Service Cloud, Industries Cloud", "EP-303 Claims", "US-303 As adjuster I want task queue", "Given claim When assign Then tasks created"),
        ("underwriting.md", "Insurance Underwriting", "Risk evaluation, rules, referral", "Straight-through processing", "Industries Cloud, Platform", "EP-304 UW", "US-304 As underwriter I want risk dashboard", "Given submission When rules pass Then auto-approve"),
    ],
    "telecom": [
        ("order-capture.md", "Telecom Order Capture", "Product catalog, order validation", "Order fallout reduction", "Sales Cloud, Industries Cloud", "EP-401 Order", "US-401 As sales I want configure bundle", "Given catalog When select Then price calculated"),
        ("activation.md", "Telecom Activation", "Service activation workflow", "Activation time", "Service Cloud, Platform", "EP-402 Activation", "US-402 As ops I want activation status", "Given order When paid Then activate"),
        ("provisioning.md", "Telecom Provisioning", "Network provisioning integration", "Provision SLA", "Platform, MuleSoft pattern", "EP-403 Provision", "US-403 As provisioner I want work order to OSS", "Given activation When trigger Then OSS job created"),
        ("billing.md", "Telecom Billing", "Usage, rating, billing integration", "Bill accuracy", "Service Cloud, Revenue Cloud", "EP-404 Billing", "US-404 As customer I want usage on bill", "Given cycle When close Then usage rated"),
    ],
    "banking": [
        ("kyc.md", "Banking KYC", "Customer verification, AML screening", "KYC cycle time", "Financial Services Cloud, Platform", "EP-501 KYC", "US-501 As onboarding I want KYC checklist", "Given applicant When docs uploaded Then screening started"),
        ("loan-origination.md", "Banking Loan Origination", "Application, decision, disbursement", "Time to yes", "FSC, Sales Cloud", "EP-502 Loans", "US-502 As applicant I want apply online", "Given application When submit Then case created"),
        ("credit.md", "Banking Credit Assessment", "Credit decision, bureau integration", "Decision accuracy", "FSC, Platform", "EP-503 Credit", "US-503 As underwriter I want bureau pull", "Given consent When pull Then score stored"),
        ("collections.md", "Banking Collections", "Delinquency, outreach, arrangements", "Cure rate", "Service Cloud, FSC", "EP-504 Collections", "US-504 As collector I want prioritized queue", "Given delinquent When contact Then arrangement offered"),
    ],
}

def main():
    TPL.mkdir(parents=True, exist_ok=True)
    PB.mkdir(parents=True, exist_ok=True)

    for fname, content in TEMPLATES.items():
        (TPL / fname).write_text(content, encoding="utf-8")
        print("template", fname)

    for fname, (title, overview, deliverables, activities, tags) in PLAYBOOKS.items():
        content = pb_wrap(title, overview, deliverables, activities, tags)
        (PB / fname).write_text(content, encoding="utf-8")
        print("playbook", fname)

    for industry, items in SCENARIOS.items():
        d = SC / industry
        d.mkdir(parents=True, exist_ok=True)
        for fname, title, problem, objectives, clouds, epics, stories, ac in items:
            meta = sc_yaml(title, industry, fname.replace(".md", "").replace("-", " "), clouds)
            sf = f"| Capability | Salesforce |\n|------------|------------|\n| Core process | {clouds.split(',')[0].strip()} |\n| Portal/self-service | Experience Cloud |\n| Integration | Platform APIs |"
            content = sc_wrap(meta, f"Synthetic {industry} scenario: {title}.", problem, objectives, sf, f"**{epics}** — measurable business outcome.", f"**{stories}**", f"**{ac}**")
            (d / fname).write_text(content, encoding="utf-8")
            print("scenario", industry, fname)

    # README files
    tpl_readme = "# Enterprise Template Library (Sprint 3)\n\nVersion **0.4.0**. See specification in `zzz_ImplmentationGuide/Sprint 3 Specification.docx`.\n\n"
    tpl_readme += "\n".join(f"- [{f}]({f})" for f in sorted(TEMPLATES.keys()) + [
        "brd-template.md", "frd-template.md", "user-story-template.md", "raid-log-template.md", "traceability-matrix-template.md"
    ])
    (TPL / "README.md").write_text(tpl_readme, encoding="utf-8")

    pb_readme = "# Enterprise Playbook Library (Sprint 4)\n\nVersion **0.5.0**.\n\n"
    pb_readme += "\n".join(f"- [{f}]({f})" for f in sorted(PLAYBOOKS.keys()) + [
        "discovery-playbook.md", "requirements-elicitation.md", "fit-gap-analysis.md", "uat-playbook.md"
    ])
    (PB / "README.md").write_text(pb_readme, encoding="utf-8")

    sc_readme = "# Industry Scenario Library (Sprint 5)\n\nVersion **0.6.0**.\n\n"
    for ind in SCENARIOS:
        sc_readme += f"\n## {ind.title()}\n"
        for fname, *_ in SCENARIOS[ind]:
            sc_readme += f"- [{fname}]({ind}/{fname})\n"
    sc_readme += "\n## Legacy industry overviews\n- [financial-services.md](financial-services.md)\n- [healthcare.md](healthcare.md)\n- [manufacturing.md](manufacturing.md)\n- [public-sector.md](public-sector.md)\n"
    (SC / "README.md").write_text(sc_readme, encoding="utf-8")

    print("DONE")

if __name__ == "__main__":
    main()
