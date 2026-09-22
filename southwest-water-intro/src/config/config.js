'use strict';

const fs = require('fs');
const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '../../.env') });

const ROOT = path.join(__dirname, '../..');

function env(name, fallback = '') {
  const value = process.env[name];
  return value === undefined || value === '' ? fallback : value;
}

function envInt(name, fallback) {
  const value = Number.parseInt(env(name, String(fallback)), 10);
  return Number.isFinite(value) ? value : fallback;
}

const config = {
  root: ROOT,
  assetsDir: path.join(ROOT, 'assets'),
  outputDir: path.join(ROOT, 'output'),
  tempDir: path.join(ROOT, 'temp'),
  sourceImage: path.join(ROOT, 'assets/southwest-water-customer-journey.png'),
  ninaSource: path.join(ROOT, 'assets/nina-source.png'),
  alexSource: path.join(ROOT, 'assets/alex-advisor.png'),
  harveySource: path.join(ROOT, 'assets/harvey-customer.png'),
  backgroundSource: path.join(ROOT, 'assets/corporate-bg.png'),
  layoutPath: path.join(ROOT, 'temp/layout.json'),
  ninaCropPath: path.join(ROOT, 'temp/nina-crop.png'),
  ninaMaskPath: path.join(ROOT, 'temp/nina-mask.png'),
  audioPath: path.join(ROOT, 'temp/audio.wav'),
  ninaTalkingPath: path.join(ROOT, 'output/nina-talking.mp4'),
  compositedPath: path.join(ROOT, 'temp/composited.mp4'),
  finalOutput: path.join(ROOT, 'output/southwest-water-customer-journey-intro.mp4'),
  validationReport: path.join(ROOT, 'output/validation-report.json'),
  previewOutput: path.join(ROOT, 'output/preview.mp4'),
  provider: env('AI_VIDEO_PROVIDER', 'auto').toLowerCase(),
  apiKey: env('AI_VIDEO_API_KEY'),
  heygen: {
    apiKey: env('HEYGEN_API_KEY', env('AI_VIDEO_API_KEY')),
    voiceId: env('HEYGEN_VOICE_ID'),
    engine: env('HEYGEN_ENGINE', 'avatar_iv'),
    baseUrl: 'https://api.heygen.com',
  },
  did: {
    apiKey: env('DID_API_KEY', env('AI_VIDEO_API_KEY')),
    apiSecret: env('DID_API_SECRET'),
    baseUrl: 'https://api.d-id.com',
  },
  replicate: {
    token: env('REPLICATE_API_TOKEN'),
    model: env('REPLICATE_MODEL', 'cjwbw/sadtalker'),
  },
  tts: {
    provider: env('TTS_PROVIDER', 'edge').toLowerCase(),
    edgeVoice: env('EDGE_TTS_VOICE', 'en-GB-SoniaNeural'),
    edgeRate: env('EDGE_TTS_RATE', '-10%'),
    elevenKey: env('ELEVENLABS_API_KEY'),
    elevenVoice: env('ELEVENLABS_VOICE_ID'),
    azureKey: env('AZURE_SPEECH_KEY'),
    azureRegion: env('AZURE_SPEECH_REGION'),
  },
  video: {
    width: envInt('OUTPUT_WIDTH', 1920),
    height: envInt('OUTPUT_HEIGHT', 1080),
    fps: envInt('OUTPUT_FPS', 30),
    codec: env('VIDEO_CODEC', 'libx264'),
    audioCodec: env('AUDIO_CODEC', 'aac'),
    sampleRate: envInt('AUDIO_SAMPLE_RATE', 48000),
  },
  previewSeconds: envInt('PREVIEW_SECONDS', 12),
};

function ensureDirs() {
  for (const dir of [config.assetsDir, config.outputDir, config.tempDir]) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

function hasCloudVideoCredentials() {
  return Boolean(config.heygen.apiKey || config.did.apiKey || config.replicate.token || config.apiKey);
}

function missingCredentialsMessage() {
  return 'AI video provider credentials are not configured. Add the required API key to .env.';
}

module.exports = {
  config,
  ensureDirs,
  hasCloudVideoCredentials,
  missingCredentialsMessage,
};
