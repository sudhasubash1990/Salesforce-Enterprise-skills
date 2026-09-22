'use strict';

/**
 * Provider-independent talking-avatar contract.
 * Implementations: HeyGen, D-ID, Replicate, local viseme renderer.
 */
const {
  generateTalkingAvatar,
  generateHeyGen,
  generateDid,
  generateReplicate,
  generateLocal,
} = require('../video/avatarGenerator');

module.exports = {
  generateTalkingAvatar,
  generateHeyGen,
  generateDid,
  generateReplicate,
  generateLocal,
};
