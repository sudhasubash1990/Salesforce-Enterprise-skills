'use strict';

const fs = require('fs');
const path = require('path');
const sharp = require('sharp');
const { config, ensureDirs } = require('../config/config');
const { MOVE_IN_ICONS, SELF_SERVICE_ICONS } = require('../config/transcript');
const logger = require('../utils/logger');

const W = 1920;
const H = 1080;

function escapeXml(text) {
  return String(text)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function iconGlyph(label) {
  const map = {
    Call: '☎',
    Search: '⌕',
    'Create Customer': '＋',
    'Property Validation': '⌂',
    'Move-in': '→',
    'Log Case': '☑',
    'Self-Service Portal': '◉',
    'Meter Reading': '▦',
    'View Bill': '▤',
    'Pay Online': '£',
  };
  return map[label] || '●';
}

function overlaySvg(layout) {
  const moveIcons = layout.icons.filter((i) => i.group === 'movein');
  const selfIcons = layout.icons.filter((i) => i.group === 'selfservice');

  const iconSvg = (icon) => `
    <g>
      <rect x="${icon.x}" y="${icon.y}" width="${icon.w}" height="${icon.h}" rx="16" fill="rgba(8,28,48,0.72)" stroke="rgba(120,210,230,0.55)" stroke-width="1.5"/>
      <circle cx="${icon.x + icon.w / 2}" cy="${icon.y + 38}" r="18" fill="rgba(0,161,224,0.18)" stroke="#7ad7ea" stroke-width="1.5"/>
      <text x="${icon.x + icon.w / 2}" y="${icon.y + 44}" text-anchor="middle" font-size="16" fill="#e8fbff" font-family="Segoe UI, Helvetica, Arial, sans-serif">${escapeXml(iconGlyph(icon.label))}</text>
      <text x="${icon.x + icon.w / 2}" y="${icon.y + 78}" text-anchor="middle" font-size="13" fill="#f4fbff" font-family="Segoe UI, Helvetica, Arial, sans-serif">${escapeXml(icon.label)}</text>
    </g>`;

  return Buffer.from(`<?xml version="1.0" encoding="UTF-8"?>
<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="scrim" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#041526" stop-opacity="0.28"/>
      <stop offset="55%" stop-color="#062033" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#021018" stop-opacity="0.72"/>
    </linearGradient>
  </defs>
  <rect width="${W}" height="${H}" fill="url(#scrim)"/>
  <text x="48" y="52" font-size="22" font-weight="700" fill="#F4FBFF" font-family="Segoe UI, Helvetica, Arial, sans-serif">Southwest Water</text>
  <text x="250" y="52" font-size="16" fill="#7AD7EA" font-family="Segoe UI, Helvetica, Arial, sans-serif">×</text>
  <text x="272" y="52" font-size="22" font-weight="700" fill="#00A1E0" font-family="Segoe UI, Helvetica, Arial, sans-serif">Salesforce</text>
  <text x="48" y="82" font-size="15" fill="#C9E7F2" font-family="Segoe UI, Helvetica, Arial, sans-serif">Customer journey demonstration  ·  Contact centre live path  ·  Self-service follow-through</text>
  <text x="${layout.nina.x + 24}" y="${layout.nina.y + layout.nina.h - 28}" font-size="28" font-weight="700" fill="#FFFFFF" font-family="Segoe UI, Helvetica, Arial, sans-serif">Nina</text>
  <text x="${layout.nina.x + 24}" y="${layout.nina.y + layout.nina.h - 4}" font-size="16" fill="#B8D7E6" font-family="Segoe UI, Helvetica, Arial, sans-serif">Demo Guide</text>
  <rect x="${layout.alex.x}" y="${layout.alex.y}" width="${layout.alex.w}" height="${layout.alex.h}" rx="22" fill="none" stroke="rgba(122,215,234,0.35)" stroke-width="2"/>
  <text x="${layout.alex.x + 18}" y="${layout.alex.y + layout.alex.h - 36}" font-size="20" font-weight="700" fill="#FFFFFF" font-family="Segoe UI, Helvetica, Arial, sans-serif">Alex</text>
  <text x="${layout.alex.x + 18}" y="${layout.alex.y + layout.alex.h - 14}" font-size="14" fill="#C9E7F2" font-family="Segoe UI, Helvetica, Arial, sans-serif">Contact Centre Advisor</text>
  <text x="${layout.alex.x + 18}" y="${layout.alex.y + layout.alex.h + 4}" font-size="13" fill="#7AD7EA" font-family="Segoe UI, Helvetica, Arial, sans-serif">Southwest Water</text>
  <rect x="${layout.harvey.x}" y="${layout.harvey.y}" width="${layout.harvey.w}" height="${layout.harvey.h}" rx="22" fill="none" stroke="rgba(122,215,234,0.35)" stroke-width="2"/>
  <text x="${layout.harvey.x + 18}" y="${layout.harvey.y + layout.harvey.h - 32}" font-size="20" font-weight="700" fill="#FFFFFF" font-family="Segoe UI, Helvetica, Arial, sans-serif">Harvey Spector</text>
  <text x="${layout.harvey.x + 18}" y="${layout.harvey.y + layout.harvey.h - 10}" font-size="14" fill="#C9E7F2" font-family="Segoe UI, Helvetica, Arial, sans-serif">Customer</text>
  <text x="${layout.icons[0].x}" y="528" font-size="14" font-weight="700" fill="#7AD7EA" font-family="Segoe UI, Helvetica, Arial, sans-serif">MOVE-IN JOURNEY</text>
  ${moveIcons.map(iconSvg).join('')}
  <text x="${selfIcons[0].x}" y="778" font-size="14" font-weight="700" fill="#7AD7EA" font-family="Segoe UI, Helvetica, Arial, sans-serif">SELF-SERVICE JOURNEY</text>
  ${selfIcons.map(iconSvg).join('')}
</svg>`);
}

function defaultLayout() {
  const nina = { x: 36, y: 96, w: 680, h: 940 };
  const alex = { x: 760, y: 110, w: 540, h: 380 };
  const harvey = { x: 1330, y: 110, w: 540, h: 380 };
  const icons = [];
  const iconW = 178;
  const iconH = 100;
  MOVE_IN_ICONS.forEach((label, i) => {
    icons.push({
      id: label.toLowerCase().replace(/\s+/g, '-'),
      label,
      group: 'movein',
      x: 760 + i * (iconW + 14),
      y: 548,
      w: iconW,
      h: iconH,
    });
  });
  SELF_SERVICE_ICONS.forEach((label, i) => {
    icons.push({
      id: label.toLowerCase().replace(/\s+/g, '-'),
      label,
      group: 'selfservice',
      x: 760 + i * (iconW + 14),
      y: 798,
      w: iconW,
      h: iconH,
    });
  });
  return { width: W, height: H, nina, alex, harvey, icons };
}

async function fitCover(input, width, height) {
  return sharp(input)
    .rotate()
    .resize(width, height, { fit: 'cover', position: 'top' })
    .png()
    .toBuffer();
}

async function composeScene({ force = false } = {}) {
  ensureDirs();
  const officialExists = fs.existsSync(config.sourceImage);
  const layout = defaultLayout();

  if (officialExists && !force) {
    logger.info('Using supplied source image; composing overlay-safe layout metadata only', {
      path: config.sourceImage,
    });
    const meta = await sharp(config.sourceImage).metadata();
    if (meta.width !== W || meta.height !== H) {
      const resized = path.join(config.tempDir, 'source-1920x1080.png');
      await sharp(config.sourceImage)
        .resize(W, H, { fit: 'cover', position: 'centre' })
        .png()
        .toFile(resized);
      await sharp(resized).toFile(config.sourceImage.replace(/\.png$/, '-working.png'));
      layout.source = config.sourceImage;
      layout.working = resized;
    } else {
      layout.source = config.sourceImage;
      layout.working = config.sourceImage;
    }
    fs.writeFileSync(config.layoutPath, JSON.stringify(layout, null, 2));
    return layout;
  }

  logger.info('Official journey still not found — building branded composite from portrait layers (vector text, not AI text).');

  const bg = await sharp(config.backgroundSource)
    .resize(W, H, { fit: 'cover' })
    .modulate({ brightness: 0.72, saturation: 0.85 })
    .toBuffer();

  const ninaBuf = await fitCover(config.ninaSource, layout.nina.w, layout.nina.h);
  const alexBuf = await fitCover(config.alexSource, layout.alex.w - 24, layout.alex.h - 88);
  const harveyBuf = await fitCover(config.harveySource, layout.harvey.w - 24, layout.harvey.h - 88);

  const rounded = (buf, w, h, radius) =>
    sharp(buf)
      .composite([
        {
          input: Buffer.from(
            `<svg width="${w}" height="${h}"><rect x="0" y="0" width="${w}" height="${h}" rx="${radius}" fill="white"/></svg>`
          ),
          blend: 'dest-in',
        },
      ])
      .png()
      .toBuffer();

  const ninaRound = await rounded(ninaBuf, layout.nina.w, layout.nina.h, 28);
  const alexRound = await rounded(alexBuf, layout.alex.w - 24, layout.alex.h - 88, 18);
  const harveyRound = await rounded(harveyBuf, layout.harvey.w - 24, layout.harvey.h - 88, 18);

  const overlay = overlaySvg(layout);

  await sharp(bg)
    .composite([
      { input: ninaRound, left: layout.nina.x, top: layout.nina.y },
      { input: alexRound, left: layout.alex.x + 12, top: layout.alex.y + 12 },
      { input: harveyRound, left: layout.harvey.x + 12, top: layout.harvey.y + 12 },
      { input: overlay, left: 0, top: 0 },
    ])
    .png()
    .toFile(config.sourceImage);

  layout.source = config.sourceImage;
  layout.working = config.sourceImage;
  layout.constructed = true;
  fs.writeFileSync(config.layoutPath, JSON.stringify(layout, null, 2));
  logger.info('Wrote scene still', { path: config.sourceImage });
  return layout;
}

if (require.main === module) {
  composeScene({ force: process.argv.includes('--force') }).catch((error) => {
    logger.error('Scene compose failed', { message: error.message });
    process.exit(1);
  });
}

module.exports = { composeScene, defaultLayout };
