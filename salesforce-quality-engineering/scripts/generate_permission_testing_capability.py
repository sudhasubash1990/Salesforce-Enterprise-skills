"""Generate Permission Testing Agent skill pack."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = ROOT / "skills" / "permission-testing-agent"
VERSION = "0.17.0"
DATE = "2026-07-27"

OUTPUT_SECTIONS = [
    "Executive Summary",
    "Security Context",
    "Business Requirement",
    "Security Components Impacted",
    "CRUD Validation Matrix",
    "Field Level Security Validation",
    "Record Access Validation",
    "Sharing Validation",
    "Profile Validation",
    "Permission Set Validation",
    "Permission Set Group Validation",
    "API Security Validation",
    "Experience Cloud Validation",
    "Negative Test Scenarios",
    "Regression Scope",
    "Automation Candidates",
    "Recommended SOQL Validation",
    "Deployment Risks",
    "Security Recommendations",
]


def fm(title: str, category: str, doc_type: str, tags: list[str]) -> str:
    return f"""---
title: {title}
module: Salesforce Quality Engineering
category: {category}
document_type: {doc_type}
version: {VERSION}
review_status: Draft
owner: QE Practice Lead
created_date: {DATE}
last_updated: {DATE}
review_cycle: quarterly
tags: [{", ".join(tags)}]
---

"""


def write(rel: str, content: str) -> None:
    path = CAP / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {rel}")


def knowledge_article(title, slug, purpose, reasoning, cross_links, rules):
    links = "\n".join(f"- [{n}]({p})" for n, p in cross_links)
    return fm(title, "QE Specialized Skill Knowledge", "Knowledge Article", ["permission-testing", "knowledge"]) + f"""# {title}

## Purpose

{purpose}

## Reasoning Model

{chr(10).join(f"{i}. {r}" for i, r in enumerate(reasoning, 1))}

## Decision Rules

{chr(10).join(f"- {r}" for r in rules)}

## Cross-Links (Canonical Depth)

{links}

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial capability knowledge |
"""


def playbook(title, slug, objective, inputs, workflow, decisions, deliverables, expected, escalation, pointer=""):
    ptr = f"\n\n**Pointer:** {pointer}" if pointer else ""
    b = lambda xs: "\n".join(f"- {x}" for x in xs)
    return fm(title, "QE Specialized Skill Playbook", "Playbook", ["permission-testing", "playbook"]) + f"""# {title}

## Objective

{objective}{ptr}

## Inputs

{b(inputs)}

## Validation Workflow

{b(workflow)}

## Decision Points

{b(decisions)}

## Deliverables

{b(deliverables)}

## Expected Results

{b(expected)}

## Escalation Rules

{b(escalation)}
"""


def template_doc(title, sections):
    body = "\n\n".join(f"## {s}\n\n_Complete during validation._" for s in sections)
    return fm(title, "QE Specialized Skill Template", "Template", ["permission-testing", "template"]) + f"""# {title}

{body}

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial template |
"""


def prompt_doc(title, prompt, sections):
    return fm(title, "QE Specialized Skill Prompt", "Prompt", ["permission-testing", "prompt"]) + f"""# {title}

## Prompt

```
{prompt}
```

## Required Output Sections

{chr(10).join(f"{i}. {s}" for i, s in enumerate(sections, 1))}

## Quality Gate

- Security Context and Business Requirement BEFORE test scenarios.
- CRUD, FLS, Sharing, and Record Access sections required.
- Delegate SOQL expansion to SOQL Validation Assistant when needed.
"""


def example_doc(title, scenario, requirement, strategy, expected, negative, soql, qa):
    return fm(title, "QE Specialized Skill Example", "Example", ["permission-testing", "example"]) + f"""# {title}

## Business Scenario

{scenario}

## Security Requirement

{requirement}

## Validation Strategy

{strategy}

## Expected Result

{expected}

## Negative Validation

{negative}

## Recommended SOQL

```sql
{soql}
```

## QA Recommendations

{qa}
"""


def main() -> None:
    print("Generating Permission Testing Agent skill pack...")
    CAP.mkdir(parents=True, exist_ok=True)

    write(
        "skill-config.yaml",
        f"""name: permission-testing-agent
short_id: PTA
version: {VERSION}
parent_module: salesforce-quality-engineering
entry: SKILL.md

