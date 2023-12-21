# Ai Video Transcriptor
## Summary
An OpenAI Whisper powered python application for taking in videos and creating a transcript for them.

Future functionality will include LLM summarization, LLM "talking to the document", and translation.

## Requirements
Python 3.10
GPU with at least 6GB VRAM (some customizability here)
Ollama 0.1.12

## Preparation
1. Install all necessary python libraries using the below command:
    
    `pip install -r requirements.txt`
2. Create the Ollama model from the Modelfile like so:

    `ollama create llama-summarizer`

3. Ensure Ollama is running and ready to use.

## Running the Script
1. Add mp4 video to folder called 'mp4files'.
2. Run the main.py script: 
    
    `python main.py`
3. After the process runs (one video takes ~ 5 minutes), a transcript should be produced.