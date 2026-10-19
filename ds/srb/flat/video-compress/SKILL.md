---
name: video-compress
description: "Use when Compress video files using ffmpeg with optimized presets. Use when the user asks to compress, shrink, or re-encode a video file, or mentions: covers video, compress, 비디오, 압축, compression"
metadata:
  holon-triggers: |
    make this video smaller
    re-encode a video file
---

---
name: video-compress
description: >-
  Compress video files using ffmpeg with optimized presets. Use when the user
  asks to compress, shrink, or re-encode a video file, or mentions ffmpeg, demo
  recording, screen capture, video size reduction, or says "make this video
  smaller". Do NOT use for audio-only compression, image optimization, video
  editing/trimming, or format conversion without size reduction intent. Korean
  triggers: "비디오", "압축", "최적화".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "execution"
---
# Video Compress

Compress video files using ffmpeg with configurable presets. Default preset is **H264-CRF32** (~14.9x compression, 93.3% size reduction).

## Input

The user provides:
1. **Video file path** (required) -- e.g. `~/Videos/demo.mov`
2. **Preset name** (optional) -- defaults to `h264-crf32`

## Presets

| Preset | Codec | CRF | ffmpeg Preset | Audio | Extra | Typical Ratio |
|---|---|---|---|---|---|---|
| `h264-crf32` (default) | libx264 | 32 | veryslow | AAC 96k | - | ~14.9x |
| `h264-crf28` | libx264 | 28 | fast | AAC 128k | - | ~12.2x |
| `720p` | libx264 | 28 | fast | AAC 128k | scale=1280:-1 | ~61.2x |
| `hevc` | libx265 | 28 | slow | AAC 128k | - | ~10.4x |
| `noaudio` | libx264 | 28 | fast | none | -an | ~12.2x |
| `all` | - | - | - | - | all presets in parallel | varies |

### Custom Parameters

Users may override defaults by specifying:
- **CRF value** (0-51, lower = higher quality, larger file)
- **Resolution** (e.g. `1280:-1` for 720p, `1920:-1` for 1080p)
- **Audio bitrate** (e.g. `64k`, `128k`, `256k`)
- **Codec** (`libx264`, `libx265`)

When custom parameters are given, build the ffmpeg command manually instead of using a preset.

## Workflow

### Step 1: Validate Input

Check that the input file exists and has a recognized video extension:

```bash
ls -lh "<INPUT_FILE>"
```

Supported extensions: `.mov`, `.mp4`, `.avi`, `.mkv`, `.webm`, `.flv`, `.m4v`, `.wmv`, `.ts`

If the file does not exist or is not a vid