routing:
  keywords:
    - permission
    - permissions
    - profile
    - permission set
    - permission set group
    - CRUD
    - FLS
    - field level security
    - record access
    - sharing
    - OWD
    - organization wide default
    - role hierarchy
    - manual sharing
    - experience cloud
    - community user
    - guest user
    - security testing
    - access control
    - login
    - session
    - MFA
    - API access
    - restriction rule
    - scoping rule
    - user visibility
    - deployment security
    - segregation of duties
    - least privilege
  primary_support:
    - knowledge/security/
    - knowledge/sharing-security-testing.md
    - knowledge/permission-set-testing.md
  upstream_skills:
    - skills/metadata-impact-analyzer
  downstream_capabilities:
    - skills/soql-validation-assistant
  downstream_after_analysis:
    - knowledge/test-design-engine.md

output_schema:
  sections:
{chr(10).join(f'    - id: {s.lower().replace(" ", "_")}' + chr(10) + f'      title: "{s}"' for s in OUTPUT_SECTIONS)}

quality_gates:
  - security_context_before_scenarios
  - crud_fls_sharing_sections_required
  - negative_scenarios_required
  - soql_delegated_to_sova_when_expanded

escalation:
  - signal: guest_user_or_experience_cloud
    to: Security Architect
  - signal: view_all_modify_all
    to: Security Architect + Release Manager
  - signal: production_profile_change
    to: Release Manager
