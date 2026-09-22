'use strict';

const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const { config } = require('../config/config');
const { runPython } = require('./imageProcessor');
const logger = require('../utils/logger');

async function compositeScene({
  sourceImage,
  ninaTalking,
  audioPath,
  layoutPath,
  outputPath,
  duration,
}) {
  const script = path.join(__dirname, '../python/composite_scene.py');
  logger.info('Compositing Nina talking layer over original scene');
  await runPython(script, [
    '--source',
    sourceImage,
    '--nina-video',
    ninaTalking,
    '--audio',
    audioPath,
    '--layout',
    layoutPath,
    '--out',
    outputPath,
    '--fps',
    String(config.video.fps),
    '--width',
    String(config.video.width),
    '--height',
    String(config.video.height),
    '--duration',
    String(duration),
  ]);
  if (!fs.existsSync(outputPath)) {
    throw new Error('Compositor did not write an output file.');
  }
  return outputPath;
}

function muxFinal(inputVideo, audioPath, outputPath) {
  return new Promise((resolve, reject) => {
    const args = [
      '-y',
      '-i',
      inputVideo,
      '-i',
      audioPath,
      '-map',
      '0:v:0',
      '-map',
      '1:a:0',
      '-c:v',
      config.video.codec,
      '-preset',
      'medium',
      '-crf',
      '18',
      '-pix_fmt',
      'yuv420p',
      '-c:a',
      config.video.audioCodec,
      '-b:a',
      '192k',
      '-ar',
      String(config.video.sampleRate),
      '-shortest',
      '-movflags',
      '+faststart',
      outputPath,
    ];
    const proc = spawn('ffmpeg', args, { stdio: ['ignore', 'pipe', 'pipe'] });
    let err = '';
    proc.stderr.on('data', (d) => {
      err += d.toString();
    });
    proc.on('close', (code) => {
      if (code !== 0) reject(new Error(err.slice(-4000) || `ffmpeg exited ${code}`));
      else resolve(outputPath);
    });
  });
}

async function renderFinal({ composited, audioPath, outputPath }) {
  logger.info('Rendering final H.264/AAC MP4', { outputPath });
  return muxFinal(composited, audioPath, outputPath);
}

module.exports = { compositeScene, renderFinal, muxFinal };
