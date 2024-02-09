from fastapi import FastAPI, File, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Word Counter API",
    description="An API that counts characters and words in a given text.",
    version="1.0.0",
)

app.mount("/generated_audio", StaticFiles(directory="generated_audio"), name="generated_audio")

# Enable CORS for https://chat.openai.com/
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chat.openai.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the manifest content from the ai-plugin.json file
with open('ai-plugin.json', 'r') as manifest_file:
    manifest_content = json.load(manifest_file)

# Serve the manifest file at the /.well-known/ai-plugin.json path
@app.get("/.well-known/ai-plugin.json")
async def serve_manifest():
    return JSONResponse(content=manifest_content)

@app.get("/text-to-speech")
async def text_to_speech(text: str = Query(..., description="Text to convert to speech")):
    # Generate audio with ElevenLabs
    import uuid, os
    import elevenlabs
    elevenlabs.set_api_key('')
    voices = elevenlabs.voices()
    audio = elevenlabs.generate(text=text, voice=voices[0], model="eleven_multilingual_v2")

    # Save the audio file
    file_name = f"{uuid.uuid4()}.mp3"
    file_path = os.path.join("generated_audio", file_name)
    with open(file_path, "wb") as audio_file:
        audio_file.write(audio)

    # Construct URL to access the audio file
    # Assuming you have a static file serving setup or an endpoint to serve this file
    audio_url = f"https://140023d0967cb5.lhr.life/generated_audio/{file_name}"

    return {"speech_url": audio_url}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)