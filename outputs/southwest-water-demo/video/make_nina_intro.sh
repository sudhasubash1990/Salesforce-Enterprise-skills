#!/usr/bin/env bash
# Reproduce nina-intro.mkv: neural TTS (edge-tts) + Wav2Lip (GAN) lip-sync on a static image,
# then GFPGAN face restoration + mouth-only compositing (composite_mouth.py).
# Requirements: python3, ffmpeg, git; CPU is sufficient (~2 min Wav2Lip + ~30 min GFPGAN for 60 s).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
W2L=/tmp/Wav2Lip
GFP=/tmp/gfpgan_w

pip install --quiet --index-url https://download.pytorch.org/whl/cpu torch torchvision
pip install --quiet opencv-python-headless edge-tts librosa numba scipy tqdm gfpgan basicsr facexlib
[ -d "$W2L" ] || git clone --depth 1 https://github.com/Rudrabha/Wav2Lip.git "$W2L"

# Model weights (community mirrors of the official checkpoints)
[ -f "$W2L/checkpoints/wav2lip_gan.pth" ] || curl -sL --fail -o "$W2L/checkpoints/wav2lip_gan.pth" \
  https://huggingface.co/numz/wav2lip_studio/resolve/main/Wav2lip/wav2lip_gan.pth
[ -f "$W2L/face_detection/detection/sfd/s3fd.pth" ] || curl -sL --fail -o "$W2L/face_detection/detection/sfd/s3fd.pth" \
  https://huggingface.co/camenduru/Wav2Lip/resolve/main/face_detection/detection/sfd/s3fd.pth
mkdir -p "$GFP"
[ -f "$GFP/GFPGANv1.4.pth" ] || curl -sL --fail -o "$GFP/GFPGANv1.4.pth" \
  https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth

# Compatibility patches for current torch / torchvision / librosa
DEG="$(python3 -c 'import importlib.util,os;print(os.path.join(os.path.dirname(importlib.util.find_spec("basicsr").origin),"data","degradations.py"))')"
sed -i 's/from torchvision.transforms.functional_tensor import rgb_to_grayscale/from torchvision.transforms.functional import rgb_to_grayscale/' "$DEG"
sed -i 's/torch.load(checkpoint_path)$/torch.load(checkpoint_path, weights_only=False)/' "$W2L/inference.py"
sed -i 's/checkpoint = torch.load(checkpoint_path,$/checkpoint = torch.load(checkpoint_path, weights_only=False,/' "$W2L/inference.py"
sed -i 's/torch.load(path_to_detector)$/torch.load(path_to_detector, weights_only=False)/' "$W2L/face_detection/detection/sfd/sfd_detector.py"
sed -i 's/librosa.filters.mel(hp.sample_rate, hp.n_fft, n_mels=hp.num_mels,/librosa.filters.mel(sr=hp.sample_rate, n_fft=hp.n_fft, n_mels=hp.num_mels,/' "$W2L/audio.py"

# 1. Voice
python3 -m edge_tts --voice en-GB-SoniaNeural --rate=-4% -f "$HERE/nina-intro-transcript.txt" --write-media "$HERE/nina-intro-voice.mp3"
ffmpeg -y -loglevel error -i "$HERE/nina-intro-voice.mp3" -af "adelay=700|700,apad=pad_dur=1.0" -ac 1 -ar 16000 -c:a pcm_s16le "$HERE/nina-intro-voice.wav"

# 2. Lip-sync
( cd "$W2L" && python3 inference.py --checkpoint_path checkpoints/wav2lip_gan.pth \
    --face "$HERE/nina-source.png" --audio "$HERE/nina-intro-voice.wav" \
    --outfile /tmp/nina_w2l.mp4 --pads 0 15 0 0 --fps 25 --wav2lip_batch_size 64 --face_det_batch_size 4 )

# 3. GFPGAN restoration + temporal smoothing + mouth-only composite -> final MKV (H.264 + AAC, no subtitles).
# Wav2Lip regenerates the whole face at 96x96 (soft, shimmering, smeared teeth). GFPGAN restores the
# generated face crop; only the lips/jaw ellipse is blended back so the original high-res face stays
# perfectly stable. --mouth (cx,cy,ax,ay) and --face (cx,cy,half) are source-image pixels for nina-source.png.
( cd /tmp && python3 "$HERE/composite_mouth.py" --source "$HERE/nina-source.png" --wav2lip /tmp/nina_w2l.mp4 \
  --audio "$HERE/nina-intro-voice.wav" --out "$HERE/nina-intro.mkv" \
  --mouth 380,266,44,30 --feather 6 --gfpgan "$GFP/GFPGANv1.4.pth" --face 380,215,150 --gfpgan-weight 0.5 --smooth 0.2 )
echo "wrote $HERE/nina-intro.mkv"
