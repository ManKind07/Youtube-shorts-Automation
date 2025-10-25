#Transcription from Audio with proper pauses
#Running on google colab coz its easier to setup and less hassle to run

import json
from faster_whisper import WhisperModel

# Using tiny model coz its enough for our use case as well as memory efficient
model_size = "tiny.en"
device = "cpu"  #GPU can be used, but again CPU is enough for our use case
model = WhisperModel(model_size, device=device)

audio_file = "[Insert your audio File]"

#Transcribe of sample audio with word-level timestamps
segments, info = model.transcribe(audio_file, beam_size=5, word_timestamps=True)

word_list = []

for segment in segments:
    if not hasattr(segment, 'words'):
        continue  #skips if no word-level info

    for word_info in segment.words:
        word_list.append({
            "word": word_info.word,
            "start": round(word_info.start, 2),
            "end": round(word_info.end, 2)
        })

#Save as JSON
with open("word_timestamps_oneperline.json", "w", encoding="utf-8") as f:
    json.dump(word_list, f, indent=2)

print("Transcription saved. Sample:")
print(word_list[:])

print("#Process Completed")
