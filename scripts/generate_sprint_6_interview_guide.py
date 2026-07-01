"""Generate Sprint 6 Enterprise Interview Intelligence Framework (v1.0.0)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "salesforce-business-analyst"
IG = ROOT / "interview-guide"

DIFFICULTIES = ["Beginner", "Intermediate", "Senior", "Lead", "Principal"]
INTERVIEW_TYPES = ["Screening", "Technical", "Functional", "Consulting", "Leadership", "Executive"]

QUESTION_COUNTS: dict[str, int] = {
    "business-analysis.md": 50,
    "requirement-gathering.md": 40,
    "current-state.md": 25,
    "future-state.md": 25,
    "user-stories.md": 40,
    "acceptance-criteria.md": 20,
    "stakeholders.md": 30,
    "salesforce/crm.md": 20,
    "salesforce/sales-cloud.md": 20,
    "salesforce/service-cloud.md": 25,
    "salesforce/experience-cloud.md": 20,
    "salesforce/cpq.md": 15,
    "salesforce/industries.md": 25,
    "delivery/architecture.md": 25,
    "delivery/agile.md": 25,
    "delivery/scrum.md": 20,
    "delivery/risk-management.md": 20,
    "delivery/communication.md": 20,
    "delivery/leadership.md": 20,
    "advanced/scenario-questions.md": 60,
    "advanced/case-studies.md": 40,
    "advanced/whiteboard-exercises.md": 25,
    "advanced/behavioral.md": 40,
    "advanced/executive-communication.md": 20,
}

TOPIC_META: dict[str, dict] = {
    "business-analysis.md": {
        "title": "Business Analysis Interview Questions",
        "difficulty": "Intermediate",
        "clouds": "Platform",
        "brain": ["identity.md", "consulting-principles.md", "reasoning-framework.md"],
        "knowledge": ["business-analysis-fundamentals.md", "babok-guide.md", "requirement-types.md"],
        "templates": ["brd-template.md", "frd-template.md"],
        "playbooks": ["discovery-workshop-playbook.md", "requirement-workshop-playbook.md"],
        "scenarios": ["banking/loan-origination.md"],
        "tags": ["business-analysis", "babok", "consulting"],
        "overview": "BA responsibilities, lifecycle, deliverables, BABOK concepts, consulting mindset, and stakeholder management.",
    },
    "requirement-gathering.md": {
        "title": "Requirement Gathering Interview Questions",
        "difficulty": "Intermediate",
        "clouds": "Platform",
        "brain": ["enterprise-behaviors.md", "communication-framework.md", "reasoning-framework.md"],
        "knowledge": ["requirement-types.md", "requirements-engineering.md", "moscow-prioritization.md"],
        "templates": ["workshop-agenda-template.md", "meeting-minutes-template.md"],
        "playbooks": ["discovery-workshop-playbook.md", "requirement-workshop-playbook.md"],
        "scenarios": ["retail/returns.md"],
        "tags": ["elicitation", "workshops", "requirements"],
        "overview": "Workshops, interviews, observation, questioning techniques, validation, prioritization, and scope management.",
    },
    "current-state.md": {
        "title": "Current State Analysis Interview Questions",
        "difficulty": "Intermediate",
        "clouds": "Platform",
        "brain": ["reasoning-framework.md", "anti-hallucination.md"],
        "knowledge": ["current-state-analysis.md", "process-mapping.md", "business-analysis-fundamentals.md"],
        "templates": ["current-state-template.md", "process-flow-template.md"],
        "playbooks": ["discovery-workshop-playbook.md", "gap-analysis-playbook.md"],
        "scenarios": ["utilities/meter-to-cash.md"],
        "tags": ["current-state", "as-is", "discovery"],
        "overview": "As-Is analysis, pain points, process discovery, existing systems, and metrics.",
    },
    "future-state.md": {
        "title": "Future State Design Interview Questions",
        "difficulty": "Senior",
        "clouds": "Platform",
        "brain": ["reasoning-framework.md", "decision-framework.md"],
        "knowledge": ["future-state-design.md", "process-mapping.md", "governance-framework.md"],
        "templates": ["future-state-template.md", "solution-scope-template.md"],
        "playbooks": ["solution-recommendation-playbook.md", "gap-analysis-playbook.md"],
        "scenarios": ["healthcare/appointments.md"],
        "tags": ["future-state", "to-be", "transformation"],
        "overview": "To-Be design, target operating model, transformation, process improvement, and automation.",
    },
    "user-stories.md": {
        "title": "User Stories Interview Questions",
        "difficulty": "Intermediate",
        "clouds": "Sales Cloud, Service Cloud",
        "brain": ["output-framework.md", "validation-framework.md"],
        "knowledge": ["user-stories.md", "acceptance-criteria.md", "epic-design.md"],
        "templates": ["user-story-template.md", "epic-template.md", "feature-template.md"],
        "playbooks": ["story-refinement-playbook.md", "sprint-planning-playbook.md"],
        "scenarios": ["telecom/order-capture.md"],
        "tags": ["user-stories", "invest", "agile"],
        "overview": "INVEST, story decomposition, refinement, estimation readiness, and acceptance criteria linkage.",
    },
    "acceptance-criteria.md": {
        "title": "Acceptance Criteria Interview Questions",
        "difficulty": "Intermediate",
        "clouds": "Platform",
        "brain": ["validation-framework.md", "output-framework.md"],
        "knowledge": ["acceptance-criteria.md", "user-stories.md", "requirements-engineering.md"],
        "templates": ["user-story-template.md", "acceptance-criteria-template.md"],
        "playbooks": ["story-refinement-playbook.md", "uat-planning-playbook.md"],
        "scenarios": ["insurance/claims.md"],
        "tags": ["acceptance-criteria", "gherkin", "testability"],
        "overview": "Given/When/Then, Definition of Done, testability, and validation.",
    },
    "stakeholders.md": {
        "title": "Stakeholder Management Interview Questions",
        "difficulty": "Senior",
        "clouds": "Platform",
        "brain": ["enterprise-behaviors.md", "communication-framework.md"],
        "knowledge": ["stakeholder-analysis.md", "governance-framework.md", "requirements-engineering.md"],
        "templates": ["stakeholder-matrix-template.md", "meeting-minutes-template.md"],
        "playbooks": ["steering-committee-playbook.md", "executive-presentation-playbook.md"],
        "scenarios": ["banking/loan-origination.md"],
        "tags": ["stakeholders", "facilitation", "executive"],
        "overview": "Identification, power-interest matrix, communication, conflict resolution, and executive engagement.",
    },
    "salesforce/crm.md": {
        "title": "Salesforce CRM Platform Interview Questions",
        "difficulty": "Intermediate",
        "clouds": "Platform, Sales Cloud, Service Cloud",
        "brain": ["decision-framework.md", "reasoning-framework.md"],
        "knowledge": ["salesforce-clouds-overview.md", "salesforce-platform.md", "security-model.md"],
        "templates": ["data-dictionary-template.md", "brd-template.md"],
        "playbooks": ["solution-recommendation-playbook.md"],
        "scenarios": ["retail/loyalty.md"],
        "tags": ["crm", "platform", "data-model"],
        "overview": "Core CRM concepts, standard objects, relationships, sharing, and platform fundamentals.",
    },
    "salesforce/sales-cloud.md": {
        "title": "Sales Cloud Interview Questions",
        "difficulty": "Intermediate",
        "clouds": "Sales Cloud",
        "brain": ["decision-framework.md"],
        "knowledge": ["salesforce-clouds-overview.md", "salesforce-platform.md", "industry-patterns.md"],
        "templates": ["brd-template.md", "user-story-template.md"],
        "playbooks": ["discovery-workshop-playbook.md"],
        "scenarios": ["banking/loan-origination.md"],
        "tags": ["sales-cloud", "pipeline", "leads"],
        "overview": "Lead/opportunity lifecycle, forecasting, territory, and sales process design.",
    },
    "salesforce/service-cloud.md": {
        "title": "Service Cloud Interview Questions",
        "difficulty": "Intermediate",
        "clouds": "Service Cloud",
        "brain": ["decision-framework.md"],
        "knowledge": ["salesforce-platform.md", "salesforce-clouds-overview.md", "integration-patterns.md"],
        "templates": ["brd-template.md", "process-flow-template.md"],
        "playbooks": ["discovery-workshop-playbook.md"],
        "scenarios": ["utilities/outages.md"],
        "tags": ["service-cloud", "cases", "omnichannel"],
        "overview": "Case management, entitlements, knowledge, omnichannel, and service metrics.",
    },
    "salesforce/experience-cloud.md": {
        "title": "Experience Cloud Interview Questions",
        "difficulty": "Senior",
        "clouds": "Experience Cloud",
        "brain": ["decision-framework.md", "communication-framework.md"],
        "knowledge": ["salesforce-clouds-overview.md", "security-model.md", "salesforce-platform.md"],
        "templates": ["brd-template.md", "nfr-template.md"],
        "playbooks": ["solution-recommendation-playbook.md"],
        "scenarios": ["healthcare/patient-onboarding.md"],
        "tags": ["experience-cloud", "portal", "community"],
        "overview": "Portals, partner communities, authentication, sharing sets, and self-service design.",
    },
    "salesforce/cpq.md": {
        "title": "CPQ Interview Questions",
        "difficulty": "Senior",
        "clouds": "CPQ",
        "brain": ["decision-framework.md"],
        "knowledge": ["industry-patterns.md", "salesforce-clouds-overview.md", "business-rules.md"],
        "templates": ["brd-template.md", "frd-template.md"],
        "playbooks": ["solution-recommendation-playbook.md"],
        "scenarios": ["telecom/order-capture.md"],
        "tags": ["cpq", "quoting", "pricing"],
        "overview": "Product catalog, pricing rules, approvals, and quote-to-order integration.",
    },
    "salesforce/industries.md": {
        "title": "Salesforce Industries Interview Questions",
        "difficulty": "Senior",
        "clouds": "Industries",
        "brain": ["decision-framework.md", "reasoning-framework.md"],
        "knowledge": ["industry-patterns.md", "salesforce-clouds-overview.md"],
        "templates": ["brd-template.md", "solution-scope-template.md"],
        "playbooks": ["discovery-workshop-playbook.md"],
        "scenarios": ["insurance/claims.md", "banking/loan-origination.md"],
        "tags": ["industries", "fsc", "vlocity"],
        "overview": "Industry cloud capability mapping, regulated industries, and business capability over feature memorization.",
    },
    "delivery/architecture.md": {
        "title": "Solution Architecture Interview Questions",
        "difficulty": "Senior",
        "clouds": "Platform",
        "brain": ["decision-framework.md", "reasoning-framework.md"],
        "knowledge": ["integration-patterns.md", "security-model.md", "data-migration.md"],
        "templates": ["api-catalogue-template.md", "nfr-template.md"],
        "playbooks": ["solution-recommendation-playbook.md"],
        "scenarios": ["utilities/field-service.md"],
        "tags": ["architecture", "integration", "security"],
        "overview": "Solution architecture, integration, data model, security, scalability, and governance.",
    },
    "delivery/agile.md": {
        "title": "Agile Delivery Interview Questions",
        "difficulty": "Intermediate",
        "clouds": "Platform",
        "brain": ["enterprise-behaviors.md", "output-framework.md"],
        "knowledge": ["epic-design.md", "user-stories.md", "release-management.md"],
        "templates": ["epic-template.md", "user-story-template.md"],
        "playbooks": ["sprint-planning-playbook.md", "story-refinement-playbook.md"],
        "scenarios": ["retail/order-management.md"],
        "tags": ["agile", "safe", "backlog"],
        "overview": "Scrum, Kanban, SAFe awareness, sprint ceremonies, and backlog management.",
    },
    "delivery/scrum.md": {
        "title": "Scrum Interview Questions",
        "difficulty": "Intermediate",
        "clouds": "Platform",
        "brain": ["enterprise-behaviors.md"],
        "knowledge": ["epic-design.md", "user-stories.md"],
        "templates": ["epic-template.md", "lessons-learned-template.md"],
        "playbooks": ["sprint-planning-playbook.md", "story-refinement-playbook.md"],
        "scenarios": ["healthcare/care-management.md"],
        "tags": ["scrum", "ceremonies", "estimation"],
        "overview": "Roles, events, artifacts, estimation, and refinement.",
    },
    "delivery/risk-management.md": {
        "title": "Risk Management Interview Questions",
        "difficulty": "Senior",
        "clouds": "Platform",
        "brain": ["enterprise-behaviors.md", "validation-framework.md"],
        "knowledge": ["risk-management.md", "governance-framework.md", "assumptions-management.md"],
        "templates": ["raid-log-template.md", "risk-register-template.md"],
        "playbooks": ["production-readiness-playbook.md", "steering-committee-playbook.md"],
        "scenarios": ["insurance/claims.md"],
        "tags": ["risk", "raid", "governance"],
        "overview": "Risk identification, mitigation, RAID, governance, and escalation.",
    },
    "delivery/communication.md": {
        "title": "Communication Interview Questions",
        "difficulty": "Senior",
        "clouds": "Platform",
        "brain": ["communication-framework.md", "enterprise-behaviors.md"],
        "knowledge": ["stakeholder-analysis.md", "governance-framework.md"],
        "templates": ["meeting-minutes-template.md", "business-case-template.md"],
        "playbooks": ["executive-presentation-playbook.md"],
        "scenarios": ["banking/loan-origination.md"],
        "tags": ["communication", "facilitation", "presentation"],
        "overview": "Executive communication, difficult conversations, facilitation, active listening, and presentations.",
    },
    "delivery/leadership.md": {
        "title": "Leadership Interview Questions",
        "difficulty": "Lead",
        "clouds": "Platform",
        "brain": ["consulting-principles.md", "enterprise-behaviors.md"],
        "knowledge": ["governance-framework.md", "stakeholder-analysis.md"],
        "templates": ["decision-log-template.md", "stakeholder-matrix-template.md"],
        "playbooks": ["steering-committee-playbook.md"],
        "scenarios": ["utilities/billing.md"],
        "tags": ["leadership", "mentoring", "influence"],
        "overview": "Mentoring, decision making, influence, conflict management, and team collaboration.",
    },
    "advanced/scenario-questions.md": {
        "title": "Scenario-Based Interview Questions",
        "difficulty": "Senior",
        "clouds": "Platform",
        "brain": ["reasoning-framework.md", "decision-framework.md", "enterprise-behaviors.md"],
        "knowledge": ["business-analysis-fundamentals.md", "salesforce-clouds-overview.md"],
        "templates": ["brd-template.md", "solution-scope-template.md"],
        "playbooks": ["discovery-workshop-playbook.md", "gap-analysis-playbook.md"],
        "scenarios": ["banking/loan-origination.md", "retail/returns.md"],
        "tags": ["scenario", "consulting", "case"],
        "overview": "Real-world Salesforce consulting scenarios with context, constraints, and evaluation criteria.",
    },
    "advanced/case-studies.md": {
        "title": "Case Study Interview Exercises",
        "difficulty": "Senior",
        "clouds": "Platform",
        "brain": ["reasoning-framework.md", "output-framework.md"],
        "knowledge": ["industry-patterns.md", "integration-patterns.md"],
        "templates": ["brd-template.md", "current-state-template.md"],
        "playbooks": ["discovery-workshop-playbook.md", "solution-recommendation-playbook.md"],
        "scenarios": ["healthcare/appointments.md", "insurance/claims.md"],
        "tags": ["case-study", "analysis", "solution"],
        "overview": "Industry case studies with objectives, requirements, deliverables, and discussion questions.",
    },
    "advanced/whiteboard-exercises.md": {
        "title": "Whiteboard Interview Exercises",
        "difficulty": "Senior",
        "clouds": "Platform",
        "brain": ["reasoning-framework.md", "communication-framework.md"],
        "knowledge": ["process-mapping.md", "integration-patterns.md"],
        "templates": ["process-flow-template.md", "data-dictionary-template.md"],
        "playbooks": ["discovery-workshop-playbook.md"],
        "scenarios": ["telecom/order-capture.md"],
        "tags": ["whiteboard", "diagram", "architecture"],
        "overview": "Process mapping, capability mapping, data model, integration, and solution architecture exercises.",
    },
    "advanced/behavioral.md": {
        "title": "Behavioral Interview Questions",
        "difficulty": "Senior",
        "clouds": "Platform",
        "brain": ["consulting-principles.md", "enterprise-behaviors.md"],
        "knowledge": ["governance-framework.md", "stakeholder-analysis.md"],
        "templates": ["meeting-minutes-template.md"],
        "playbooks": ["discovery-workshop-playbook.md"],
        "scenarios": ["banking/loan-origination.md"],
        "tags": ["behavioral", "star", "soft-skills"],
        "overview": "STAR-framework behavioral questions on leadership, collaboration, conflict, learning, and ethics.",
    },
    "advanced/executive-communication.md": {
        "title": "Executive Communication Interview Questions",
        "difficulty": "Lead",
        "clouds": "Platform",
        "brain": ["communication-framework.md", "consulting-principles.md"],
        "knowledge": ["governance-framework.md", "stakeholder-analysis.md"],
        "templates": ["business-case-template.md", "vision-document-template.md"],
        "playbooks": ["executive-presentation-playbook.md", "steering-committee-playbook.md"],
        "scenarios": ["utilities/billing.md"],
        "tags": ["executive", "steering", "business-case"],
        "overview": "Executive presentations, business cases, recommendations, steering committees, and governance.",
    },
}

SEED_QUESTIONS: dict[str, list[str]] = {
    "business-analysis.md": [
        "What is the primary role of a Salesforce Business Analyst on an enterprise transformation program?",
        "How do you differentiate business requirements from functional requirements in a BRD?",
        "Describe the BA lifecycle from discovery through UAT on a multi-cloud program.",
        "How does BABOK inform your approach to Salesforce engagements?",
        "What deliverables do you produce at each phase of a Salesforce implementation?",
        "How do you maintain traceability from business goals to user stories?",
        "When would you escalate a scope conflict to the steering committee?",
        "How do you balance speed of delivery with documentation quality?",
        "What consulting mindset behaviors distinguish a senior BA from a junior BA?",
        "How do you handle a sponsor who wants to skip discovery and go straight to build?",
    ],
    "requirement-gathering.md": [
        "How do you prepare for a requirements workshop with conflicting stakeholder groups?",
        "What questioning techniques do you use to uncover unstated assumptions?",
        "How do you validate requirements without leading the stakeholder to your preferred answer?",
        "Describe your approach to prioritizing requirements when everything is marked Must-have.",
        "How do you manage scope creep during elicitation sessions?",
        "When do you use observation versus interview versus document analysis?",
        "How do you document decisions made in a workshop in real time?",
        "What is your process for confirming requirements with absent stakeholders?",
        "How do you elicit non-functional requirements during functional workshops?",
        "How do you close an elicitation cycle and obtain sign-off?",
    ],
    "current-state.md": [
        "How do you document an As-Is process without getting lost in edge cases?",
        "What sources do you triangulate when stakeholders disagree on the current process?",
        "How do you identify pain points that are symptoms versus root causes?",
        "What metrics do you capture during current state analysis?",
        "How do you map existing systems and integration touchpoints?",
        "When is a current state diagram sufficient versus needing a detailed swimlane?",
        "How do you handle undocumented tribal knowledge?",
        "What red flags in current state analysis suggest integration risk?",
        "How do you present current state findings to executives?",
        "How do you validate current state documentation with operations teams?",
    ],
    "future-state.md": [
        "How do you design a To-Be process that balances automation with human judgment?",
        "What is your approach to defining a target operating model on Salesforce?",
        "How do you quantify benefits in a future state proposal?",
        "When should a future state defer automation to a later release?",
        "How do you align future state design with change management readiness?",
        "What role does the capability map play in future state design?",
        "How do you handle future state designs that require organizational restructuring?",
        "How do you document assumptions in future state recommendations?",
        "How do you validate future state with both business and IT architects?",
        "What trade-offs do you surface when proposing process standardization?",
    ],
    "user-stories.md": [
        "How do you split an epic into INVEST-compliant user stories?",
        "What makes a user story too large for a single sprint?",
        "How do you write stories that account for Salesforce permissions and sharing?",
        "When should a story include integration acceptance criteria?",
        "How do you link user stories to business requirement IDs?",
        "What is your approach to story refinement with a distributed team?",
        "How do you handle stories that span multiple clouds?",
        "What anti-patterns do you correct during backlog grooming?",
        "How do you ensure stories are estimable before sprint planning?",
        "How do you document data dependencies in user stories?",
    ],
    "acceptance-criteria.md": [
        "How do you write Given/When/Then criteria for a Salesforce screen flow?",
        "What negative test scenarios must AC cover for a community portal?",
        "How do you define Definition of Done for a Salesforce sprint?",
        "When should AC reference specific profiles or permission sets?",
        "How do you make bulk data scenarios testable in AC?",
        "What is the difference between AC and UAT test scripts?",
        "How do you validate AC with business users who are not technical?",
        "How many AC per story is appropriate for enterprise delivery?",
        "How do you write AC for integration error handling?",
        "How do you prevent untestable AC like 'system shall be user-friendly'?",
    ],
    "stakeholders.md": [
        "How do you build a stakeholder map for a global Salesforce rollout?",
        "How do you engage a resistant middle manager who fears job displacement?",
        "What is your approach to managing executive sponsors with limited availability?",
        "How do you resolve conflicting priorities between Sales and Service leaders?",
        "How do you identify hidden influencers on a program?",
        "What communication cadence do you recommend for steering committee members?",
        "How do you handle stakeholders who bypass governance to demand scope changes?",
        "How do you document RACI for requirements sign-off?",
        "When do you use one-on-one interviews versus group workshops for stakeholders?",
        "How do you maintain trust after delivering bad news about scope or timeline?",
    ],
    "salesforce/crm.md": [
        "When would you use a custom object versus extending a standard object?",
        "How do you explain the Salesforce sharing model to a business audience?",
        "What decisions do you document when defining lead conversion mapping?",
        "How do you approach duplicate management in a multi-source lead environment?",
        "What is your process for validating whether Person Accounts are appropriate?",
        "How do you document record type strategy in requirements?",
        "When should master-detail versus lookup relationships be used?",
        "How do you capture platform limits considerations in requirements?",
        "What governance do you recommend for field proliferation?",
        "How do you align CRM data model decisions with integration architecture?",
    ],
    "salesforce/sales-cloud.md": [
        "How do you document opportunity stage criteria and exit requirements?",
        "What requirements do you capture for territory management?",
        "How do you handle forecasting requirements across product lines?",
        "When should leads remain unconverted versus auto-converted?",
        "How do you specify partner relationship management on Sales Cloud?",
        "What AC do you write for mobile sales rep offline scenarios?",
        "How do you document approval requirements for discounting?",
        "What is your approach to activity management requirements?",
        "How do you capture campaign influence requirements?",
        "How do you align Sales Cloud design with CPQ if introduced later?",
    ],
    "salesforce/service-cloud.md": [
        "How do you define case assignment and escalation rules in requirements?",
        "What omnichannel routing requirements do you capture for a contact center?",
        "How do you specify entitlement and SLA requirements?",
        "When should Knowledge be in scope versus external KB integration?",
        "How do you document case hierarchy and parent-child scenarios?",
        "What requirements apply to Service Console layout and macros?",
        "How do you capture requirements for Einstein Case Classification?",
        "What AC cover email-to-case and web-to-case error paths?",
        "How do you define service metrics and reporting requirements?",
        "How do you integrate Service Cloud with field service requirements?",
    ],
    "salesforce/experience-cloud.md": [
        "How do you decide between Experience Cloud and an external portal?",
        "What authentication requirements do you capture for partner communities?",
        "How do you document sharing set versus sharing rule requirements?",
        "What self-service capabilities belong in community versus core CRM?",
        "How do you specify branding and CMS requirements?",
        "What NFRs apply to community page load and mobile responsiveness?",
        "How do you handle PII display in community profiles?",
        "What moderation and content governance requirements apply?",
        "How do you test guest user access in acceptance criteria?",
        "How do you plan Experience Cloud releases with core org changes?",
    ],
    "salesforce/cpq.md": [
        "How do you document product catalog hierarchy requirements?",
        "What pricing rule complexity triggers architect review?",
        "How do you capture approval workflow requirements for quotes?",
        "When should CPQ be deferred to a phase two release?",
        "How do you specify bundle and constraint requirements?",
        "What integration points between CPQ and ERP must be in the BRD?",
        "How do you write AC for guided selling flows?",
        "What migration considerations apply to legacy quote data?",
        "How do you handle subscription versus asset-based quoting?",
        "What licensing and cost implications do you flag for CPQ scope?",
    ],
    "salesforce/industries.md": [
        "How do you map business capabilities to Industry Cloud features without feature shopping?",
        "What questions do you ask to determine FSC versus custom wealth management?",
        "How do you document regulatory controls for insurance policy administration?",
        "When should Vlocity/OmniStudio be in scope versus standard clouds?",
        "How do you handle industry-specific data models in fit-gap analysis?",
        "What stakeholder groups are unique to utilities implementations?",
        "How do you assess readiness for Health Cloud versus Service Cloud?",
        "What integration patterns are common in communications quote-to-activate?",
        "How do you document consent and privacy for regulated industries?",
        "How do you avoid over-customizing industry accelerators?",
    ],
    "delivery/architecture.md": [
        "How do you document integration patterns in a BRD for architect handoff?",
        "What NFR categories are mandatory for enterprise Salesforce programs?",
        "How do you capture data residency and encryption requirements?",
        "When do you recommend event-driven versus request-response integration?",
        "How do you document master data management decisions?",
        "What scalability requirements do you elicit for batch integrations?",
        "How do you specify error handling and reconciliation for integrations?",
        "What security requirements belong in BA documents versus security design?",
        "How do you assess whether middleware is required?",
        "How do you trace NFRs to test scenarios?",
    ],
    "delivery/agile.md": [
        "How do you maintain a BRD anchor while delivering in agile sprints?",
        "What artifacts does the BA produce each sprint on a Salesforce program?",
        "How do you handle changing priorities mid-sprint?",
        "When is SAFe appropriate versus pure Scrum for Salesforce?",
        "How do you manage documentation debt in agile delivery?",
        "What is your approach to release planning across multiple workstreams?",
        "How do you coordinate BA work with regression testing windows?",
        "How do you define ready for refinement criteria?",
        "What metrics do you track for backlog health?",
        "How do you integrate UAT cycles with sprint cadence?",
    ],
    "delivery/scrum.md": [
        "What is the BA role during sprint planning?",
        "How do you facilitate backlog refinement when stories are poorly written?",
        "What should be in the definition of ready for Salesforce stories?",
        "How do you handle spillover stories without losing traceability?",
        "What estimation inputs does the BA provide?",
        "How do you participate effectively in retrospectives as a BA?",
        "When should the BA attend daily standups?",
        "How do you manage dependencies between teams in scrum?",
        "What sprint artifacts does the BA own or contribute to?",
        "How do you protect the team from mid-sprint requirement churn?",
    ],
    "delivery/risk-management.md": [
        "How do you identify risks during discovery versus delivery?",
        "What belongs in a RAID log versus a risk register?",
        "How do you quantify and prioritize program risks?",
        "When do you escalate a risk to the steering committee?",
        "How do you document mitigation owners and due dates?",
        "What Salesforce-specific risks do you always flag early?",
        "How do you track assumption validation as risks?",
        "How do you communicate risk status without alarm fatigue?",
        "What governance gates tie to risk closure?",
        "How do you link risks to requirements and test coverage?",
    ],
    "delivery/communication.md": [
        "How do you tailor a status update for executives versus the delivery team?",
        "What is your approach to delivering scope reduction news?",
        "How do you facilitate a workshop when two executives disagree publicly?",
        "How do you confirm understanding without interrogating stakeholders?",
        "What visual formats do you use for complex process explanations?",
        "How do you manage written communication across time zones?",
        "How do you prepare for a steering committee presentation?",
        "What do you do when a stakeholder stops attending sessions?",
        "How do you document and circulate action items effectively?",
        "How do you handle language barriers in global programs?",
    ],
    "delivery/leadership.md": [
        "How do you mentor junior BAs on a large program?",
        "Describe a time you influenced a technical decision without authority.",
        "How do you build consensus when architects and business disagree?",
        "What is your approach to delegating workshop facilitation?",
        "How do you model consulting ethics under client pressure?",
        "How do you recover team morale after a failed release?",
        "When do you push back on a client sponsor?",
        "How do you develop BA capability across a multi-vendor team?",
        "What leadership behaviors do you demonstrate in crisis situations?",
        "How do you balance client satisfaction with sustainable delivery practices?",
    ],
    "advanced/scenario-questions.md": [
        "A bank wants RMs to see household relationships and complaints in one view. Outline your discovery plan.",
        "A retailer needs omnichannel returns across stores and ecommerce. What are your first three BRD themes?",
        "A utility must reduce call center volume during outages. How do you approach requirements?",
        "An insurer wants straight-through processing for simple claims. What constraints do you probe?",
        "A telecom B2B team quotes complex bundles manually. Where do you start fit-gap?",
        "A healthcare provider needs patient scheduling with compliance constraints. What workshops do you run?",
        "A manufacturer wants dealer portal ordering integrated to ERP. What integration requirements matter?",
        "A public sector agency needs case management with FOIA workflows. What governance applies?",
        "A global rollout must support 12 languages. What requirements do you capture early?",
        "A merger requires consolidating two Salesforce orgs. What is your BA approach?",
    ],
    "advanced/case-studies.md": [],
    "advanced/whiteboard-exercises.md": [],
    "advanced/behavioral.md": [
        "Tell me about a time you had to push back on a senior stakeholder's unrealistic deadline.",
        "Describe a situation where you uncovered a critical requirement others had missed.",
        "Give an example of resolving conflict between business and technical leads.",
        "Tell me about a failed workshop and what you changed afterward.",
        "Describe how you adapted when project scope doubled mid-program.",
        "Give an example of mentoring someone who struggled with user story quality.",
        "Tell me about a time you made a mistake in requirements and how you recovered.",
        "Describe a situation requiring ethical judgment on data use.",
        "Give an example of influencing adoption when users resisted change.",
        "Tell me about delivering bad news to an executive sponsor.",
    ],
    "advanced/executive-communication.md": [
        "How do you structure a 10-minute executive briefing on program status?",
        "What belongs in a business case for Salesforce investment?",
        "How do you present trade-offs between scope, time, and cost?",
        "How do you recommend a go/no-go decision before go-live?",
        "What metrics do executives care about during transformation?",
        "How do you handle an executive who wants daily detailed updates?",
        "How do you document steering committee decisions?",
        "What is your approach to benefits realization reporting?",
        "How do you communicate technical debt to non-technical sponsors?",
        "How do you prepare for board-level presentations on CRM programs?",
    ],
}

TOPIC_THEMES: dict[str, list[str]] = {
    "business-analysis.md": [
        "requirement traceability", "fit-gap classification", "MoSCoW prioritization",
        "stakeholder sign-off", "assumption management", "scope boundaries",
        "benefits realization", "change impact assessment", "vendor management",
        "quality gates", "documentation standards", "business case alignment",
    ],
    "requirement-gathering.md": [
        "probing questions", "active listening", "workshop design", "parking lot management",
        "consensus building", "silent stakeholders", "remote elicitation", "survey design",
        "prototype validation", "requirement conflicts", "implicit requirements",
    ],
    "current-state.md": [
        "process mining", "shadowing", "system inventory", "data quality assessment",
        "bottleneck analysis", "handoff points", "exception paths", "volume metrics",
        "cycle time", "error rates", "compliance gaps",
    ],
    "future-state.md": [
        "automation candidates", "standardization", "role changes", "KPI definition",
        "phased rollout", "quick wins", "dependency mapping", "change readiness",
        "training needs", "adoption metrics", "continuous improvement",
    ],
    "user-stories.md": [
        "persona definition", "story mapping", "vertical slicing", "spike stories",
        "technical debt stories", "enabler stories", "cross-team dependencies",
        "mobile stories", "bulk processing", "reporting stories",
    ],
    "acceptance-criteria.md": [
        "boundary values", "role-based testing", "regression scope", "performance AC",
        "accessibility", "audit trail", "localization", "concurrency",
    ],
    "stakeholders.md": [
        "sponsor engagement", "change champions", "union considerations",
        "vendor stakeholders", "regulatory bodies", "customer advisory",
    ],
    "salesforce/crm.md": [
        "validation rules", "page layouts", "lightning pages", "app builder",
        "flows", "reports and dashboards", "data import", "sandbox strategy",
    ],
    "salesforce/sales-cloud.md": [
        "lead scoring", "pipeline hygiene", "account hierarchy", "contact roles",
        "products and price books", "contracts", "orders",
    ],
    "salesforce/service-cloud.md": [
        "live chat", "messaging", "CTI integration", "surveys", "swarming",
        "field service handoff", "warranty management",
    ],
    "salesforce/experience-cloud.md": [
        "LWR versus Aura", "SEO requirements", "SSO", "MFA", "data categories",
        "audience targeting", "personalization",
    ],
    "salesforce/cpq.md": [
        "discount schedules", "contract amendments", "renewals", "usage-based pricing",
        "multi-currency", "tax integration",
    ],
    "salesforce/industries.md": [
        "Financial Services Cloud", "Health Cloud", "Vlocity", "Public Sector Solutions",
        "Net Zero Cloud", "loyalty management", "referral management",
    ],
    "delivery/architecture.md": [
        "API limits", "bulk API", "platform events", "Heroku", "MuleSoft",
        "identity management", "single sign-on", "high availability",
    ],
    "delivery/agile.md": [
        "PI planning", "feature toggles", "continuous delivery", "DevOps alignment",
        "regression strategy", "environments", "release trains",
    ],
    "delivery/scrum.md": [
        "velocity", "burndown", "impediments", "sprint goals", "team norms",
        "Scrum Master collaboration", "PO collaboration",
    ],
    "delivery/risk-management.md": [
        "issue versus risk", "contingency plans", "residual risk", "risk appetite",
        "cutover risk", "data migration risk", "adoption risk",
    ],
    "delivery/communication.md": [
        "status RAG", "escalation paths", "lessons learned", "knowledge transfer",
        "town halls", "FAQs", "release notes",
    ],
    "delivery/leadership.md": [
        "coaching", "feedback culture", "psychological safety", "diversity",
        "vendor leadership", "client relationship", "thought leadership",
    ],
    "advanced/scenario-questions.md": [
        "data migration crisis", "regulatory audit", "performance degradation",
        "security incident", "acquisition integration", "licensing overrun",
        "adoption failure", "integration outage", "scope explosion",
    ],
    "advanced/case-studies.md": [
        "retail loyalty transformation", "insurance claims modernization",
        "banking KYC remediation", "healthcare member engagement",
        "utilities smart meter rollout", "telecom billing dispute reduction",
    ],
    "advanced/whiteboard-exercises.md": [
        "lead-to-cash swimlane", "case escalation flow", "integration landscape",
        "capability heat map", "stakeholder power-interest grid", "entity relationship",
    ],
    "advanced/behavioral.md": [
        "ambiguity tolerance", "client empathy", "intellectual honesty",
        "continuous learning", "cross-cultural collaboration", "resilience",
    ],
    "advanced/executive-communication.md": [
        "portfolio prioritization", "investment governance", "value stream",
        "operating model", "transformation office", "OKR alignment",
    ],
}

INDUSTRIES = ["Banking", "Insurance", "Healthcare", "Retail", "Utilities", "Telecom", "Manufacturing", "Public Sector"]
WB_TYPES = ["Process mapping", "Capability mapping", "Data model", "Integration", "Solution architecture", "Stakeholder analysis"]


def rel(prefix: str, items: list[str]) -> str:
    prefix = prefix.rstrip("/") + "/"
    return ", ".join(f"[{Path(i).name}]({prefix}{i})" for i in items)


def yaml_header(meta: dict, rel_path: str) -> str:
    depth = rel_path.count("/")
    kb = "../" * (depth + 1) + "knowledge/"
    tpl = "../" * (depth + 1) + "templates/"
    pb = "../" * (depth + 1) + "playbooks/"
    sc = "../" * (depth + 1) + "scenarios/"
    brain = "../" * (depth + 1) + "brain/"
    return f"""---
