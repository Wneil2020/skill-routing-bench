---
name: transcribee
description: "Use when Transcribe YouTube, Instagram Reels, TikTok, and local audio/video files with speaker diarization, then auto-categorize into a self-organizing: covers transcribee, 빌드, 비디오, organizing, reels"
metadata:
  holon-triggers: |
    transcribe a video URL
    audio file
---

---
name: transcribee
description: >-
  Transcribe YouTube, Instagram Reels, TikTok, and local audio/video files with
  speaker diarization, then auto-categorize into a self-organizing knowledge
  library. Use when the user asks to transcribe a video URL, podcast, audio
  file, or build a transcript library. Do NOT use for live audio capture,
  real-time streaming, or text-to-speech generation. Korean triggers: "빌드",
  "비디오", "트랜스크립션".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Transcribee

Transcribe video/audio content with speaker diarization (ElevenLabs) and auto-categorize transcripts into a self-organizing knowledge library (Claude).

## Prerequisites

### System Dependencies

```bash
brew install yt-dlp ffmpeg
```

### API Keys

Configure `~/.local/share/transcribee/.env`:

```bash
ELEVEN_LABS_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

Copy from `.env.example` if setting up for the first time:

```bash
cp ~/.local/share/transcribee/.env.example ~/.local/share/transcribee/.env
```

### Installation Path

The transcribee tool is installed at `~/.local/share/transcribee/`. Run commands from this directory or use the shell alias below.

## Quick Start

```bash
cd ~/.local/share/transcribee

# Transcribe a YouTube video
pnpm exec tsx index.ts "https://www.youtube.com/watch?v=..."

# Transcribe an Instagram Reel
pnpm exec tsx index.ts "https://instagram.com/reel/..."

# Transcribe a TikTok video
pnpm exec tsx index.ts "https://vt.tiktok.com/..."

# Transcribe a local file
pnpm exec tsx index.ts ~/Downloads/podcast.mp3
pnpm exec tsx index.ts ~/Videos/interview.mp4
```

### Shell Alias (Recommended)

Add to `~/.zshrc`:

```bash
alias transcribee="noglob ~/.local/share/transcribee/transcribe.sh"
```

Then use: `transcribee "https://youtube.com/watch?v=..."`

## Workflow

The tool follows a 5-step pipeline:

1. **Download/Extract Audio** -- yt-dlp for URLs, ffmpeg for local video files
2. **Transcribe** -- ElevenLabs `s
