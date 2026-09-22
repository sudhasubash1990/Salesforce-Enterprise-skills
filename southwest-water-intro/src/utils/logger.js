'use strict';

function timestamp() {
  return new Date().toISOString();
}

function sanitize(value) {
  if (typeof value !== 'string') return value;
  return value
    .replace(/Bearer\s+[A-Za-z0-9._-]+/gi, 'Bearer [redacted]')
    .replace(/x-api-key["']?\s*[:=]\s*["']?[^"'\s]+/gi, 'x-api-key=[redacted]')
    .replace(/api[_-]?key["']?\s*[:=]\s*["']?[^"'\s]+/gi, 'api_key=[redacted]');
}

function log(level, message, meta) {
  const line = { ts: timestamp(), level, message };
  if (meta !== undefined) {
    line.meta = typeof meta === 'string' ? sanitize(meta) : JSON.parse(sanitize(JSON.stringify(meta)));
  }
  const stream = level === 'error' ? process.stderr : process.stdout;
  stream.write(`${JSON.stringify(line)}\n`);
}

module.exports = {
  info: (message, meta) => log('info', message, meta),
  warn: (message, meta) => log('warn', message, meta),
  error: (message, meta) => log('error', message, meta),
  debug: (message, meta) => {
    if (process.env.DEBUG) log('debug', message, meta);
  },
};