title: {meta['title']}
module: Salesforce Business Analyst
category: Interview Guide
document-type: Interview Framework
version: 1.0.0
status: approved
owner: BA Practice Lead
last-reviewed: 2026-07-02
review-cycle: quarterly
difficulty: {meta['difficulty']}
industry: all
salesforce-cloud: {meta['clouds']}
related-brain-modules: [{', '.join(meta['brain'])}]
related-knowledge: [{', '.join(meta['knowledge'])}]
related-templates: [{', '.join(meta['templates'])}]
related-playbooks: [{', '.join(meta['playbooks'])}]
related-scenarios: [{', '.join(meta['scenarios'])}]
tags: [{', '.join(meta['tags'])}]
---

"""


def question_block(
    qnum: int,
    question: str,
    topic: str,
    difficulty: str,
    interview_type: str,
    meta: dict,
    depth: int,
) -> str:
    kb = "../" * (depth + 1) + "knowledge/"
    brain = "../" * (depth + 1) + "brain/"
    intent_map = {
        "Screening": "Baseline competency and role fit",
        "Technical": "Platform literacy and technical judgment",
        "Functional": "Business process and requirements depth",
        "Consulting": "Enterprise consulting mindset and structured thinking",
        "Leadership": "Influence, facilitation, and program leadership",
        "Executive": "Executive communication and strategic alignment",
    }
    return f"""### Q{qnum}

