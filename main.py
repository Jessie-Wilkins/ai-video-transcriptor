import os
import torch
import whisper
from moviepy.editor import *
from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager

model = ""
os.makedirs(os.path.join(os.curdir,  "mp3files"), exist_ok=True)
os.makedirs(os.path.join(os.curdir,  "mp4files"), exist_ok=True)
os.makedirs(os.path.join(os.curdir,  "transcripts"), exist_ok=True)
os.makedirs(os.path.join(os.curdir,  "summaries"), exist_ok=True)

if (os.listdir(os.path.join(os.curdir,"mp4files")).count == 0 or os.listdir(os.path.join(os.curdir,"mp4files")).count != 
    os.listdir(os.path.join(os.curdir,"transcripts")).count):
    model = whisper.load_model("medium", device="cuda", in_memory=True)

for filename in os.listdir(os.path.join(os.curdir,"mp4files")):
    result = ""
    audio = ""
    transcript = ""
    summary_content = ""

    if filename.endswith(".mp4"):
        audio = os.path.join(os.curdir, "mp3files", filename.removesuffix(".mp4")+".mp3")
        if not os.path.exists(audio):
            video = VideoFileClip(os.path.join(os.curdir,"mp4files",filename))
            video.audio.write_audiofile(audio)
        transcript = os.path.join(os.curdir, "transcripts", filename.removesuffix(".mp4")+".txt")
        if not os.path.exists(transcript):
            result = model.transcribe(audio, verbose=True)
            with open(transcript, 'w') as f:
                f.write(result["text"])

torch.cuda.empty_cache()

template = """
Summarize the following: {transcript}
"""

prompt = PromptTemplate(
    template=template, 
    input_variables=["transcript"]
)

llm = Ollama(
    model="mistral-summarizer",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    verbose=True
    )

llm_chain = LLMChain(llm=llm, prompt=prompt)

for filename in os.listdir(os.path.join(os.curdir, "transcripts")):
    with open(os.path.join(os.curdir,"transcripts",filename), 'r') as f:
        content = f.read()
        summary_content = llm_chain.run(transcript = content)
    with open(os.path.join(os.curdir, "summaries", filename.removesuffix(".txt")+"_summary.txt"), 'w') as f:
         f.write(summary_content)

print()
print("Done!!!")