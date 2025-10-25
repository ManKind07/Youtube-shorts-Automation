# 🤖 YouTube Shorts Automation Pipeline

This project provides a set of Python scripts to automate the creation of engaging, captioned YouTube Shorts. The pipeline takes a raw audio file and a background video, transcribes the audio using AI, generates word-by-word "karaoke-style" subtitles, and combines everything into a final, polished video file with a title card.

The process is broken into three main stages: AI transcription, subtitle generation, and FFmpeg video assembly.

---

## 🚀 Features

- **AI-Powered Transcription:** Uses `faster_whisper` (a fast implementation of OpenAI's Whisper) for accurate, word-level transcription.  
- **Word-by-Word Timestamps:** Generates precise start and end times for every single word in the audio.  
- **Karaoke-Style Subtitles:** Automatically converts timestamps into an `.ass` subtitle file with karaoke fade effects.  
- **FFmpeg Automation:** A powerful pipeline script (`pipeline.py`) chains multiple FFmpeg commands to:
  - Burn subtitles onto the video.
  - Add the original audio.
  - Overlay a fading title card.
  - Trim the video to its final length.  
- **Lightweight:** Designed to run efficiently (the transcription model is `tiny.en`).

---

## ⚙️ How It Works — The 3-Script Pipeline

This project is a **manual, step-by-step pipeline**. You must run the scripts in order.

### 1️⃣ `Transcription.py` — Audio to Timestamps

- **Input:** An audio file (e.g., `real_audio.mp3`). Edit the `audio_file` variable in the script.  
- **Process:** Loads the `faster_whisper` model and transcribes the entire audio file, generating word-level timestamps.  
- **Output:** `word_timestamps_oneperline.json` containing a list of all words with start/end times.

---

### 2️⃣ `FFmpeg_Facilitator.py` — Timestamps to Subtitles

- **Input:** JSON data from `word_timestamps_oneperline.json`.  
- **Process (Manual Step):**  
  1. Copy the JSON list from `word_timestamps_oneperline.json`.  
  2. Paste it into `FFmpeg_Facilitator.py`, replacing the `timestamps = [...]` example list.  
- **Output:** `words_karaoke.ass` — a formatted Advanced SubStation Alpha subtitle file with karaoke-style effects.

---

### 3️⃣ `pipeline.py` — Video Assembly

- **Input:** Ensure the following files are in the same directory:
  - `words_karaoke.ass` (from Step 2)
  - `real_audio.mp3` (original audio)
  - `output.mp4` (background video)
  - `title.png` (title card image)

- **Process:** Runs a series of FFmpeg commands:
  - Burns the subtitles onto `output.mp4` and adds `real_audio.mp3`.
  - Delays the audio by 2 seconds for the title.
  - Overlays `title.png` on a blurred background, fading between 2–4 seconds.
  - Trims the first 2 seconds to create the final short.

- **Output:** `output_trimmed.mp4` — the final polished video.

---
