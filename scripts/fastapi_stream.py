from fastapi import FastAPI, UploadFile, File, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from vosk import Model, KaldiRecognizer
import json, time, uuid
import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav

from mongo_service import (
    save_transcription,
    update_transcription,
    save_avatar,
    get_avatars,
    update_avatar_description,
    delete_avatar,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = "../model/vosk-model-small-ru-0.22"
vosk_model = Model(model_path)

recognizer = KaldiRecognizer(vosk_model, 16000)
recognizer.SetWords(True)

voice_encoder = VoiceEncoder()

session_id = None
session_text = ""
session_start = None
session_duration = 0.0

avatar_sessions: dict[str, list[bytes]] = {}


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
    recognizer = KaldiRecognizer(vosk_model, 16000)
    recognizer.SetWords(True)
    session_id = None
    session_text = ""
    session_duration = 0.0
    session_start = None
    return {"status": "ok"}


@app.post("/avatar/start")
async def avatar_start():
    sid = str(uuid.uuid4())
    avatar_sessions[sid] = []
    return {"session_id": sid}


@app.post("/avatar/chunk/{session_id}")
async def avatar_chunk(session_id: str, file: UploadFile = File(...)):
    if session_id not in avatar_sessions:
        return JSONResponse({"error": "unknown session"}, status_code=404)

    raw = await file.read()
    avatar_sessions[session_id].append(raw)
    return {"status": "ok", "chunks": len(avatar_sessions[session_id])}


@app.post("/avatar/finish/{session_id}")
async def avatar_finish(session_id: str):
    if session_id not in avatar_sessions:
        return JSONResponse({"error": "unknown session"}, status_code=404)

    raw_chunks = avatar_sessions.pop(session_id)

    if not raw_chunks:
        return JSONResponse({"error": "no audio received"}, status_code=400)

    pcm16 = np.frombuffer(b"".join(raw_chunks), dtype=np.int16)
    audio_float = pcm16.astype(np.float32) / 32768.0

    wav = preprocess_wav(audio_float)
    embedding = voice_encoder.embed_utterance(wav)

    temp_suffix = uuid.uuid4().hex[:8]
    avatar_name = f"user_{temp_suffix}"

    avatar_id = save_avatar(
        name=avatar_name,
        embedding=embedding.tolist(),
        char_count=int(pcm16.shape[0]),
    )

    return {
        "status": "created",
        "avatar_id": avatar_id,
        "avatar_name": avatar_name,
        "embedding_dim": len(embedding),
    }


@app.get("/avatars")
async def list_avatars():
    try:
        records = get_avatars()
        return {"status": "ok", "records": records}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.put("/avatars/{avatar_id}")
async def edit_avatar(avatar_id: str, data: dict):
    try:
        update_avatar_description(avatar_id, data.get("description", ""))
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.delete("/avatars/{avatar_id}")
async def remove_avatar(avatar_id: str):
    try:
        delete_avatar(avatar_id)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}