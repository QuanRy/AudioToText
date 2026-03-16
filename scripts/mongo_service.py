from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")  # локально (без докера)
# client = MongoClient("mongodb://mongo:27017/")  # если докер 
db = client["audiototext"]
collection = db["transcriptions"]

def save_transcription(filename: str, extension: str, duration: float, char_count: int, text: str):
    record = {
        "filename": filename,
        "extension": extension,
        "duration_sec": duration,
        "char_count": char_count,
        "text": text,
        "created_at": datetime.now()
    }
    result = collection.insert_one(record)
    print(f"Сохранено в MongoDB, id: {result.inserted_id}")
    return str(result.inserted_id)