""",
    )

    knowledge_specs = [
        ("Salesforce Security Architecture", "salesforce-security-architecture.md",
         "Map business process to layered security model before test design.",
         ["Identify personas and channels (UI, API, community).", "Layer CRUD → FLS → sharing → record access.", "Note automation running system vs user mode.", "Cross-link impacted metadata from MIA if present."],
         [("Security Knowledge", "../../knowledge/security/README.md"), ("Security Model BA", "../../../salesforce-business-analyst/knowledge/security-model.md")],
         ["Never skip sharing when OWD is Private.", "Community/guest paths are separate validation packs."]),
        ("CRUD", "crud.md", "Validate object-level Create/Read/Update/Delete per persona.",
         ["Build CRUD matrix: persona × object × action.", "Test UI and API channels separately if both in scope.", "Note tab visibility vs object CRUD distinction."],
         [("Object Level Security", "../../knowledge/security/object-level-security.md")],
         ["Missing Create but tab visible → document UX vs security gap.", "Integration user CRUD ≠ business user CRUD."]),
        ("Field Level Security", "field-level-security.md", "Validate readable/editable/hidden fields per persona.",
         ["Map sensitive fields explicitly.", "Test read-only vs hidden vs editable.", "Validate related list field exposure."],
         [("FLS Knowledge", "../../knowledge/security/field-level-security.md"), ("Permission Set Testing", "../../knowledge/permission-set-testing.md")],
         ["Hidden field must not appear in UI or API response for persona.", "Formula roll-up read-only exceptions documented."]),
        ("Role Hierarchy", "role-hierarchy.md", "Validate role-based record access inheritance.",
         ["Map role tree and record ownership.", "Test manager visibility to subordinate records.", "Note role + sharing rule interaction."],
         [("Role Hierarchy", "../../knowledge/security/role-hierarchy.md")],
         ["Role change deploy → regression on ownership-based reports."]),
        ("Organization Wide Defaults", "organization-wide-defaults.md", "Validate OWD impact on baseline access.",
         ["Document OWD per object (Private, Public Read Only, etc.).", "Predict sharing rule necessity from OWD.", "Test default vs shared access."],
         [("OWD", "../../knowledge/security/organization-wide-defaults.md"), ("Sharing Security Testing", "../../knowledge/sharing-security-testing.md")],
         ["OWD tightening → integration service account review required."]),
        ("Sharing Rules", "sharing-rules.md", "Validate criteria-based and owner-based sharing extensions.",
         ["Identify rules added/changed/deleted.", "Test included/excluded record populations.", "Validate rule criteria vs business intent."],
         [("Sharing Rules", "../../knowledge/security/sharing-rules.md")],
         ["Sharing rule + restriction rule — test combined effect."]),
        ("Permission Sets", "permission-sets.md", "Validate additive permissions and muting sets.",
         ["List permission sets and groups per persona.", "Identify View All/Modify All/Author Apex.", "Validate assignment scope (user vs group)."],
         [("Permission Sets", "../../knowledge/security/permission-sets.md")],
         ["Prefer perm set delta over profile rewrite for testing focus."]),
        ("Permission Set Groups", "permission-set-groups.md", "Validate PSG composition and muting.",
         ["Map PSG → constituent perm sets.", "Apply muting permission set rules.", "Verify effective permissions after group assignment."],
         [("Permission Set Groups", "../../knowledge/security/permission-set-groups.md")],
         ["PSG change affects all members — high blast radius."]),
        ("Restriction Rules", "restriction-rules.md", "Validate record filtering for visibility reduction.",
         ["Document criteria excluding records from view.", "Test records that should disappear vs remain.", "Combine with sharing rules in test plan."],
         [("Restriction Rules", "../../knowledge/security/restriction-rules.md")],
         ["Restriction rule deploy without comms → false defect reports."]),
        ("Scoping Rules", "scoping-rules.md", "Validate enterprise territory/ scoping visibility patterns.",
         ["Identify scoped objects and personas.", "Test in-scope vs out-of-scope records.", "Document enterprise edition dependencies."],
         [("Security Knowledge", "../../knowledge/security/README.md")],
         ["Scoping not licensed → mark Partial."]),
        ("Apex Security", "apex-security.md", "Validate Apex sharing mode and elevated access risks.",
         ["Identify without sharing / inherited sharing classes.", "Map run-as and elevated DML.", "Test data created by automation visibility."],
         [("Sharing Security Testing", "../../knowledge/sharing-security-testing.md")],
         ["without sharing class → explicit sharing validation required."]),
        ("WITH SECURITY_ENFORCED", "with-security-enforced.md", "Advise SOQL/Apex user-mode enforcement for validation.",
         ["Recommend WITH SECURITY_ENFORCED in validation SOQL where applicable.", "Contrast system mode query results vs user mode.", "Delegate query text to SOVA."],
         [("SOQL Validation Assistant", "../soql-validation-assistant/SKILL.md")],
         ["System mode SOQL in validation must be labeled — not default for business proof."]),
        ("User Mode vs System Mode", "user-mode-vs-system-mode.md", "Choose validation channel matching real user experience.",
         ["UI and user-mode API reflect true access.", "System mode for admin/investigation only — document separately.", "Flow/Apex context determines mode."],
         [("Apex Security", "apex-security.md")],
         ["Never sign off community access using system admin verification only."]),
        ("Sharing Keywords", "sharing-keywords.md", "Interpret with sharing, without sharing, inherited sharing for test scope.",
         ["Map keyword to class/trigger visibility behavior.", "Design tests for records created by each keyword path.", "Identify false positives in automation tests."],
         [("Apex Security", "apex-security.md")],
         ["inherited sharing — default for most triggers; still validate owner."]),
        ("Experience Cloud Security", "experience-cloud-security.md", "Validate partner/customer/guest community access separately.",
         ["Separate profiles/perm sets for external users.", "Guest user — minimal CRUD, high risk.", "Test sharing sets and super user access if used."],
         [("Sharing Security Testing", "../../knowledge/sharing-security-testing.md")],
         ["Guest profile change → Critical deployment risk."]),
        ("Shield Platform Encryption", "shield-platform-encryption.md", "Note encryption impact on validation and field access.",
         ["Encrypted fields — FLS still applies; search/filter limitations.", "Mark compliance fields for Legal review.", "Do not claim encryption compliance without evidence."],
         [("Security Knowledge", "../../knowledge/security/README.md")],
         ["Encryption + integration — confirm middleware field access."]),
        ("Session Security", "session-security.md", "Validate session policies affecting test execution.",
         ["Login hours, session timeout, IP restrictions.", "Test blocked vs allowed sessions.", "Document MFA interaction."],
         [("Session Policies", "../../knowledge/security/session-policies.md")],
         ["IP restriction blocks automation user — separate service account."]),
        ("MFA", "mfa.md", "Validate MFA requirements for privileged personas.",
         ["Identify MFA-required profiles/perm sets.", "Document test user bypass only in non-prod.", "Never disable MFA in prod for testing."],
         [("MFA", "../../knowledge/security/mfa.md")],
         ["Admin MFA bypass in sandbox — label assumption."]),
        ("Login Security", "login-security.md", "Validate login policies and lockout behavior.",
         ["Login IP ranges, trusted IPs, password policies.", "Negative: blocked login paths.", "Integration OAuth separate from user login."],
         [("Login Policies", "../../knowledge/security/login-policies.md")],
         ["Lockout during UAT — coordinate test data users."]),
        ("Connected Apps", "connected-apps.md", "Validate OAuth connected app scope and user access.",
         ["Map profiles/perm sets authorized for app.", "Validate scope vs least privilege.", "Test token and refresh flows at QA design level."],
         [("Integration Knowledge", "../../knowledge/integration/README.md")],
         ["Connected app scope expansion → API Security regression In."]),
        ("API Security", "api-security.md", "Validate REST/Bulk API access per integration persona.",
         ["CRUD/FLS enforced for API user.", "Compare API vs UI visibility.", "Named credential identity separate matrix."],
         [("API Security", "../../knowledge/integration/README.md"), ("SOQL Validation", "../soql-validation-assistant/SKILL.md")],
         ["API user with Modify All — flag excessive privilege."]),
    ]
    for spec in knowledge_specs:
        write(f"knowledge/{spec[1]}", knowledge_article(*spec))

    write("knowledge/README.md", fm("Permission Testing — Knowledge", "QE Specialized Skill Knowledge", "Guide", ["permission-testing"]) + """# Permission Testing — Knowledge

