---
title: Mobile Test Assessment Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, mobile-testing, playbook]
---

# Mobile Test Assessment Playbook

## Purpose

Structured workflow for assessing Salesforce mobile testing scope.

## Assessment Steps

### Step 1 — Identify Mobile Scope
- Salesforce Mobile app usage (which objects, actions, flows)
- Field Service Lightning mobile requirements
- Experience Cloud responsive/mobile pages
- Custom LWC components on mobile

### Step 2 — Assess Mobile-Specific Functionality
- Compact layouts and mobile cards
- Quick actions and global actions on mobile
- Mobile navigation bar configuration
- Barcode scanning, geolocation, camera

### Step 3 — Assess Offline Requirements
- Offline briefcase configuration
- Offline record creation and editing
- Sync behavior on reconnect
- Conflict resolution strategy

### Step 4 — Assess Touch and Responsive Behavior
- Touch target sizes (minimum 44px)
- Gesture support (swipe, pinch, long press)
- Responsive breakpoints for LWC
- Orientation changes (portrait/landscape)

### Step 5 — Assess Device Matrix
- iOS versions to support
- Android versions to support
- Phone vs tablet form factors
- Salesforce Mobile app version compatibility

### Step 6 — Document Assessment
- Produce Mobile Assessment section in SST report
- Identify device/OS combinations for testing
- Flag offline testing environment needs

## Output

Mobile Assessment section (section 12 of 18-section SST report).

## Related

- [Mobile Testing Knowledge](../knowledge/mobile-testing.md)
- [Compatibility Testing Knowledge](../knowledge/compatibility-testing.md)
