---
title: Service Cloud Complaint Management - Sample User Story
module: Salesforce Business Analyst
category: Example
document_type: Example
type: user-story
version: 1.0.0
status: approved
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
project: SAMPLE-SC-001
epic: EP-SC-COMPLAINT
salesforce_cloud: Service Cloud
related_brain_modules: [salesforce-business-analyst/brain/output-framework.md, salesforce-business-analyst/brain/anti-hallucination.md]
related_knowledge: [salesforce-business-analyst/knowledge/service-cloud-patterns.md, salesforce-business-analyst/knowledge/ado-backlog-integration.md]
related_templates: [salesforce-business-analyst/templates/user-story-template.md]
related_playbooks: [salesforce-business-analyst/playbooks/story-refinement-playbook.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/salesforce/service-cloud.md]
related_examples: [examples/sample-user-story/dealer-portal-stories.md]
related_documents: [salesforce-business-analyst/skill.md]
keywords: [service cloud, complaint, case, user story, sample]
tags: [service-cloud, case, complaint, email-notification, dashboard, sample]
---

# User Story: Complaint Management

## Epic Statement

**Outcome:** Agents can record, track, and resolve customer complaints in Service Cloud, providing customers with confirmation and managers with operational visibility.

**Requirement refs:** BR-001, BR-002, BR-003

---

### US-SC-001: Complaint Management - Record Customer Complaints in Service Cloud

**As a** Customer Service Agent,
**I want** to record customer complaints received by phone in Salesforce Service Cloud,
**So that** complaints are tracked, customers receive confirmation, and managers can monitor resolution progress.

**Requirement refs:** BR-001, FR-001, FR-002, FR-003

**Priority:** Must

**Description:**

- **Current process (AS-IS):** Agents handle complaints by phone with no standardized Salesforce record. Complaints are tracked in spreadsheets or email threads. Managers have no consolidated view.
- **Future process (TO-BE):** Agent creates a Case record (Complaint record type) during or after the call with required details. System applies defaults (Status = New, Priority = Medium), sends confirmation email when possible, and exposes data to a manager dashboard.
- **Functional expectations:** Required field validation; complaints are searchable; dashboard refreshes on standard schedule.
- **Salesforce approach:** Use standard **Case** object with Complaint record type. No custom objects needed. Defaults via Record-Triggered Flow. Email via Email Alert + Template.

**Business Rules:**

- BR1: On complaint creation, Status defaults to **New**.
- BR2: On complaint creation, Priority defaults to **Medium**.
- BR3: Customer Name, Contact Number, Complaint Category, and Complaint Description are required.
- BR4: Confirmation email sends only when a valid customer email address is available.
- BR5: Agents may update Status and Priority after creation; managers have read access to all complaints in their hierarchy.

**Acceptance Criteria:**

- **AC1 — Happy path: create complaint:**
  - **Given** a Customer Service Agent is logged into Service Cloud
  - **And** the agent has permission to create Cases
  - **When** the agent creates a complaint with Customer Name, Contact Number, Complaint Category, and Complaint Description
  - **Then** a Case record is saved successfully
  - **And** Status is set to "New"
  - **And** Priority is set to "Medium"
- **AC2 — Validation: missing required field:**
  - **Given** a Customer Service Agent is creating a complaint
  - **When** any required field (Customer Name, Contact Number, Complaint Category, Complaint Description) is missing
  - **Then** the complaint cannot be saved
  - **And** the agent sees a clear validation message identifying the missing field(s)
- **AC3 — Confirmation email sent:**
  - **Given** a complaint is created successfully
  - **And** the related Contact has a valid email address
  - **When** the Case is saved
  - **Then** a confirmation email is sent to the customer
  - **And** the email includes the Case number and complaint summary
- **AC4 — Email skipped when no address:**
  - **Given** a complaint is created successfully
  - **And** the related Contact has no email address
  - **When** the Case is saved
  - **Then** no confirmation email is sent
  - **And** the agent is informed that email was not sent due to missing email address
- **AC5 — Manager dashboard visibility:**
  - **Given** a Service Manager is logged into Salesforce
  - **When** the manager opens the Complaints dashboard
  - **Then** open complaints are displayed with Status, Priority, and Complaint Category
  - **And** the manager can filter by date range and priority
- **AC6 — Permission: agent cannot delete:**
  - **Given** a Customer Service Agent views an existing complaint
  - **When** the agent attempts to delete the complaint
  - **Then** the delete action is not available or is denied

**Field Requirements:**

