---
title: Permission Testing Agent — README
module: Salesforce Quality Engineering
category: QE Specialized Skill
document_type: Guide
version: 0.17.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [permission-testing]
---

# Permission Testing Agent

## Purpose

Enterprise **Security QA reasoning engine** for Salesforce permissions, sharing, and access control. Reasons through the security model before generating test scenarios — not a checklist generator.

## Capabilities

- CRUD, FLS, record access, and sharing validation matrices  
- Profile, permission set, and PSG analysis  
- Experience Cloud and guest user security paths  
- API/integration security validation  
- Negative scenarios, regression scope, deployment risks  
- Integration with [Metadata Impact Analyzer](../metadata-impact-analyzer/SKILL.md) and [SOQL Validation Assistant](../soql-validation-assistant/SKILL.md)

## Supported Security Components

Profiles · Permission Sets · PSG · Roles · OWD · Sharing/Restriction/Scoping Rules · Queues · Territories · Manual/Apex Sharing · Login/Session/MFA · Connected Apps · API · Experience Cloud · Guest Users · Shield (advisory)

## Folder Structure

```
skills/permission-testing-agent/
├── SKILL.md
├── README.md
├── skill-config.yaml
├── knowledge/       ← 21 reasoning articles
├── playbooks/       ← 7 playbooks
├── templates/       ← 8 templates
├── prompts/         ← 10 prompts
├── examples/        ← 14 examples
└── tests/           ← 12 scenarios
```

## Inputs

| Input | Required |
|-------|----------|
| Business requirement / persona | Yes |
| Security metadata change or scope | Yes |
| MIA impact report | When deploy-driven |
| Environment | Recommended |

## Outputs

19-section [Permission Validation Report](templates/permission-validation-report.md).

## Sample Prompt

```
Load skills/permission-testing-agent/SKILL.md.
Business Requirement: Dispatchers edit WorkOrder priority; Technicians read-only.
Security change: Permission set FSL_Dispatcher updated.
Produce all 19 sections including negative scenarios and CRUD/FLS matrices.
```

## Best Practices

- Always test as **business persona**, not admin  
- Separate community/guest validation packs  
- Flag View All / Modify All as high risk  
- Chain to SOVA for security-aware SOQL with run-as context  

## Security Considerations

- Zero rows in SOQL may mean FLS/sharing — not always clean validation  
- System mode Apex can invalidate UI-only tests  
- Guest user changes require Critical deployment review  

## Known Limitations

- No live org login in skill pack  
- Shield/legal attestations require human Compliance review  
- OmniStudio/Agentforce depth varies by org — mark Partial when unknown  

## Future Enhancements

- Risk-Based Regression capability integration  
- Production RCA security incident patterns  
- Automated CRUD matrix diff from metadata deploy  

## Related Documents

- [SKILL.md](SKILL.md)
- [../README.md](../README.md)
- [../../knowledge/security/README.md](../../knowledge/security/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.17.0 | 2026-07-27 | QE Practice Lead | Initial release |