Canonical security encyclopedia: [`../../knowledge/security/`](../../knowledge/security/README.md). These articles provide **reasoning models** for permission testing.

| Document | Focus |
|----------|-------|
| [Salesforce Security Architecture](salesforce-security-architecture.md) | Layered model |
| [CRUD](crud.md) | Object permissions |
| [Field Level Security](field-level-security.md) | FLS |
| [Role Hierarchy](role-hierarchy.md) | Roles |
| [Organization Wide Defaults](organization-wide-defaults.md) | OWD |
| [Sharing Rules](sharing-rules.md) | Sharing |
| [Permission Sets](permission-sets.md) | Perm sets |
| [Permission Set Groups](permission-set-groups.md) | PSG |
| [Restriction Rules](restriction-rules.md) | Restriction |
| [Scoping Rules](scoping-rules.md) | Scoping |
| [Apex Security](apex-security.md) | Apex sharing |
| [WITH SECURITY_ENFORCED](with-security-enforced.md) | User-mode SOQL |
| [User Mode vs System Mode](user-mode-vs-system-mode.md) | Validation channel |
| [Sharing Keywords](sharing-keywords.md) | with/without sharing |
| [Experience Cloud Security](experience-cloud-security.md) | Community |
| [Shield Platform Encryption](shield-platform-encryption.md) | Encryption |
| [Session Security](session-security.md) | Session |
| [MFA](mfa.md) | Multi-factor |
| [Login Security](login-security.md) | Login policies |
| [Connected Apps](connected-apps.md) | OAuth apps |
| [API Security](api-security.md) | API access |
""")

    playbooks = [
        ("CRUD Validation Playbook", "crud-validation.md", "Validate object CRUD per persona across channels.",
         ["Persona list", "Object inventory", "Channel UI/API"],
         ["Build CRUD matrix.", "Execute positive/negative per cell.", "Document gaps and excessive access."],
         ["All objects in scope?", "API tested separately?"],
         ["CRUD Matrix", "Permission Validation Report"],
         ["Matrix complete with Pass/Fail", "No unexplained Modify All"],
         ["Excessive CRUD → Security Architect"],
         "[../../knowledge/security/object-level-security.md](../../knowledge/security/object-level-security.md)"),
        ("FLS Validation Playbook", "fls-validation.md", "Validate field read/edit/hidden per persona.",
         ["Sensitive field list", "Layouts/Dynamic Forms", "Personas"],
         ["Map FLS per field.", "UI verify hidden/read-only.", "API field-level check via SOVA."],
         ["Encrypted fields?", "Formula fields read-only?"],
         ["FLS Validation Matrix"],
         ["Sensitive fields protected", "No leakage via related lists"],
         ["Sensitive exposure → Compliance advisory"],
         ""),
        ("Sharing Validation Playbook", "sharing-validation.md", "Validate OWD, rules, roles, manual sharing.",
         ["OWD settings", "Sharing/restriction rules", "Role hierarchy"],
         ["Predict baseline access.", "Test rule criteria populations.", "Validate manual share scenarios."],
         ["Territory in scope?", "Apex sharing involved?"],
         ["Record Access Matrix", "Sharing Validation section"],
         ["Expected visibility confirmed", "Negative hidden records verified"],
         ["Sharing conflict → Solution Architect"],
         ""),
        ("Experience Cloud Security Playbook", "experience-cloud-security.md", "Validate external user and guest access.",
         ["Community profiles", "Sharing sets", "Guest user config"],
         ["Separate matrix for external users.", "Test portal record visibility.", "Guest — minimal access verification."],
         ["Guest user in scope?", "Partner vs customer community?"],
         ["Experience Cloud Security Checklist"],
         ["External users cannot access internal records", "Guest cannot escalate"],
         ["Guest change → Critical — Release Manager"],
         ""),
        ("API Security Validation Playbook", "api-security-validation.md", "Validate integration and API user permissions.",
         ["Integration user identity", "Connected apps", "Named credentials"],
         ["CRUD/FLS for API user.", "Compare API response to UI.", "OAuth scope review."],
         ["Bulk API in scope?", "Modify All on integration user?"],
         ["API Security Validation section"],
         ["API least privilege", "No excessive scope"],
         ["Scope expansion → Integration Architect"],
         "[../soql-validation-assistant/SKILL.md](../soql-validation-assistant/SKILL.md)"),
        ("Release Security Validation Playbook", "release-security-validation.md", "Pre/post deploy security regression pack.",
         ["Deploy manifest security components", "MIA impact report if available"],
         ["Identify profile/perm/sharing changes.", "Select regression security scenarios.", "Execute release checklist."],
         ["Production deploy?", "Rollback for security components?"],
         ["Release Security Checklist", "Deployment Security Report"],
         ["No Critical open security defects", "Sign-off from security delegate"],
         ["Critical → No-Go"],
         "[../../knowledge/release/release-readiness.md](../../knowledge/release/release-readiness.md)"),
        ("Regression Security Playbook", "regression-security.md", "Security regression scope from metadata or release changes.",
         ["Changed security metadata", "Persona inventory"],
         ["Map change to impacted personas/objects.", "In/Out/Conditional security tests.", "Link SOVA for backend proofs."],
         ["Can any persona be Out of scope?"],
         ["Regression Scope section", "Security Test Checklist"],
         ["High-risk personas covered", "Negative paths included"],
         ["Scope dispute → Test Lead + Security Architect"],
         "[../../playbooks/regression-planning.md](../../playbooks/regression-planning.md)"),
    ]
    for title, slug, *rest in playbooks:
        write(f"playbooks/{slug}", playbook(title, slug, *rest))

    write("playbooks/README.md", fm("Permission Testing — Playbooks", "QE Specialized Skill Playbook", "Guide", ["permission-testing"]) + """# Permission Testing — Playbooks

