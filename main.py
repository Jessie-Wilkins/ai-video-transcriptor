import os
import whisper
from moviepy.editor import *

model = whisper.load_model("medium", device="cuda", in_memory=True)

for filename in os.listdir(os.path.join(os.curdir,"mp4files")):
    if filename.endswith(".mp4"):
        audio = os.path.join(os.curdir, "mp3files", filename.removesuffix(".mp4")+".mp3")
        if not os.path.exists(audio):
            video = VideoFileClip(os.path.join(os.curdir,"mp4files",filename))
            video.audio.write_audiofile(audio)
        result = model.transcribe(audio, verbose=True)
        with open(os.path.join(os.curdir, "transcripts", filename.removesuffix(".mp3")+".txt"), 'w') as f:
            f.write(result["text"])