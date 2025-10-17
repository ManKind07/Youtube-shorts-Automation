Automated Video Subtitle & Caption Pipeline

A powerful, three-stage Python pipeline that leverages OpenAI's Whisper to generate highly accurate, timestamped transcriptions and then uses FFmpeg to burn them as stylized, permanent captions onto any video.

This project automates the entire workflow of creating professional-looking, hardcoded subtitles, saving countless hours of manual transcription and video editing.

How It Works: The Three-Stage Pipeline

The automation is handled by three core scripts that work in sequence:

1. Transcription.py - AI-Powered Transcription

Input: An audio or video file.

Process: Feeds the audio into OpenAI's Whisper model to perform speech-to-text transcription. It captures not just words, but also precise start/end timestamps, pauses, and punctuation for each segment.

Output: A structured JSON file containing the full, timestamped transcript.

2. FFmpeg_facilitator.py - Subtitle Styling & Formatting

Input: The JSON transcript from the previous stage.

Process: Parses the JSON data and converts it into an Advanced SubStation Alpha (.ass) subtitle file. This script is where you can programmatically define the visual characteristics of your captions.

Output: A .ass file containing the text and styling rules (font, size, color, position, etc.) for the subtitles.

3. pipeline.py - Video & Caption Integration

Input: The original source video and the generated .ass file.

Process: This script acts as the final assembler. It uses a templated FFmpeg command to overlay and "burn" the stylized subtitles from the .ass file directly onto the source video frames.

Output: A final .mp4 video with permanent, professional-grade captions.

Built With

Python

OpenAI Whisper

FFmpeg

Getting Started

To get a local copy up and running, follow these steps.

Prerequisites

Python 3.8+

FFmpeg: You must have FFmpeg installed on your system and available in your system's PATH.

PyTorch: Whisper requires a working PyTorch installation.

pip install torch torchvision torchaudio


Installation

Clone the repository:

git clone [https://github.com/your_username/your_project_name.git](https://github.com/your_username/your_project_name.git)


Navigate to the project directory:

cd your_project_name


Install the required Python packages:

pip install -r requirements.txt
# The requirements.txt file should include openai-whisper


Usage

To process a video, run the main pipeline script and specify the path to your source video file.

python pipeline.py --video_path "path/to/your/video.mp4"


The script will execute the full pipeline, and you will find the final captioned video in the output/ directory.

Features

High-Accuracy Transcription: Leverages the state-of-the-art Whisper model for precise speech-to-text, including punctuation.

Word-Level Timestamps: Generates captions that are perfectly synchronized with the audio.

Customizable Caption Styles: Easily modify FFmpeg_facilitator.py to change the font, size, color, and position of your subtitles.

Fully Automated: End-to-end pipeline requires zero manual editing.

Robust & Reliable: Uses the industry-standard FFmpeg for high-quality video processing.