| Playbook | Focus |
|----------|-------|
| [CRUD Validation](crud-validation.md) | Object CRUD |
| [FLS Validation](fls-validation.md) | Field access |
| [Sharing Validation](sharing-validation.md) | OWD/rules/roles |
| [Experience Cloud Security](experience-cloud-security.md) | Community/guest |
| [API Security Validation](api-security-validation.md) | API/integration |
| [Release Security Validation](release-security-validation.md) | Release gate |
| [Regression Security](regression-security.md) | Security regression |
""")

    templates = [
        ("Permission Validation Report", OUTPUT_SECTIONS),
        ("CRUD Matrix", ["Persona", "Object", "Create", "Read", "Update", "Delete", "Expected", "Actual", "Pass/Fail"]),
        ("FLS Validation Matrix", ["Persona", "Object", "Field", "Read", "Edit", "Expected UI", "Actual", "Pass/Fail"]),
        ("Record Access Matrix", ["Persona", "Record Context", "Expected Visibility", "Actual", "Sharing Path", "Pass/Fail"]),
        ("Security Test Checklist", ["Scenario", "Persona", "Type", "Steps", "Expected", "Status"]),
        ("Experience Cloud Security Checklist", ["User Type", "Object", "Access", "Negative Test", "Status"]),
        ("Release Security Checklist", ["Component", "Change", "Regression Pack", "Evidence", "Sign-off"]),
        ("Deployment Security Report", ["Executive Summary", "Changes", "Risk", "Matrices", "Open Issues", "Recommendation"]),
    ]
    for title, sections in templates:
        slug = title.lower().replace(" ", "-") + ".md"
        write(f"templates/{slug}", template_doc(title, sections))

    write("templates/README.md", fm("Permission Testing — Templates", "QE Specialized Skill Template", "Guide", ["permission-testing"]) + """# Permission Testing — Templates

