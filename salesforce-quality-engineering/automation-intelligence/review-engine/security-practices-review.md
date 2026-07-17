---
title: Security Practices Review (Secrets Management)
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# Security Practices Review (Secrets Management)

## Purpose

Evaluate secrets handling, credential hygiene, and security-sensitive automation practices.

## Business Context

Leaked sandbox passwords, security tokens, or Connected App secrets are P0 enterprise risks—even in “test” repos.

## Architecture

Secrets in vault/CI secret store; no credentials in git; least-privilege automation users; rotation; sanitized logs/artifacts.

## Decision Criteria

| Score | Signals |
|-------|---------|
| 5 | Vault/CI secrets; no secrets in repo; rotated service users; log redaction |
| 3 | Env vars locally but samples in git history risk; inconsistent |
| 1 | Passwords/tokens in config files, tests, or READMEs |

**Security score ≤ 2 ⇒ overall review status At Risk** (see scoring model).

## Best Practices

- Dedicated automation users per env; no human shared passwords.  
- Never commit `.env` with secrets; scan history if exposure found.  
- Redact auth headers in traces.  

## Salesforce Considerations

- Named Credentials / Connected Apps / refresh tokens need secure storage.  
- Prefer JWT/OAuth flows designed for automation over stored passwords where feasible.  

## Automation Considerations

- Link [../framework-design/secrets-management.md](../framework-design/secrets-management.md).  

## Common Pitfalls

- “It’s only a sandbox” justification for committed secrets.  
- Sharing one Sys Admin user across all pipelines.  

## Examples

Credentials in `config.json` committed → Security **1**, P0 rotate + purge + vault.

## Interview Questions

- What is a P0 security finding in an automation review?  

## Related Documents

- [../ci-cd/azure-devops-pipelines.md](../ci-cd/azure-devops-pipelines.md)
- [Maintainability Score](maintainability-score.md)

## Navigation

- **Previous:** [governance-compliance-review.md](governance-compliance-review.md)
- **Next:** [maintainability-score.md](maintainability-score.md)

## Future Enhancements

- Secret-scanning checklist for reviews  
