from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
from pathlib import Path

from model.format_to_audio import continue_process_transcription
from model.wav_to_text import start_model

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

        # 3. транскрибация
        txt_path = start_model(wav_path)

        # 4. читаем результат
        with open(txt_path, "r", encoding="utf-8") as f:
            text = f.read()

        # 5. ВОЗВРАЩАЕМ JSON
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