| Template | Use |
|----------|-----|
| [Permission Validation Report](permission-validation-report.md) | Primary 19-section deliverable |
| [CRUD Matrix](crud-matrix.md) | CRUD proof |
| [FLS Validation Matrix](fls-validation-matrix.md) | Field access |
| [Record Access Matrix](record-access-matrix.md) | Sharing visibility |
| [Security Test Checklist](security-test-checklist.md) | Execution checklist |
| [Experience Cloud Security Checklist](experience-cloud-security-checklist.md) | Community |
| [Release Security Checklist](release-security-checklist.md) | Release gate |
| [Deployment Security Report](deployment-security-report.md) | Deploy review |
""")

    base = (
        "Act as Permission Testing Agent. Reason through Security Context and Business Requirement BEFORE test scenarios. "
        "Produce all 19 sections per SKILL.md. Include CRUD, FLS, Sharing, negative scenarios. "
        "Delegate detailed SOQL to SOQL Validation Assistant when expanding section 17. Context:\n[paste]"
    )
    prompts = [
        ("Validate CRUD", "validate-crud.md", base, OUTPUT_SECTIONS),
        ("Validate FLS", "validate-fls.md", base + "\nFocus: Field Level Security matrices and hidden field negative tests.", OUTPUT_SECTIONS),
        ("Review Permission Sets", "review-permission-sets.md", base + "\nFocus: permission set and PSG deltas, excessive permissions.", OUTPUT_SECTIONS),
        ("Review Profiles", "review-profiles.md", base + "\nFocus: profile changes, community profiles, least privilege.", OUTPUT_SECTIONS),
        ("Analyze Sharing Rules", "analyze-sharing-rules.md", base + "\nFocus: OWD, sharing rules, restriction rules, record visibility.", OUTPUT_SECTIONS),
        ("Validate Record Visibility", "validate-record-visibility.md", base + "\nFocus: record access matrix and ownership/transfer.", OUTPUT_SECTIONS),
        ("Verify Experience Cloud Access", "verify-experience-cloud-access.md", base + "\nFocus: partner, customer, guest user paths.", OUTPUT_SECTIONS),
        ("Verify API Security", "verify-api-security.md", base + "\nFocus: integration user, connected app, API CRUD/FLS.", OUTPUT_SECTIONS),
        ("Generate Security Test Cases", "generate-security-test-cases.md", base + "\nFocus: sections 14-16 negative scenarios and regression scope.", OUTPUT_SECTIONS),
        ("Review Deployment Security", "review-deployment-security.md", base + "\nFocus: sections 18-19 deployment risks and recommendations.", OUTPUT_SECTIONS),
    ]
    for title, slug, prompt, sections in prompts:
        write(f"prompts/{slug}", prompt_doc(title, prompt, sections))

    write("prompts/README.md", fm("Permission Testing — Prompts", "QE Specialized Skill Prompt", "Guide", ["permission-testing"]) + """# Permission Testing — Prompts