**Question**

{question}

**Interviewer Intent**

Assess {intent_map.get(interview_type, 'consulting competency')} at **{difficulty}** level for **{topic.replace('.md', '').replace('/', ' / ')}**. Evaluates structured reasoning, Salesforce awareness where relevant, and enterprise delivery experience.

**Expected Strong Answer**

The candidate explains their approach with clear reasoning, cites relevant practices (e.g., traceability, standard-before-custom, stakeholder validation), names risks and trade-offs, and references how they would document or validate the outcome. They connect business outcomes to Salesforce capabilities without jumping to implementation details prematurely. For senior levels, they describe real program context (anonymized) and governance touchpoints.

**Weak Answer**

Vague generalities ("I would talk to stakeholders"), feature-listing without business outcome, jumping to Apex or custom objects without justification, or claiming certainty without validation steps. No mention of assumptions, risks, or how success would be measured.

**Follow-up Questions**

1. What assumptions would you validate first, and with whom?
2. How would you document this in a BRD or workshop output?
3. What Salesforce standard capabilities would you explore before recommending custom build?
4. What risks would you add to the RAID log?
5. How would you know the requirement is testable and ready for refinement?

**Common Mistakes**

- Treating interview answers as purely theoretical with no delivery structure
- Over-indexing on Salesforce features instead of business capability
- Ignoring adoption, security, or integration implications
- Failing to mention traceability or sign-off paths

