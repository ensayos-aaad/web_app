# uvicorn main:app
# uvicorn main:app --reload

# Main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
#from fastapi.middleware.cors import CORSMiddleware

# Custom function imports
from functions.speech_to_text import voice_to_text

# Initiate App
app = FastAPI()

# Check health
@app.get("/")
@app.get("/health")
async def check_health():
    return {"response": "healthy"}


@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):

    # Convert audio to text - production
    # Save the file temporarily
    
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")
    
    print(audio_input)

    # Decode audio
    # message_decoded = voice_to_text(audio_input)
    print(message_decoded)
    return {"response": message_decoded}
