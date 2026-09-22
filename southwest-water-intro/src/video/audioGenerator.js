'use strict';

const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const { config } = require('../config/config');
const logger = require('../utils/logger');
const { withRetry } = require('../utils/retry');

function spawnCapture(cmd, args) {
  return new Promise((resolve, reject) => {
    const proc = spawn(cmd, args, { stdio: ['ignore', 'pipe', 'pipe'] });
    let out = '';
    let err = '';
    proc.stdout.on('data', (d) => {
      out += d.toString();
    });
    proc.stderr.on('data', (d) => {
      err += d.toString();
    });
    proc.on('close', (code) => {
      if (code !== 0) reject(new Error(err || `${cmd} exited ${code}`));
      else resolve(out);
    });
  });
}

async function ffmpegToWav48k(input, output) {
  await spawnCapture('ffmpeg', [
    '-y',
    '-i',
    input,
    '-ac',
    '2',
    '-ar',
    String(config.video.sampleRate),
    '-c:a',
    'pcm_s16le',
    output,
  ]);
}

function wrapSsml(transcript, voice) {
  const paragraphs = transcript
    .split(/\n\s*\n/)
    .map((p) => p.trim())
    .filter(Boolean)
    .map((p) => `<p>${p.replace(/&/g, '&amp;').replace(/</g, '&lt;')}</p>`)
    .join('<break time="420ms"/>');
  return `<speak version="1.0" xml:lang="en-GB">${paragraphs}</speak>`;
}

async function generateEdgeTts(transcript, wavPath) {
  const script = path.join(__dirname, '../python/tts_edge.py');
  const ssmlPath = path.join(config.tempDir, 'narration.ssml');
  const mp3Path = path.join(config.tempDir, 'audio.mp3');
  fs.writeFileSync(ssmlPath, wrapSsml(transcript), 'utf8');
  await spawnCapture('python3', [
    script,
    '--voice',
    config.tts.edgeVoice,
    '--rate',
    config.tts.edgeRate,
    '--ssml',
    ssmlPath,
    '--out',
    mp3Path,
  ]);
  await ffmpegToWav48k(mp3Path, wavPath);
  logger.info('Generated Edge TTS audio', { voice: config.tts.edgeVoice, wavPath });
  return wavPath;
}

async function generateElevenLabs(transcript, wavPath) {
  if (!config.tts.elevenKey || !config.tts.elevenVoice) {
    throw new Error('ElevenLabs is selected but ELEVENLABS_API_KEY / ELEVENLABS_VOICE_ID are missing.');
  }
  const response = await fetch(
    `https://api.elevenlabs.io/v1/text-to-speech/${config.tts.elevenVoice}`,
    {
      method: 'POST',
      headers: {
        'xi-api-key': config.tts.elevenKey,
        'Content-Type': 'application/json',
        Accept: 'audio/mpeg',
      },
      body: JSON.stringify({
        text: transcript,
        model_id: 'eleven_multilingual_v2',
        voice_settings: {
          stability: 0.55,
          similarity_boost: 0.75,
          style: 0.2,
          use_speaker_boost: true,
        },
      }),
    }
  );
  if (!response.ok) {
    throw new Error(`ElevenLabs TTS failed (${response.status})`);
  }
  const mp3Path = path.join(config.tempDir, 'audio.mp3');
  fs.writeFileSync(mp3Path, Buffer.from(await response.arrayBuffer()));
  await ffmpegToWav48k(mp3Path, wavPath);
  return wavPath;
}

async function generateAudio(transcript, { outputPath = config.audioPath } = {}) {
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  if (config.tts.provider === 'elevenlabs') {
    return withRetry(() => generateElevenLabs(transcript, outputPath), { label: 'elevenlabs-tts' });
  }
  return withRetry(() => generateEdgeTts(transcript, outputPath), { label: 'edge-tts' });
}

async function probeDuration(filePath) {
  const out = await spawnCapture('ffprobe', [
    '-v',
    'error',
    '-show_entries',
    'format=duration',
    '-of',
    'default=noprint_wrappers=1:nokey=1',
    filePath,
  ]);
  return Number.parseFloat(out.trim());
}

module.exports = { generateAudio, probeDuration, ffmpegToWav48k };