**Senior Consultant Tips**

Interviewers reward candidates who think in **outcomes, constraints, and validation loops**. Pause to structure the answer (context → approach → risks → next steps). Reference canonical repo artifacts—brain modules for reasoning, knowledge articles for depth, templates for outputs—rather than reinventing frameworks. At Principal level, connect the answer to portfolio governance and measurable value.

**Related Documents**

- Brain: {rel(brain, meta['brain'][:3])}
- Knowledge: {rel(kb, meta['knowledge'][:3])}

---
"""


def scenario_block(qnum: int, seed: str, meta: dict, depth: int, theme: str) -> str:
    industry = INDUSTRIES[qnum % len(INDUSTRIES)]
    return f"""### Q{qnum}

**Context**

A **{industry}** enterprise is mid-transformation on Salesforce. {seed} Additional constraint: {theme} must be addressed within the current program phase.

**Business Problem**

Legacy processes and fragmented systems prevent consistent customer experience. Leadership demands measurable improvement within two quarters while minimizing disruption to regulated operations.

**Constraints**

- Fixed license envelope and partial offshore delivery team
- Existing ERP remains system of record for financial transactions
- Security and compliance reviews required before production changes
- Competing priorities from {theme}

**Question**

Walk through your discovery approach, three initial business requirements, fit-gap themes, and how you would validate your recommendations with stakeholders.

