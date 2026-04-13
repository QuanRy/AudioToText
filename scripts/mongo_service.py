from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")

client = MongoClient(MONGO_URL)
db = client["audiototext_tests"]   # название БД
collection = db["transcriptions"]

def save_transcription(filename: str, extension: str, duration: float, char_count: int, text: str):

    if not isinstance(duration, (int, float)):
        raise ValueError("duration must be number")

    if not isinstance(char_count, int):
        raise ValueError("char_count must be int")

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

def update_transcription(session_id: str, text: str, duration: float):
    """Обновляет существующую запись по session_id"""
    collection.update_one(
        {"_id": ObjectId(session_id)},
        {"$set": {
            "text": text,
            "char_count": len(text),
            "duration_sec": duration,
            "updated_at": datetime.now()
        }}
    )
    print(f"Обновлено в MongoDB, id: {session_id}")

def get_history():
    records = list(collection.find().sort("created_at", -1))  # свежие сверху
    result = []
    for r in records:
        result.append({
            "id": str(r["_id"]),
            "filename": r.get("filename", ""),
            "extension": r.get("extension", ""),
            "duration_sec": r.get("duration_sec", 0),
            "char_count": r.get("char_count", 0),
            "text": r.get("text", ""),
            "created_at": r.get("created_at", "").isoformat() if r.get("created_at") else None,
            "updated_at": r.get("updated_at", "").isoformat() if r.get("updated_at") else None,
        })
    return result

def update_history_text(record_id: str, text: str):
    result = collection.update_one(
        {"_id": ObjectId(record_id)},
        {"$set": {
            "text": text,
            "char_count": len(text),
            "updated_at": datetime.now()
        }}
    )

    # если запись не найдена
    if result.matched_count == 0:
        raise ValueError("Record not found")

    print(f"Текст обновлён, id: {record_id}")

def delete_history_record(record_id: str):
    result = collection.delete_one({"_id": ObjectId(record_id)})
    
    if result.deleted_count == 0:
        raise ValueError(f"Запись с ID {record_id} не найдена")
    else:
        print(f"Запись удалена, id: {record_id}")
    