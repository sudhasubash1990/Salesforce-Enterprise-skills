#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');
const { config, ensureDirs, missingCredentialsMessage } = require('./config/config');
const { FULL_TRANSCRIPT, PREVIEW_TRANSCRIPT } = require('./config/transcript');
const { composeScene } = require('./video/sceneComposer');
const { prepareImageLayers } = require('./video/imageProcessor');
const { generateAudio, probeDuration } = require('./video/audioGenerator');
const { generateTalkingAvatar } = require('./video/avatarGenerator');
const { compositeScene, renderFinal } = require('./video/compositor');
const { validateOutputs } = require('./utils/validation');
const logger = require('./utils/logger');

function usage() {
  return `Usage: node src/index.js <preview|generate|validate|render>

  preview   10–15s lip-sync test (“Hello, and welcome. My name is Nina.”)
  generate  Full narration + talking-avatar layer + composite
  validate  Quality checks against the latest render
  render    Final 1920×1080 H.264/AAC MP4
`;
}

async function ensureScene() {
  ensureDirs();
  if (!fs.existsSync(config.sourceImage) || !fs.existsSync(config.layoutPath)) {
    await composeScene();
  }
  return prepareImageLayers();
}

async function runPreview() {
  const layout = await ensureScene();
  const audioPath = path.join(config.tempDir, 'preview-audio.wav');
  const ninaVideo = path.join(config.tempDir, 'nina-talking-preview.mp4');
  const composited = path.join(config.tempDir, 'preview-composited.mp4');

  await generateAudio(PREVIEW_TRANSCRIPT, { outputPath: audioPath, padToSeconds: config.previewSeconds });
  const duration = await probeDuration(audioPath);
  logger.info('Preview audio duration', { duration });

  const avatar = await generateTalkingAvatar({
    image: config.ninaCropPath,
    audio: audioPath,
    transcript: PREVIEW_TRANSCRIPT,
    voice: config.tts.edgeVoice,
    outputPath: ninaVideo,
  });
  logger.info('Preview avatar ready', avatar);

  await compositeScene({
    sourceImage: layout.working || config.sourceImage,
    ninaTalking: ninaVideo,
    audioPath,
    layoutPath: config.layoutPath,
    outputPath: composited,
    duration,
  });

  await renderFinal({
    composited,
    audioPath,
    outputPath: config.previewOutput,
  });

  const report = await validateOutputs({
    videoPath: config.previewOutput,
    sourceImage: config.sourceImage,
    layoutPath: config.layoutPath,
    audioPath,
    reportPath: path.join(config.outputDir, 'preview-validation.json'),
  });
  logger.info('Preview complete', { output: config.previewOutput, passed: report.passed });
  return { output: config.previewOutput, report };
}

async function runGenerate() {
  const layout = await ensureScene();
  await generateAudio(FULL_TRANSCRIPT, { outputPath: config.audioPath });
  const duration = await probeDuration(config.audioPath);
  logger.info('Full audio duration', { duration });

  const avatar = await generateTalkingAvatar({
    image: config.ninaCropPath,
    audio: config.audioPath,
    transcript: FULL_TRANSCRIPT,
    voice: config.tts.edgeVoice,
    outputPath: config.ninaTalkingPath,
  });

  await compositeScene({
    sourceImage: layout.working || config.sourceImage,
    ninaTalking: config.ninaTalkingPath,
    audioPath: config.audioPath,
    layoutPath: config.layoutPath,
    outputPath: config.compositedPath,
    duration,
  });

  fs.writeFileSync(
    path.join(config.tempDir, 'generate-meta.json'),
    JSON.stringify({ duration, avatar, layout: config.layoutPath }, null, 2)
  );
  logger.info('Generate stage complete', {
    ninaTalking: config.ninaTalkingPath,
    composited: config.compositedPath,
    duration,
  });
  return { duration, avatar };
}

async function runRender() {
  if (!fs.existsSync(config.compositedPath) || !fs.existsSync(config.audioPath)) {
    logger.info('Composite missing — running generate first');
    await runGenerate();
  }
  await renderFinal({
    composited: config.compositedPath,
    audioPath: config.audioPath,
    outputPath: config.finalOutput,
  });
  logger.info('Final render written', { output: config.finalOutput });
  return { output: config.finalOutput };
}

async function runValidate() {
  const videoPath = fs.existsSync(config.finalOutput) ? config.finalOutput : config.previewOutput;
  if (!fs.existsSync(videoPath)) {
    throw new Error('No rendered video found. Run npm run preview or npm run render first.');
  }
  const audioPath = fs.existsSync(config.audioPath)
    ? config.audioPath
    : path.join(config.tempDir, 'preview-audio.wav');
  const report = await validateOutputs({
    videoPath,
    sourceImage: config.sourceImage,
    layoutPath: config.layoutPath,
    audioPath,
    reportPath: config.validationReport,
  });
  logger.info('Validation finished', { passed: report.passed, report: config.validationReport });
  if (!report.passed) process.exitCode = 2;
  return report;
}

async function main() {
  const command = process.argv[2];
  if (!command || command === '--help' || command === '-h') {
    process.stdout.write(usage());
    return;
  }
  try {
    if (command === 'preview') await runPreview();
    else if (command === 'generate') await runGenerate();
    else if (command === 'render') await runRender();
    else if (command === 'validate') await runValidate();
    else {
      process.stderr.write(usage());
      process.exit(1);
    }
  } catch (error) {
    if (String(error.message).includes('credentials are not configured')) {
      logger.error(missingCredentialsMessage());
    } else {
      logger.error(error.message);
    }
    process.exit(1);
  }
}

main();
