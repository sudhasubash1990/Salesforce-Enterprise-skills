'use strict';

const logger = require('./logger');

async function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function withRetry(fn, { attempts = 3, baseMs = 2000, label = 'operation' } = {}) {
  let lastError;
  for (let i = 1; i <= attempts; i += 1) {
    try {
      return await fn(i);
    } catch (error) {
      lastError = error;
      logger.warn(`${label} failed`, {
        attempt: i,
        attempts,
        message: error.message,
      });
      if (i < attempts) {
        const delay = baseMs * 2 ** (i - 1);
        logger.info(`${label} retrying`, { delayMs: delay });
        await sleep(delay);
      }
    }
  }
  throw lastError;
}

module.exports = { withRetry, sleep };
