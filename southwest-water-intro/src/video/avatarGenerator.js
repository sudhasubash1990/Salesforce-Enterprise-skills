'use strict';

const fs = require('fs');
const path = require('path');
const { config, hasCloudVideoCredentials, missingCredentialsMessage } = require('../config/config');
const logger = require('../utils/logger');
const { withRetry } = require('../utils/retry');

async function downloadFile(url, dest) {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Download failed ${response.status}`);
  fs.writeFileSync(dest, Buffer.from(await response.arrayBuffer()));
}

function toDataUrl(filePath, mime) {
  const b64 = fs.readFileSync(filePath).toString('base64');
  return `data:${mime};base64,${b64}`;
}

async function pollUntil(fn, { timeoutMs = 12 * 60 * 1000, intervalMs = 4000, label = 'job' } = {}) {
  const start = Date.now();
  while (Date.now() - start < timeoutMs) {
    const result = await fn();
    if (result.done) return result.value;
    await new Promise((r) => setTimeout(r, intervalMs));
  }
  throw new Error(`${label} timed out`);
}

async function heygenUpload(apiKey, filePath, contentType) {
  const body = fs.readFileSync(filePath);
  const response = await fetch(`${config.heygen.baseUrl}/v1/asset`, {
    method: 'POST',
    headers: {
      'x-api-key': apiKey,
      'Content-Type': contentType,
    },
    body,
  });
  const json = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(`HeyGen asset upload failed (${response.status}): ${json.message || json.error || 'unknown'}`);
  }
  return json.data?.id || json.id || json.asset_id;
}

async function generateHeyGen({ image, audio, transcript, outputPath }) {
  const apiKey = config.heygen.apiKey;
  if (!apiKey) throw new Error(missingCredentialsMessage());

  return withRetry(
    async () => {
      const imageId = await heygenUpload(apiKey, image, 'image/png');
      const audioId = audio ? await heygenUpload(apiKey, audio, 'audio/wav') : null;

      const payload = {
        type: 'image',
        title: 'Southwest Water Nina intro',
        engine: config.heygen.engine,
        expressiveness: 'low',
        image: { type: 'asset_id', asset_id: imageId },
        resolution: '1080p',
        aspect_ratio: '9:16',
      };
      if (audioId) {
        payload.audio_asset_id = audioId;
      } else {
        payload.script = transcript;
        payload.voice_id = config.heygen.voiceId;
      }

      const created = await fetch(`${config.heygen.baseUrl}/v3/videos`, {
        method: 'POST',
        headers: {
          'x-api-key': apiKey,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });
      const createdJson = await created.json().catch(() => ({}));
      if (!created.ok) {
        logger.error('HeyGen create video rejected', { status: created.status, body: createdJson });
        throw new Error(`HeyGen create failed (${created.status})`);
      }
      const videoId = createdJson.data?.video_id || createdJson.data?.id || createdJson.video_id;
      logger.info('HeyGen job created', { videoId });

      const finished = await pollUntil(
        async () => {
          const statusRes = await fetch(`${config.heygen.baseUrl}/v3/videos/${videoId}`, {
            headers: { 'x-api-key': apiKey },
          });
          const statusJson = await statusRes.json();
          const status = statusJson.data?.status || statusJson.status;
          if (status === 'failed' || status === 'error') {
            throw new Error(`HeyGen render failed: ${statusJson.data?.error || 'unknown'}`);
          }
          if (status === 'completed' || status === 'success') {
            return {
              done: true,
              value: statusJson.data?.video_url || statusJson.data?.url || statusJson.video_url,
            };
          }
          return { done: false };
        },
        { label: 'heygen-video' }
      );

      await downloadFile(finished, outputPath);
      return outputPath;
    },
    { label: 'heygen-talking-avatar' }
  );
}

function didAuthHeader() {
  const token = config.did.apiSecret
    ? Buffer.from(`${config.did.apiKey}:${config.did.apiSecret}`).toString('base64')
    : Buffer.from(`${config.did.apiKey}:`).toString('base64');
  return `Basic ${token}`;
}

async function generateDid({ image, audio, transcript, outputPath }) {
  if (!config.did.apiKey) throw new Error(missingCredentialsMessage());
  return withRetry(
    async () => {
      const payload = {
        source_url: toDataUrl(image, 'image/png'),
        config: {
          stitch: true,
          result_format: 'mp4',
          fluent: true,
          pad_audio: 0,
        },
      };
      if (audio && fs.existsSync(audio)) {
        payload.script = {
          type: 'audio',
          audio_url: toDataUrl(audio, 'audio/wav'),
        };
      } else {
        payload.script = {
          type: 'text',
          input: transcript,
          provider: { type: 'microsoft', voice_id: 'en-GB-SoniaNeural' },
        };
      }

      const created = await fetch(`${config.did.baseUrl}/talks`, {
        method: 'POST',
        headers: {
          Authorization: didAuthHeader(),
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });
      const createdJson = await created.json().catch(() => ({}));
      if (!created.ok) {
        logger.error('D-ID create talk rejected', { status: created.status, body: createdJson });
        throw new Error(`D-ID create failed (${created.status})`);
      }
      const id = createdJson.id;
      logger.info('D-ID job created', { id });

      const url = await pollUntil(
        async () => {
          const statusRes = await fetch(`${config.did.baseUrl}/talks/${id}`, {
            headers: { Authorization: didAuthHeader() },
          });
          const json = await statusRes.json();
          if (json.status === 'error' || json.status === 'rejected') {
            throw new Error(`D-ID render failed: ${json.error?.description || json.status}`);
          }
          if (json.status === 'done') return { done: true, value: json.result_url };
          return { done: false };
        },
        { label: 'did-talk' }
      );
      await downloadFile(url, outputPath);
      return outputPath;
    },
    { label: 'did-talking-avatar' }
  );
}

async function generateReplicate({ image, audio, outputPath }) {
  if (!config.replicate.token) throw new Error(missingCredentialsMessage());
  return withRetry(
    async () => {
      const imageData = toDataUrl(image, 'image/png');
      const audioData = toDataUrl(audio, 'audio/wav');
      const created = await fetch('https://api.replicate.com/v1/predictions', {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${config.replicate.token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: config.replicate.model,
          input: {
            source_image: imageData,
            driven_audio: audioData,
            enhancer: 'gfpgan',
            preprocess: 'crop',
            still_mode: true,
            face_enhancer: 'gfpgan',
          },
        }),
      });
      const createdJson = await created.json();
      if (!created.ok) {
        logger.error('Replicate prediction rejected', { status: created.status, body: createdJson });
        throw new Error(`Replicate create failed (${created.status})`);
      }
      const url = await pollUntil(
        async () => {
          const statusRes = await fetch(createdJson.urls.get, {
            headers: { Authorization: `Bearer ${config.replicate.token}` },
          });
          const json = await statusRes.json();
          if (json.status === 'failed' || json.status === 'canceled') {
            throw new Error(`Replicate failed: ${json.error || json.status}`);
          }
          if (json.status === 'succeeded') {
            const output = Array.isArray(json.output) ? json.output[0] : json.output;
            return { done: true, value: output };
          }
          return { done: false };
        },
        { label: 'replicate-sadtalker' }
      );
      await downloadFile(url, outputPath);
      return outputPath;
    },
    { label: 'replicate-talking-avatar' }
  );
}

async function generateLocal({ image, audio, transcript, outputPath }) {
  const { runPython } = require('../video/imageProcessor');
  const script = path.join(__dirname, '../python/local_viseme_avatar.py');
  logger.info('Generating talking avatar with local viseme renderer (IMAGE + AUDIO → talking person).');
  await runPython(script, [
    '--image',
    image,
    '--audio',
    audio,
    '--transcript',
    transcript,
    '--out',
    outputPath,
    '--fps',
    String(config.video.fps),
  ]);
  if (!fs.existsSync(outputPath)) {
    throw new Error('Local viseme renderer did not produce an output file.');
  }
  return outputPath;
}

/**
 * Provider-independent talking-avatar contract.
 */
async function generateTalkingAvatar({ image, audio, transcript, voice, outputPath }) {
  const target = outputPath || config.ninaTalkingPath;
  fs.mkdirSync(path.dirname(target), { recursive: true });
  const provider = config.provider;
  const args = { image, audio, transcript, voice, outputPath: target };

  const chain = [];
  if (provider === 'heygen') chain.push(['heygen', generateHeyGen]);
  else if (provider === 'did') chain.push(['did', generateDid]);
  else if (provider === 'replicate') chain.push(['replicate', generateReplicate]);
  else if (provider === 'local') chain.push(['local', generateLocal]);
  else {
    if (config.heygen.apiKey) chain.push(['heygen', generateHeyGen]);
    if (config.did.apiKey) chain.push(['did', generateDid]);
    if (config.replicate.token) chain.push(['replicate', generateReplicate]);
    chain.push(['local', generateLocal]);
  }

  if (!hasCloudVideoCredentials() && provider !== 'local' && provider !== 'auto') {
    throw new Error(missingCredentialsMessage());
  }

  let lastError;
  for (const [name, fn] of chain) {
    try {
      logger.info('Talking-avatar provider starting', { provider: name });
      const result = await fn(args);
      logger.info('Talking-avatar provider succeeded', { provider: name, outputPath: result });
      return { provider: name, outputPath: result };
    } catch (error) {
      lastError = error;
      logger.error('Talking-avatar provider failed', { provider: name, message: error.message });
      if (name !== 'local' && fs.existsSync(audio)) {
        logger.info('Preserving generated audio after lip-sync failure', { audio });
      }
    }
  }
  throw lastError || new Error(missingCredentialsMessage());
}

module.exports = {
  generateTalkingAvatar,
  generateHeyGen,
  generateDid,
  generateReplicate,
  generateLocal,
};