| Prompt | File |
|--------|------|
| Validate CRUD | [validate-crud.md](validate-crud.md) |
| Validate FLS | [validate-fls.md](validate-fls.md) |
| Review Permission Sets | [review-permission-sets.md](review-permission-sets.md) |
| Review Profiles | [review-profiles.md](review-profiles.md) |
| Analyze Sharing Rules | [analyze-sharing-rules.md](analyze-sharing-rules.md) |
| Validate Record Visibility | [validate-record-visibility.md](validate-record-visibility.md) |
| Verify Experience Cloud Access | [verify-experience-cloud-access.md](verify-experience-cloud-access.md) |
| Verify API Security | [verify-api-security.md](verify-api-security.md) |
| Generate Security Test Cases | [generate-security-test-cases.md](generate-security-test-cases.md) |
| Review Deployment Security | [review-deployment-security.md](review-deployment-security.md) |
""")

    examples = [
        ("Sales User Profile", "sales-user-profile.md", "Inside sales reps manage own Opportunities.", "Create/read/edit own Opportunities; no delete on Account.",
         "CRUD matrix for Sales User on Opportunity/Account; FLS on Amount field.", "Own records visible; cannot delete Account.", "Cannot edit peer-owned Opportunity.",
         "SELECT Id, OwnerId FROM Opportunity WHERE OwnerId != :currentUserId LIMIT 5", "Regression on Opportunity team if enabled."),
        ("Service User Profile", "service-user-profile.md", "Agents work Cases for assigned queue.", "Read/edit Case; no Account delete.",
         "Queue membership + Case CRUD; record access via queue.", "Queue Cases editable.", "Non-queue Case not editable.",
         "SELECT Id, OwnerId FROM Case WHERE OwnerId = :queueId LIMIT 10", "Omni-channel assignment separate test."),
        ("System Administrator", "system-administrator.md", "Admin deploy — verify least privilege not expanded accidentally.", "Admin retains full access — use only for setup proof not business sign-off.",
         "Document admin vs business persona separation.", "Admin can access all test records.", "Business user matrix is authoritative for UAT.",
         "N/A — use business persona SOQL", "Never sign off business rules as admin only."),
        ("Partner Community User", "partner-community-user.md", "Partners see shared Opportunities.", "Read/edit shared Opportunities only.",
         "Sharing set / criteria sharing tests.", "Shared opps visible.", "Non-shared opps hidden.",
         "SELECT Id FROM Opportunity WHERE Id NOT IN (SELECT ParentId FROM PartnerNetworkRecordConnection LIMIT 100)", "Critical regression on sharing set deploy."),
        ("Customer Community User", "customer-community-user.md", "Customers view own Cases.", "Read own Cases via account contact relationship.",
         "Contact/Account linkage visibility.", "Own cases visible.", "Other customer cases hidden.",
         "SELECT Id, ContactId FROM Case WHERE ContactId = :contactId", "Profile change Critical risk."),
        ("Guest User", "guest-user.md", "Public knowledge articles only.", "Guest cannot access CRM objects.",
         "Minimal guest profile audit.", "Only public content accessible.", "Any CRM object access fails.",
         "Verify no object CRUD on guest profile via setup metadata review", "Critical — Legal/Security review for guest changes."),
        ("Field Hidden", "field-hidden.md", "SSN field hidden from standard users.", "FLS Read/Edit off for SSN__c.",
         "UI + API field absence for persona.", "Field not in layout/API.", "Admin can still see — separate matrix.",
         "Query with SOVA user-mode if API check needed", "Pair with Shield encryption if applicable."),
        ("Record Not Visible", "record-not-visible.md", "Private OWD Account — user not in share.", "Record not visible without share/role.",
         "Sharing validation negative test.", "User cannot see record in UI/search.", "Owner can see.",
         "SELECT Id FROM Account WHERE Id = :recordId — expect 0 rows as test user", "Document sharing path when visible."),
        ("Sharing Rule Added", "sharing-rule-added.md", "Criteria share opens Cases in Region West.", "West region agents see additional Cases.",
         "Before/after visibility comparison.", "West Cases visible post rule.", "East Cases unchanged.",
         "SELECT Id, Region__c FROM Case WHERE Region__c = 'West' LIMIT 20", "Regression all personas in rule criteria."),
        ("Restriction Rule Added", "restriction-rule-added.md", "Hide high-value Accounts from standard sales.", "Accounts with Tier=Platinum hidden except exec role.",
         "Restriction + role exception tests.", "Standard user cannot see Platinum.", "Exec role can see.",
         "SELECT Id FROM Account WHERE Tier__c = 'Platinum'", "Combine with sharing rules in test plan."),
        ("Permission Set Updated", "permission-set-updated.md", "Grant Edit on WorkOrder to Dispatchers.", "Dispatchers edit WorkOrder priority field.",
         "PS assignment + FLS verification.", "Dispatcher edits succeed.", "Technician without PS cannot edit.",
         "SELECT AssigneeId FROM PermissionSetAssignment WHERE PermissionSet.Name = 'Dispatcher'", "PSG assignment smoke test."),
        ("Profile Modified", "profile-modified.md", "Community profile Case CRUD reduced to Read.", "Portal users read-only Case.",
         "Community profile CRUD matrix.", "Edit blocked with clear error.", "Internal profile unchanged.",
         "ObjectPermissions query for community profile Case Edit=false", "Critical deploy risk."),
        ("Queue Assignment", "queue-assignment.md", "Cases route to Support Queue.", "Queue members access queue-owned Cases.",
         "Queue + Case CRUD tests.", "Member can edit queue case.", "Non-member cannot.",
         "SELECT Id FROM GroupMember WHERE Group.Type = 'Queue'", "Validate queue email routing separately."),
        ("Apex Sharing", "apex-sharing.md", "Apex without sharing creates shared custom object rows.", "Users see records created by batch job per sharing model.",
         "Identify Apex keyword; test resulting visibility.", "Records visible per sharing design.", "Wrong keyword → over-exposure.",
         "Document Apex class sharing mode; manual record checks", "Code review + QA visibility matrix."),
    ]
    for title, slug, scenario, req, strategy, expected, negative, soql, qa in examples:
        write(f"examples/{slug}", example_doc(title, scenario, req, strategy, expected, negative, soql, qa))

    write("examples/README.md", fm("Permission Testing — Examples", "QE Specialized Skill Example", "Guide", ["permission-testing"]) + """# Permission Testing — Examples

