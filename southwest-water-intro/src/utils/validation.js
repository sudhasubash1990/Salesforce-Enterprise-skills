'use strict';

const fs = require('fs');
const path = require('path');
const { config } = require('../config/config');
const { runPython } = require('../video/imageProcessor');
const logger = require('./logger');

async function validateOutputs({ videoPath, sourceImage, layoutPath, audioPath, reportPath }) {
  const script = path.join(__dirname, '../python/validate_video.py');
  logger.info('Running quality validation', { videoPath });
  const raw = await runPython(script, [
    '--video',
    videoPath,
    '--source',
    sourceImage,
    '--layout',
    layoutPath,
    '--audio',
    audioPath,
    '--out',
    reportPath || config.validationReport,
  ]);
  const report = JSON.parse(raw.split('\n').filter(Boolean).pop());
  fs.writeFileSync(reportPath || config.validationReport, JSON.stringify(report, null, 2), 'utf8');
  return report;
}

module.exports = { validateOutputs };
