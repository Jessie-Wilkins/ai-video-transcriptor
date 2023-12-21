# Ai Video Transcriptor
## Summary
An OpenAI Whisper powered python application for taking in videos and creating a transcript for them.

Future functionality will include LLM summarization, LLM "talking to the document", and translation.

## Requirements
Python 3.10
GPU with at least 6GB VRAM (some customizability here)

## Installing dependencies for Python
`pip install -r requirements.txt`

## Running Script
1. Add mp4 video to folder called 'mp4files'.
2. Create folders called 'mp3files' and 'transcripts'
3. Run the main.py script: 
    
    `python main.py`
4. After the process runs (one video takes ~ 5 minutes), a transcript should be produced.