from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil, os, time
from pathlib import Path

from model.format_to_audio import continue_process_transcription
from model.wav_to_text import start_model
from mongo_service import save_transcription, get_history, update_history_text, delete_history_record

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "temp"
UPLOAD_DIR.mkdir(exist_ok=True)


@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    try:
        # 1. сохраняем загруженный файл
        input_path = UPLOAD_DIR / file.filename
        with open(input_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 2. конвертация в WAV (если нужно)
        wav_path = continue_process_transcription(str(input_path))

        # 3. транскрибация — start_model не трогаем, возвращает путь как раньше
        start_time = time.perf_counter()
        txt_path = start_model(wav_path)
        duration = round(time.perf_counter() - start_time, 2)

        # 4. читаем результат
        with open(txt_path, "r", encoding="utf-8") as f:
            text = f.read()

        # 5. сохраняем в MongoDB
        extension = os.path.splitext(file.filename)[1].lower()
        save_transcription(
            filename=file.filename,
            extension=extension,
            duration=duration,
            char_count=len(text),
            text=text
        )

        # 6. возвращаем JSON
        return {
            "status": "ok",
            "text": text
        }

    except Exception as e:
        print(" ОШИБКА:", e)
        return {
            "status": "error",
            "message": str(e)
        }

@app.get("/history")
async def history():
    try:
        records = get_history()
        return {"status": "ok", "records": records}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.put("/history/{record_id}")
async def update_record(record_id: str, data: dict):
    try:
        update_history_text(record_id, data.get("text", ""))
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.delete("/history/{record_id}")
async def delete_record(record_id: str):
    try:
        delete_history_record(record_id)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}