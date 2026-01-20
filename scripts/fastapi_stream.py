from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from vosk import Model, KaldiRecognizer
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = "../model/vosk-model-small-ru-0.22"
model = Model(model_path)

# ОДИН recognizer на всё время работы сервиса (чтобы не ломать во время чанков)
recognizer = KaldiRecognizer(model, 16000)
recognizer.SetWords(True)

@app.post("/transcribe_chunk")
async def transcribe_chunk(file: UploadFile = File(...)):
    audio_bytes = await file.read()

    if recognizer.AcceptWaveform(audio_bytes):
        result = json.loads(recognizer.Result())
        return {
            "type": "final",
            "text": result.get("text", "")
        }
    else:
        partial = json.loads(recognizer.PartialResult())
        return {
            "type": "partial",
            "text": partial.get("partial", "")
        }

@app.post("/reset")
async def reset_recognizer():
    global recognizer
    recognizer = KaldiRecognizer(model, 16000)
    recognizer.SetWords(True)
    return {"status": "ok"}