**Evaluation Criteria**

| Criterion | Weight |
|-----------|--------|
| Structured discovery plan | 25% |
| Business-outcome-focused requirements | 25% |
| Platform-aware fit-gap thinking | 20% |
| Risk and assumption identification | 15% |
| Stakeholder validation approach | 15% |

**Expected Strong Answer**

Phased discovery plan (executives, operations, IT), workshop outputs tied to templates, requirements with IDs and success measures, fit-gap using standard-before-custom, RAID items for {theme}, and explicit validation/sign-off steps.

**Weak Answer**

Jumps to solution design, lists features, ignores compliance or integration constraints, no measurable outcomes or traceability.

**Follow-up Questions**

1. What would you defer to phase two and why?
2. Which steering committee decisions are needed?
3. How would you test assumptions about {theme}?
4. What adoption risks do you foresee?
5. Which playbook and template would you use first?

**Common Mistakes**

- Solutioning before understanding As-Is
- Missing non-functional and governance requirements
- No link between scenario and enterprise delivery artifacts

**Senior Consultant Tips**

Use the 13-stage reasoning framework aloud. Name the artifacts you would produce and the order you would socialise them.

**Related Documents**

- Playbooks: {rel('../' * (depth + 1) + 'playbooks/', meta['playbooks'][:2])}
- Scenarios: {rel('../' * (depth + 1) + 'scenarios/', meta['scenarios'][:2])}