| Field Name | Required | Type | Validation |
|------------|----------|------|------------|
| Customer Name | Yes | Lookup (Contact) or Text | Must not be blank |
| Contact Number | Yes | Phone | Valid phone format |
| Complaint Category | Yes | Picklist | Active value only |
| Complaint Description | Yes | Long Text Area | Min 10 characters |
| Priority | Yes (default Medium) | Picklist | Default: Medium |
| Status | Yes (default New) | Picklist | Default: New |

**Objects Impacted:**

| Object | Action |
|--------|--------|
| Case | Create, Update, Read |
| Contact | Read, Update (optional link/create) |
| Account | Read |
| Email Template | Create |
| Report / Dashboard | Create, Read |

**Security and Permissions:**

| Persona | Create | Read | Update | Delete |
|---------|--------|------|--------|--------|
| Customer Service Agent | Yes | Own/Team | Yes | No |
| Service Manager | No | Yes (team/org) | Yes | No |
| System Administrator | Yes | Yes | Yes | Yes |

**Estimation (BA Input — Team to Confirm at Refinement):**

**T-shirt size:** M (Medium)

**Story points:** Not finalized — delivery team to assign during backlog refinement / planning poker.

**Note:** Story points are a relative measure of complexity, effort, and uncertainty — not hours, days, or months.

| Estimation input | Assessment |
|------------------|------------|
| Solution approach | Config (declarative: fields, layout, Flow, reports) |
| Complexity | Medium |
| Uncertainty / risk | Picklist values TBC with Service Ops; email deliverability depends on Org-Wide Email |
| Dependencies | Contact/Account data quality; Org-Wide Email Address configured |
| Splittability | Can split: complaint creation vs email notification vs dashboard |

**Deliverables Expected (Implementation Team):**

- [ ] Data model: Case record type (Complaint), custom fields (Complaint Category picklist), page layout
- [ ] Page layout / UX: Service Console layout for agent intake
- [ ] Automation: Record-Triggered Flow for Status/Priority defaults + Email Alert
- [ ] Email template: Complaint confirmation template (approved by business)
- [ ] Reports / dashboards: Complaints by Status, Priority, Category; Manager dashboard
- [ ] Security: Permission set for Agent (create/read/update Case), Manager (read all)
- [ ] Sandbox test evidence against AC; release notes

**Definition of Done:**

- [ ] All acceptance criteria (AC1–AC6) validated in target sandbox
- [ ] Implementation deliverables deployed and tested
- [ ] Security review for new fields/objects/permissions
- [ ] Email template approved by business stakeholder
- [ ] Test scenarios linked where applicable
- [ ] Release notes drafted
- [ ] Story points assigned by delivery team at refinement (if not already done)

**Dependencies:**

- Upstream: Contact/Account data quality; Org-Wide Email Address configuration
- Downstream: Future escalation/routing stories; reporting enhancements
- Integration: None in this story

**Assumptions:**

- A1: Complaints are modeled as **Case** records with a Complaint record type
- A2: Customer Name maps to Contact lookup; agent can create/link Contact during intake
- A3: Contact Number validation format to be confirmed by business
- A4: Complaint Category is a controlled picklist; values confirmed by Service Operations
- A5: Confirmation email requires valid email on Contact; if missing, complaint saves but email skips
- A6: Agents have Service Cloud licenses and Case Create permission
- A7: Manager dashboard uses native Salesforce Reports/Dashboards

**Out of Scope:**

- Customer self-service complaint submission (portal)
- SLA / Entitlement automation
- Omni-Channel routing
- SMS notifications
- ERP or external system integration

---

*This example was created from Task-9 lessons learned to provide a reference pattern for Service Cloud user stories.*

## Related Brain Modules

- [Output Framework](../../salesforce-business-analyst/brain/output-framework.md)
- [Anti-Hallucination](../../salesforce-business-analyst/brain/anti-hallucination.md)

## Related Knowledge

- [Service Cloud Patterns](../../salesforce-business-analyst/knowledge/service-cloud-patterns.md)
- [ADO Backlog Integration](../../salesforce-business-analyst/knowledge/ado-backlog-integration.md)

## Related Templates

- [User Story Template](../../salesforce-business-analyst/templates/user-story-template.md)

## Related Playbooks

- [Story Refinement Playbook](../../salesforce-business-analyst/playbooks/story-refinement-playbook.md)

## Related Industry Scenarios

- [Readme](../../salesforce-business-analyst/scenarios/README.md)

## Related Interview Topics

- [Service Cloud](../../salesforce-business-analyst/interview-guide/salesforce/service-cloud.md)

## Related Examples

- [Dealer Portal Stories](dealer-portal-stories.md)

## Related Documents

- [Skill](../../salesforce-business-analyst/skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-02 | BA Practice Lead | Initial Service Cloud complaint sample story (from Task-9 gap analysis) |
