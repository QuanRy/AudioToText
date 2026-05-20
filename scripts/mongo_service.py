from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "audiototext_tests")

client = MongoClient(MONGO_URL)
db = client[DB_NAME]
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


# ──────────────────────────────────────────────────────────────
#  Таблица - Цифровые аватары
# ──────────────────────────────────────────────────────────────

avatars_col = db["digital_avatars"]

def save_avatar(name: str, embedding: list, char_count: int) -> str:
    """Сохраняет голосовой профиль аватара. Возвращает строковый ID."""
    doc = {
        "name":        name,
        "voice":       "recorded",
        "language":    "ru",
        "embedding":   embedding,        # список из 256 float
        "char_count":  char_count,       # кол-во PCM-сэмплов
        "description": "",
        "created_at":  datetime.now(),
        "updated_at":  datetime.now(),
    }
    result = avatars_col.insert_one(doc)
    print(f"Аватар сохранён в MongoDB, id: {result.inserted_id}")
    return str(result.inserted_id)


def get_avatars() -> list:
    """Возвращает список всех аватаров (без эмбеддинга — он большой)."""
    records = []
    for doc in avatars_col.find().sort("created_at", -1):
        records.append({
            "id":          str(doc["_id"]),
            "name":        doc.get("name", ""),
            "voice":       doc.get("voice", ""),
            "language":    doc.get("language", ""),
            "char_count":  doc.get("char_count", 0),
            "description": doc.get("description", ""),
            "created_at":  doc["created_at"].isoformat() if doc.get("created_at") else None,
            "updated_at":  doc["updated_at"].isoformat() if doc.get("updated_at") else None,
        })
    return records


def update_avatar_description(avatar_id: str, description: str):
    """Обновляет описание аватара."""
    result = avatars_col.update_one(
        {"_id": ObjectId(avatar_id)},
        {"$set": {
            "description": description,
            "updated_at":  datetime.now(),
        }}
    )
    if result.matched_count == 0:
        raise ValueError(f"Аватар с ID {avatar_id} не найден")
    print(f"Описание аватара обновлено, id: {avatar_id}")


def delete_avatar(avatar_id: str):
    """Удаляет аватара из базы."""
    result = avatars_col.delete_one({"_id": ObjectId(avatar_id)})
    if result.deleted_count == 0:
        raise ValueError(f"Аватар с ID {avatar_id} не найден")
    print(f"Аватар удалён, id: {avatar_id}")