from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
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