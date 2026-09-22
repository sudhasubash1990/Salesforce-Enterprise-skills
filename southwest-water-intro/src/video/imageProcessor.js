'use strict';

const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const sharp = require('sharp');
const { config } = require('../config/config');
const { composeScene, defaultLayout } = require('./sceneComposer');
const logger = require('../utils/logger');

function runPython(script, args) {
  return new Promise((resolve, reject) => {
    const proc = spawn('python3', [script, ...args], { stdio: ['ignore', 'pipe', 'pipe'] });
    let out = '';
    let err = '';
    proc.stdout.on('data', (d) => {
      out += d.toString();
    });
    proc.stderr.on('data', (d) => {
      err += d.toString();
    });
    proc.on('close', (code) => {
      if (code !== 0) {
        reject(new Error(err || `python exited ${code}`));
        return;
      }
      resolve(out.trim());
    });
  });
}

async function detectAndCropNina(layout) {
  const script = path.join(__dirname, '../python/detect_nina.py');
  try {
    const raw = await runPython(script, [
      '--image',
      layout.working || config.sourceImage,
      '--hint-x',
      String(layout.nina.x),
      '--hint-y',
      String(layout.nina.y),
      '--hint-w',
      String(layout.nina.w),
      '--hint-h',
      String(layout.nina.h),
      '--crop-out',
      config.ninaCropPath,
      '--mask-out',
      config.ninaMaskPath,
    ]);
    const detected = JSON.parse(raw.split('\n').filter(Boolean).pop());
    logger.info('Nina detection complete', detected);
    return detected;
  } catch (error) {
    logger.warn('Python face detection unavailable; using left-panel layout crop', {
      message: error.message,
    });
    const nina = layout.nina;
    await sharp(layout.working || config.sourceImage)
      .extract({
        left: nina.x,
        top: nina.y,
        width: nina.w,
        height: Math.min(nina.h, 1080 - nina.y),
      })
      .png()
      .toFile(config.ninaCropPath);

    const w = nina.w;
    const h = Math.min(nina.h, 1080 - nina.y);
    const maskSvg = Buffer.from(
      `<svg width="${w}" height="${h}"><defs><linearGradient id="g" x1="0" x2="1"><stop offset="0%" stop-color="white"/><stop offset="88%" stop-color="white"/><stop offset="100%" stop-color="black"/></linearGradient></defs><rect width="${w}" height="${h}" fill="url(#g)"/></svg>`
    );
    await sharp(maskSvg).png().toFile(config.ninaMaskPath);
    return {
      x: nina.x,
      y: nina.y,
      w,
      h,
      method: 'layout-fallback',
    };
  }
}

async function prepareImageLayers() {
  const layout = fs.existsSync(config.layoutPath)
    ? JSON.parse(fs.readFileSync(config.layoutPath, 'utf8'))
    : defaultLayout();

  if (!fs.existsSync(config.sourceImage)) {
    await composeScene();
  } else if (!fs.existsSync(config.layoutPath)) {
    await composeScene();
  }

  const current = JSON.parse(fs.readFileSync(config.layoutPath, 'utf8'));
  const ninaBox = await detectAndCropNina(current);
  current.ninaDetected = ninaBox;
  fs.writeFileSync(config.layoutPath, JSON.stringify(current, null, 2));
  fs.copyFileSync(config.ninaCropPath, path.join(config.assetsDir, 'nina-crop.png'));
  return current;
}

module.exports = { prepareImageLayers, detectAndCropNina, runPython };
