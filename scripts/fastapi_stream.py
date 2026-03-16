from fastapi import FastAPI, UploadFile, File, Body
from fastapi.middleware.cors import CORSMiddleware
from vosk import Model, KaldiRecognizer
import json, time

from mongo_service import save_transcription, update_transcription

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = "../model/vosk-model-small-ru-0.22"
model = Model(model_path)

recognizer = KaldiRecognizer(model, 16000)
recognizer.SetWords(True)

# Состояние сессии
session_id = None
session_text = ""
session_start = None
session_duration = 0.0


@app.post("/transcribe_chunk")
async def transcribe_chunk(file: UploadFile = File(...)):
    global session_start
    if session_start is None:
        session_start = time.perf_counter()

    audio_bytes = await file.read()

    if recognizer.AcceptWaveform(audio_bytes):
        result = json.loads(recognizer.Result())
        return {"type": "final", "text": result.get("text", "")}
    else:
        partial = json.loads(recognizer.PartialResult())
        return {"type": "partial", "text": partial.get("partial", "")}


@app.post("/pause")
async def pause(data: dict = Body(...)):
    global session_id, session_text, session_duration, session_start

    text = data.get("text", "").strip()
    if not text:
        return {"status": "ok", "session_id": session_id}

    if session_start:
        session_duration += round(time.perf_counter() - session_start, 2)
        session_start = None

    session_text = text

    if session_id is None:
        session_id = save_transcription(
            filename="live_recording",
            extension=".pcm",
            duration=session_duration,
            char_count=len(session_text),
            text=session_text
        )
    else:
        update_transcription(session_id, session_text, session_duration)

    return {"status": "ok", "session_id": session_id}


@app.post("/reset")
async def reset_recognizer():
    global recognizer, session_id, session_text, session_duration, session_start
    recognizer = KaldiRecognizer(model, 16000)
    recognizer.SetWords(True)
    session_id = None
    session_text = ""
    session_duration = 0.0
    session_start = None
    return {"status": "ok"}