---
"""


def case_study_block(qnum: int, theme: str, meta: dict, depth: int) -> str:
    industry = INDUSTRIES[qnum % len(INDUSTRIES)]
    sc_prefix = "../" * (depth + 1) + "scenarios/"
    sc_path = f"{sc_prefix}{meta['scenarios'][0]}" if meta['scenarios'] else f"{sc_prefix}README.md"
    return f"""### Case Study {qnum}

**Industry**

{industry}

**Business Context**

Enterprise program: **{theme}**. Multi-cloud Salesforce footprint with legacy integration debt and uneven process maturity across regions.

**Objectives**

- Improve customer/employee experience with measurable KPIs
- Reduce manual effort and error rates in core processes
- Establish governance for sustainable enhancement backlog

**Requirements (Themes)**

1. Standardize core process with regional configurability
2. Integrate with system of record without duplicating master data
3. Enable adoption through role-based experiences and training

**Deliverables**

Discovery readout, current/future state, BRD themes, fit-gap summary, prioritized backlog, RAID log.

**Expected Analysis**

Candidate produces structured current state hypotheses, pain point ranking, capability mapping, and phased roadmap. Identifies regulatory, data, and adoption risks.

**Suggested Solution Direction**

Standard-first Salesforce capabilities, declarative automation where possible, integration via established middleware, Experience Cloud only where self-service ROI is proven.

