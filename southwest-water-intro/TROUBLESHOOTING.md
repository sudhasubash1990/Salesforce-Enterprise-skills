# Troubleshooting

## Missing source image

**Symptom:** pipeline builds a fixture still instead of the client artwork.

**Fix:** copy the official composition to `assets/southwest-water-customer-journey.png` and re-run `npm run generate`. Do not AI-regenerate logos or labels.

## “AI video provider credentials are not configured…”

Add `HEYGEN_API_KEY` (preferred) or `DID_API_KEY` / `REPLICATE_API_TOKEN` to `.env`.

Without keys, `AI_VIDEO_PROVIDER=auto` falls back to the local viseme renderer. That path is real lip animation (mouth shapes from audio + visemes), not a Ken Burns zoom, but it is **not** HeyGen-grade identity lock. Use HeyGen/D-ID for the client cut.

## HeyGen / D-ID rejects the crop

- Use a chest-up crop of Nina only (`temp/nina-crop.png`).
- Avoid sending the full poster (Alex/Harvey would be animated).
- Retry is automatic (3×, exponential backoff). Audio is kept in `temp/audio.wav` if lip-sync fails.

## Wrong voice / American accent

Set `EDGE_TTS_VOICE=en-GB-SoniaNeural` (or `en-GB-LibbyNeural`) and `TTS_PROVIDER=edge`. Do not use `en-US-*`.

## Lip motion continues after speech

Regenerate audio (`rm temp/audio.wav`) so trailing silence is trimmed, then re-run generate. The local renderer scales mouth opening by RMS and closes below a silence threshold.

## Alex or Harvey appear to speak

They must remain on the background still. Confirm `avatarGenerator` received `nina-crop.png`, not the full poster. Re-run `npm run preview` and inspect `output/nina-talking.mp4`.

## Face warp / extra teeth

Switch `AI_VIDEO_PROVIDER=heygen` and `HEYGEN_ENGINE=avatar_iv` with `expressiveness` low. Do not use generic image-to-video models that move the whole frame.

## ffmpeg concat / TTS errors

Install ffmpeg with libmp3lame. The Edge TTS step concatenates paragraph takes with 420 ms silence so the wording stays verbatim.

## Validation exit code 2

Read `output/validation-report.json`. Camera motion can move Alex/Harvey out of a sampled frame; that is expected. Failures on duration, clipping, or missing audio should be treated as blockers.

## Preview is fine, full render is slow

Full narration is ~60–75 s. Local viseme is CPU-bound. Cloud providers run asynchronously; the CLI polls until the MP4 URL is ready (timeout 12 minutes).
