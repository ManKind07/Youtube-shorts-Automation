#Transcription from Audio with proper pauses

import json
from faster_whisper import WhisperModel

# Use tiny or small for less memory usage
model_size = "tiny.en"
device = "cpu"  # safer on Colab Free
model = WhisperModel(model_size, device=device)

audio_file = "real_audio.mp3"

# Transcribe audio with word-level timestamps
segments, info = model.transcribe(audio_file, beam_size=5, word_timestamps=True)

word_list = []

for segment in segments:
    if not hasattr(segment, 'words'):
        continue  # skip if no word-level info

    for word_info in segment.words:
        word_list.append({
            "word": word_info.word,
            "start": round(word_info.start, 2),
            "end": round(word_info.end, 2)
        })

# Save to JSON
with open("word_timestamps_oneperline.json", "w", encoding="utf-8") as f:
    json.dump(word_list, f, indent=2)

print("Transcription saved. Sample:")
print(word_list[:])
print("#Process Completed")