---
title: Salesforce Compatibility Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, compatibility-testing]
---

# Salesforce Compatibility Testing

## Purpose

Reference for assessing browser and device compatibility testing scope for Salesforce.

## Browser Support Matrix

| Browser | Lightning Experience | Experience Cloud | Notes |
|---------|---------------------|-----------------|-------|
| **Chrome (latest)** | Supported | Supported | Primary test browser |
| **Edge (latest)** | Supported | Supported | Chromium-based |
| **Firefox (latest)** | Supported | Supported | ESR also supported |
| **Safari (latest)** | Supported | Supported | macOS and iOS |

> Always verify against the current [Salesforce Supported Browsers](https://help.salesforce.com/s/articleView?id=sf.getstart_browser_overview.htm) documentation for the active release.

## Device Form Factors

| Form Factor | Context | Key Considerations |
|-------------|---------|-------------------|
| **Desktop** | Lightning Experience, Classic | Full functionality baseline |
| **Tablet** | Salesforce Mobile, Experience Cloud | Touch + keyboard, responsive layouts |
| **Phone** | Salesforce Mobile, Experience Cloud | Compact layouts, touch-only, smaller viewport |

## Compatibility Test Focus Areas

### Lightning Experience
- Custom LWC rendering across browsers
- CSS compatibility (flexbox, grid, custom properties)
- JavaScript API differences (clipboard, notifications)

### Experience Cloud
- Public-facing site across all supported browsers
- Custom theme rendering consistency
- Third-party component compatibility
- Guest user experience across devices

### Salesforce Mobile App
- iOS supported versions (current and previous major)
- Android supported versions (current and previous major)
- Device-specific rendering (notch, safe areas, gesture navigation)

## Test Combination Strategy

Full matrix testing is impractical. Prioritize:

1. **Primary:** Chrome desktop + iOS Safari mobile
2. **Secondary:** Edge desktop + Android Chrome mobile
3. **Tertiary:** Firefox desktop + tablet form factor
4. **Risk-based:** Add combinations for known issues or audience demographics

## Related

- [Mobile Testing](mobile-testing.md) — Mobile-specific scenarios
- [Accessibility Testing](accessibility-testing.md) — Cross-browser assistive tech
- [Specialized Testing Model](specialized-testing-model.md)