**Discussion Questions**

1. What workshops would you run in weeks 1–2?
2. Which requirements are Must-have for MVP?
3. How do you trace business goals to stories?
4. What would you escalate to architecture review?
5. How do you measure success 90 days post go-live?

**Evaluation Criteria**

Depth of structured analysis, business judgment, platform awareness, risk thinking, and communication clarity.

**Related Documents**

- [{theme}]({sc_path})
- Knowledge: {rel('../' * (depth + 1) + 'knowledge/', meta['knowledge'][:2])}

---
"""


def whiteboard_block(qnum: int, exercise_type: str, meta: dict, depth: int) -> str:
    return f"""### Exercise {qnum}

**Whiteboard Prompt**

**{exercise_type}** — Design a diagram for a Salesforce enterprise engagement covering {meta['title'].replace(' Interview Questions', '').replace(' Interview Exercises', '')}. Include actors, systems, key objects or capabilities, and integration touchpoints. Time box: 20 minutes draw + 10 minutes explain.

**Evaluation Criteria**

| Criterion | Indicators |
|-----------|------------|
| Completeness | Major actors, systems, flows not omitted |
| Clarity | Legible labels, consistent notation |
| Business alignment | Diagram reflects outcomes not just tech |
| Salesforce awareness | Standard objects/capabilities where appropriate |
| Communication | Candidate narrates trade-offs while drawing |

**Expected Strong Answer**

Clear legend, happy path plus exception path, explicit system-of-record labels, security or compliance callouts where relevant, and verbal explanation of assumptions.

**Weak Answer**

Feature sketch with no process narrative, missing integrations, or inability to explain diagram choices.

**Follow-up Questions**

1. Where are the highest-risk handoffs?
2. What would you validate in workshop?
3. Which part would you prototype first?
4. What NFRs does this diagram imply?
5. How would you maintain this artifact?

**Senior Consultant Tips**

Talk while drawing. State assumptions. Leave space for feedback. Reference [process-mapping.md](../{'../' * depth}knowledge/process-mapping.md) notation.

**Related Documents**

- Templates: {rel('../' * (depth + 1) + 'templates/', meta['templates'][:2])}

---
"""


def ai_coaching_section(meta: dict, depth: int) -> str:
  kb = "../" * (depth + 1) + "knowledge/README.md"
  return f"""## AI Coaching Guidance

When conducting mock interviews from this topic:

1. **Open** with difficulty and interview type (Screening through Executive).
2. **Ask** one question at a time; wait for full response before follow-ups.
3. **Evaluate** against Expected Strong Answer criteria—not keyword matching.
4. **Probe** with 2–3 follow-up questions from the question block.
5. **Feedback** using: Strengths → Gaps → Senior Consultant Tips → Related study links.
6. **Adapt** difficulty up if candidate excels; down if struggling—offer hints from knowledge articles.
7. **Recommend** review: brain modules for reasoning, [{meta['knowledge'][0]}](../{'../' * depth}knowledge/{meta['knowledge'][0]}) for depth, playbooks for methodology.
8. **Never** invent Salesforce features—validate against knowledge base and flag TBC items.

"""


def footer_sections(meta: dict, rel_path: str, prev_link: str, next_link: str) -> str:
    depth = rel_path.count("/")
    p = "../" * (depth + 1)
    return f"""## Related Brain Modules

{chr(10).join(f'- [{b}]({p}brain/{b})' for b in meta['brain'])}

## Related Knowledge

{chr(10).join(f'- [{k}]({p}knowledge/{k})' for k in meta['knowledge'])}

## Related Templates

{chr(10).join(f'- [{t}]({p}templates/{t})' for t in meta['templates'])}

## Related Playbooks

{chr(10).join(f'- [{pb}]({p}playbooks/{pb})' for pb in meta['playbooks'])}

## Related Industry Scenarios

{chr(10).join(f'- [{s}]({p}scenarios/{s})' for s in meta['scenarios'])}

## Related Interview Topics

- [interview-index.md]({'../' * depth}interview-index.md)

## Related Examples

- [examples/sample-project/README.md](../../examples/sample-project/README.md)

## Related Documents

- [skill.md]({p}skill.md)
- [checklists.md]({p}checklists.md)

## Navigation