| Example | Focus |
|---------|-------|
| [Sales User Profile](sales-user-profile.md) | Sales CRUD |
| [Service User Profile](service-user-profile.md) | Service queue |
| [System Administrator](system-administrator.md) | Admin separation |
| [Partner Community User](partner-community-user.md) | Partner sharing |
| [Customer Community User](customer-community-user.md) | Customer portal |
| [Guest User](guest-user.md) | Guest minimal access |
| [Field Hidden](field-hidden.md) | FLS hidden |
| [Record Not Visible](record-not-visible.md) | Sharing negative |
| [Sharing Rule Added](sharing-rule-added.md) | Sharing rule |
| [Restriction Rule Added](restriction-rule-added.md) | Restriction |
| [Permission Set Updated](permission-set-updated.md) | Perm set |
| [Profile Modified](profile-modified.md) | Profile |
| [Queue Assignment](queue-assignment.md) | Queue |
| [Apex Sharing](apex-sharing.md) | Apex keyword |
""")

    tests = [
        ("crud-testing", "CRUD matrix present before scenarios"),
        ("fls-testing", "FLS section with hidden/read-only negatives"),
        ("sharing-testing", "Sharing validation with OWD context"),
        ("profile-testing", "Profile validation separated from perm sets"),
        ("permission-set-testing", "Perm set and PSG sections populated"),
        ("permission-set-group-testing", "PSG muting considered"),
        ("experience-cloud-security", "Community/guest separate path"),
        ("guest-user-access", "Guest treated as Critical risk"),
        ("api-security", "API Security section for integration users"),
        ("session-security", "Session/MFA noted in Security Context"),
        ("release-validation", "Deployment risks for security metadata"),
        ("regression-validation", "Regression scope In/Out/Conditional"),
    ]
    for slug, desc in tests:
        write(f"tests/scenario-{slug}.md", fm(f"Test — {slug}", "QE Specialized Skill Test", "Test Scenario", ["permission-testing"]) + f"""# Test Scenario — {slug}

## Objective

{desc}

## Pass Criteria

- Security Context before test scenarios
- Sections 5–13 populated as applicable
- Negative Test Scenarios present
- Recommended SOQL references SOVA when expanded

## Fail Criteria

- Test cases without security reasoning
- Missing CRUD/FLS/Sharing analysis
- Admin-only sign-off for business personas
""")

    write("tests/README.md", fm("Permission Testing — Tests", "QE Specialized Skill Test", "Guide", ["permission-testing"]) + """# Permission Testing — Tests

| Scenario | Focus |
|----------|-------|
| [crud-testing](scenario-crud-testing.md) | CRUD matrix |
| [fls-testing](scenario-fls-testing.md) | FLS |
| [sharing-testing](scenario-sharing-testing.md) | Sharing |
| [profile-testing](scenario-profile-testing.md) | Profiles |
| [permission-set-testing](scenario-permission-set-testing.md) | Perm sets |
| [permission-set-group-testing](scenario-permission-set-group-testing.md) | PSG |
| [experience-cloud-security](scenario-experience-cloud-security.md) | Community |
| [guest-user-access](scenario-guest-user-access.md) | Guest |
| [api-security](scenario-api-security.md) | API |
| [session-security](scenario-session-security.md) | Session |
| [release-validation](scenario-release-validation.md) | Release |
| [regression-validation](scenario-regression-validation.md) | Regression |
""")

    print("Done.")


if __name__ == "__main__":
    main()
