'use strict';

/**
 * Narration must be used verbatim. Do not rewrite.
 */
const FULL_TRANSCRIPT = `Hello, and welcome. My name is Nina, and I'll be your guide through this demonstration.

Over the next few minutes you'll follow a single customer journey from end to end, exactly as it would play out in a live contact centre.

You'll hear two voices. The first is Alex, a contact centre advisor at Southwest Water, working in Salesforce. The second is Harvey Spector, a customer who has just moved into a new property and is calling to set up his account.

Everything Alex does on screen happens in real time, as he speaks with Harvey.

The call covers the full move-in journey: searching for an existing record, creating the contact and household account, capturing priority service needs, validating the property, completing the move-in, and logging the case.

After the call, we'll follow Harvey into the self-service portal, where he registers, submits a meter reading, views his first bill, and pays online.

Let's join the call.`;

const PREVIEW_TRANSCRIPT = `Hello, and welcome. My name is Nina.`;

const SCENES = [
  {
    id: 'opening',
    name: 'Opening',
    startSec: 0,
    endSec: 8,
    camera: 'nina',
    highlight: null,
    line: "Hello, and welcome. My name is Nina, and I'll be your guide through this demonstration.",
  },
  {
    id: 'journey-intro',
    name: 'Customer Journey Introduction',
    startSec: 8,
    endSec: 18,
    camera: 'journey',
    highlight: null,
    line: 'Over the next few minutes you\'ll follow a single customer journey from end to end, exactly as it would play out in a live contact centre.',
  },
  {
    id: 'introduce-cast',
    name: 'Introduce Alex and Harvey',
    startSec: 18,
    endSec: 31,
    camera: 'cast',
    highlight: 'cast',
    line: 'You\'ll hear two voices. The first is Alex, a contact centre advisor at Southwest Water, working in Salesforce. The second is Harvey Spector, a customer who has just moved into a new property and is calling to set up his account.',
  },
  {
    id: 'realtime',
    name: 'Real-Time Demonstration',
    startSec: 31,
    endSec: 38,
    camera: 'nina',
    highlight: null,
    line: 'Everything Alex does on screen happens in real time, as he speaks with Harvey.',
  },
  {
    id: 'move-in',
    name: 'Move-In Journey',
    startSec: 38,
    endSec: 50,
    camera: 'journey',
    highlight: 'movein',
    line: 'The call covers the full move-in journey: searching for an existing record, creating the contact and household account, capturing priority service needs, validating the property, completing the move-in, and logging the case.',
  },
  {
    id: 'self-service',
    name: 'Self-Service Journey',
    startSec: 50,
    endSec: 62,
    camera: 'selfservice',
    highlight: 'selfservice',
    line: 'After the call, we\'ll follow Harvey into the self-service portal, where he registers, submits a meter reading, views his first bill, and pays online.',
  },
  {
    id: 'join-call',
    name: 'Transition to Call',
    startSec: 62,
    endSec: 67,
    camera: 'nina-end',
    highlight: null,
    line: "Let's join the call.",
  },
];

const MOVE_IN_ICONS = [
  'Call',
  'Search',
  'Create Customer',
  'Property Validation',
  'Move-in',
  'Log Case',
];

const SELF_SERVICE_ICONS = [
  'Self-Service Portal',
  'Meter Reading',
  'View Bill',
  'Pay Online',
];

module.exports = {
  FULL_TRANSCRIPT,
  PREVIEW_TRANSCRIPT,
  SCENES,
  MOVE_IN_ICONS,
  SELF_SERVICE_ICONS,
};
