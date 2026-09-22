'use strict';

const { SCENES } = require('../config/transcript');

function lerp(a, b, t) {
  return a + (b - a) * t;
}

function clamp(v, min, max) {
  return Math.max(min, Math.min(max, v));
}

function sceneAt(timeSec, duration) {
  const scaled = SCENES.map((scene) => {
    const start = (scene.startSec / 67) * duration;
    const end = (scene.endSec / 67) * duration;
    return { ...scene, start, end };
  });
  return scaled.find((s) => timeSec >= s.start && timeSec < s.end) || scaled[scaled.length - 1];
}

function cameraWindow(layout, scene, timeSec, duration) {
  const nina = layout.ninaDetected || layout.nina;
  const alex = layout.alex;
  const harvey = layout.harvey;
  const w = layout.width;
  const h = layout.height;

  const full = { x: 0, y: 0, w, h, zoom: 1 };
  const ninaFocus = {
    x: Math.max(0, nina.x - 40),
    y: Math.max(0, nina.y - 20),
    w: Math.min(w, nina.w + 380),
    h,
    zoom: 1.06,
  };
  const journeyFocus = { x: 420, y: 80, w: w - 420, h: h - 80, zoom: 1.08 };
  const alexFocus = {
    x: Math.max(0, alex.x - 80),
    y: Math.max(0, alex.y - 40),
    w: Math.min(w - alex.x + 80, alex.w + 200),
    h: Math.min(h, alex.h + 160),
    zoom: 1.12,
  };
  const harveyFocus = {
    x: Math.max(0, harvey.x - 80),
    y: Math.max(0, harvey.y - 40),
    w: Math.min(w - harvey.x + 80, harvey.w + 200),
    h: Math.min(h, harvey.h + 180),
    zoom: 1.12,
  };
  const selfFocus = { x: 520, y: 520, w: w - 540, h: 520, zoom: 1.1 };

  let from = full;
  let to = ninaFocus;
  if (scene.camera === 'nina') {
    from = full;
    to = ninaFocus;
  } else if (scene.camera === 'journey') {
    from = ninaFocus;
    to = journeyFocus;
  } else if (scene.camera === 'cast') {
    const mid = (scene.start + scene.end) / 2;
    if (timeSec < mid) {
      from = journeyFocus;
      to = alexFocus;
    } else {
      from = alexFocus;
      to = harveyFocus;
    }
  } else if (scene.camera === 'selfservice') {
    from = journeyFocus;
    to = selfFocus;
  } else if (scene.camera === 'nina-end') {
    from = selfFocus;
    to = ninaFocus;
  }

  const t = clamp((timeSec - scene.start) / Math.max(0.01, scene.end - scene.start), 0, 1);
  const eased = t * t * (3 - 2 * t);
  return {
    x: lerp(from.x, to.x, eased),
    y: lerp(from.y, to.y, eased),
    w: lerp(from.w, to.w, eased),
    h: lerp(from.h, to.h, eased),
    zoom: lerp(from.zoom || 1, to.zoom || 1, eased),
    scene,
  };
}

function activeIconIndex(layout, scene, timeSec) {
  if (!scene.highlight) return -1;
  const group = scene.highlight === 'cast' ? null : scene.highlight;
  if (!group) return -1;
  const icons = layout.icons.filter((i) => i.group === group);
  if (!icons.length) return -1;
  const t = clamp((timeSec - scene.start) / Math.max(0.01, scene.end - scene.start), 0, 1);
  return Math.min(icons.length - 1, Math.floor(t * icons.length));
}

module.exports = {
  sceneAt,
  cameraWindow,
  activeIconIndex,
  lerp,
};