- **Previous:** {prev_link}
- **Next:** {next_link}
- **See Also:** [interview-index.md]({'../' * depth}interview-index.md) | [README.md]({'../' * depth}README.md)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-07-02 | Sprint 6 Enterprise Interview Intelligence Framework |
"""


def generate_questions(rel_path: str, count: int, meta: dict) -> str:
    depth = rel_path.count("/")
    seeds = list(SEED_QUESTIONS.get(rel_path, []))
    themes = TOPIC_THEMES.get(rel_path, ["enterprise delivery"])
    blocks: list[str] = []
    topic_label = rel_path.replace(".md", "").replace("/", " — ")

    for i in range(1, count + 1):
        diff = DIFFICULTIES[(i - 1) % len(DIFFICULTIES)]
        itype = INTERVIEW_TYPES[(i - 1) % len(INTERVIEW_TYPES)]
        theme = themes[(i - 1) % len(themes)]

        if rel_path == "advanced/scenario-questions.md":
            seed = seeds[(i - 1) % len(seeds)] if seeds else f"Scenario variant {i} involving {theme}."
            blocks.append(scenario_block(i, seed, meta, depth, theme))
        elif rel_path == "advanced/case-studies.md":
            blocks.append(case_study_block(i, theme, meta, depth))
        elif rel_path == "advanced/whiteboard-exercises.md":
            ex_type = WB_TYPES[(i - 1) % len(WB_TYPES)]
            blocks.append(whiteboard_block(i, ex_type, meta, depth))
        else:
            if i <= len(seeds):
                q = seeds[i - 1]
            else:
                q = (
                    f"How do you apply {theme} in a Salesforce BA engagement "
                    f"({diff} / {itype} perspective)?"
                )
            blocks.append(question_block(i, q, topic_label, diff, itype, meta, depth))

    return "\n".join(blocks)


def generate_topic_file(rel_path: str, prev_link: str, next_link: str) -> None:
    meta = TOPIC_META[rel_path]
    count = QUESTION_COUNTS[rel_path]
    depth = rel_path.count("/")
    out_path = IG / rel_path
    out_path.parent.mkdir(parents=True, exist_ok=True)

    type_matrix = "| Type | Use when |\n|------|----------|\n" + "\n".join(
        f"| {t} | Assessing {t.lower()} depth |" for t in INTERVIEW_TYPES
    )

    body = f"""# {meta['title']}

## Overview

{meta['overview']}

**Question count:** {count}

## Difficulty and Interview Types

| Level | Description |
|-------|-------------|
| Beginner | Foundational concepts and terminology |
| Intermediate | Applied delivery experience |
| Senior | Complex programs and trade-off judgment |
| Lead | Multi-workstream leadership |
| Principal | Portfolio and executive alignment |

{type_matrix}

## Question Bank

{generate_questions(rel_path, count, meta)}

{ai_coaching_section(meta, depth)}
{footer_sections(meta, rel_path, prev_link, next_link)}
"""
    out_path.write_text(yaml_header(meta, rel_path) + body, encoding="utf-8")
    print(f"  wrote {rel_path} ({count} items)")


def generate_readme(total: int) -> None:
    content = f"""---
title: Enterprise Interview Intelligence Framework
module: Salesforce Business Analyst
category: Interview Guide
document-type: Interview Framework
version: 1.0.0
status: approved
owner: BA Practice Lead
last-reviewed: 2026-07-02
review-cycle: quarterly
difficulty: all
industry: all
salesforce-cloud: Platform
tags: [interview, hiring, coaching, assessment]
---

# Enterprise Interview Intelligence Framework

Sprint 6 delivers **{total}** structured interview items for Salesforce Business Analyst and enterprise consulting roles.

## Purpose

- Candidate preparation for screening through executive rounds
- Interview panel guidance with competency-based assessment
- AI-assisted mock interviews and coaching
- Scenario, case study, and whiteboard facilitation

## Legacy Content

Stakeholder interview structure and hiring scorecards from the original `interview-guide.md` are preserved in:

- [stakeholders.md](stakeholders.md) — stakeholder engagement questions
- [business-analysis.md](business-analysis.md) — senior BA hiring signals
- [advanced/scenario-questions.md](advanced/scenario-questions.md) — scenario exercises
- [advanced/behavioral.md](advanced/behavioral.md) — behavioral assessment

## Structure

| Area | Files | Focus |
|------|-------|-------|
| Core BA | 7 topic files | Analysis, elicitation, states, stories, AC, stakeholders |
| Salesforce | [salesforce/](salesforce/) | CRM, clouds, CPQ, industries |
| Delivery | [delivery/](delivery/) | Architecture, agile, scrum, risk, communication, leadership |
| Advanced | [advanced/](advanced/) | Scenarios, cases, whiteboard, behavioral, executive |

## How to Use

1. Start at [interview-index.md](interview-index.md) for the full catalog.
2. Load topic file matching the interview round.
3. Cross-reference brain, knowledge, templates, playbooks, and scenarios—do not duplicate canonical content.
4. For AI coaching, follow **AI Coaching Guidance** in each topic file.

## Related Documents

- [skill.md](../skill.md)
- [interview-guide.md](../interview-guide.md) (redirect stub)
- [brain/README.md](../brain/README.md)
- [knowledge/README.md](../knowledge/README.md)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-07-02 | Sprint 6 — full interview intelligence framework |
"""
    (IG / "README.md").write_text(content, encoding="utf-8")
    print("  wrote README.md")


def generate_index() -> None:
    rows = []
    total = 0
    for rel_path, count in QUESTION_COUNTS.items():
        total += count
        link = rel_path
        title = TOPIC_META[rel_path]["title"]
        rows.append(f"| [{title}]({link}) | {count} | {TOPIC_META[rel_path]['difficulty']} |")

    table = "\n".join(rows)
    content = f"""---
title: Interview Index
module: Salesforce Business Analyst
category: Interview Guide
document-type: Interview Framework
version: 1.0.0
status: approved
owner: BA Practice Lead
last-reviewed: 2026-07-02
review-cycle: quarterly
tags: [index, interview, catalog]
---

# Interview Index

Master catalog for the Enterprise Interview Intelligence Framework.

**Total items:** {total}

## Category Catalog

| Topic | Count | Typical Difficulty |
|-------|------:|-------------------|
{table}

## Loading Guide for Agents

| Interview round | Load |
|-----------------|------|
| Screening | business-analysis.md, requirement-gathering.md |
| Technical / Functional | salesforce/*.md, user-stories.md, acceptance-criteria.md |
| Consulting | advanced/scenario-questions.md, current-state.md, future-state.md |
| Leadership | delivery/leadership.md, delivery/communication.md |
| Executive | advanced/executive-communication.md, stakeholders.md |
| Mock interview (full) | This index + topic file + related knowledge articles |

## Difficulty Legend

- **Beginner** — Terminology and fundamentals
- **Intermediate** — Hands-on delivery
- **Senior** — Trade-offs and enterprise complexity
- **Lead** — Multi-team programs
- **Principal** — Portfolio and executive stewardship

## Related Documents

- [README.md](README.md)
- [skill.md](../skill.md)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-07-02 | Sprint 6 interview index |
"""
    (IG / "interview-index.md").write_text(content, encoding="utf-8")
    print(f"  wrote interview-index.md (total={total})")


def main() -> None:
    IG.mkdir(parents=True, exist_ok=True)
    order = list(QUESTION_COUNTS.keys())
    print("Generating Sprint 6 interview guide...")
    for i, rel_path in enumerate(order):
        prev_link = f"[{TOPIC_META[order[i - 1]]['title']}]({order[i - 1]})" if i > 0 else "[README.md](README.md)"
        next_link = (
            f"[{TOPIC_META[order[i + 1]]['title']}]({order[i + 1]})" if i < len(order) - 1 else "[README.md](README.md)"
        )
        generate_topic_file(rel_path, prev_link, next_link)
    total = sum(QUESTION_COUNTS.values())
    generate_readme(total)
    generate_index()
    print(f"Done. {len(order)} topic files, {total} items.")


if __name__ == "__main__":
    main()
