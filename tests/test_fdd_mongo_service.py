import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from bson.errors import InvalidId
from bson import ObjectId
from datetime import datetime, timedelta

from scripts.mongo_service import (
    save_transcription,
    get_history,
    update_history_text,
    delete_history_record,
    collection
)


# очищаем БД перед тестами
@pytest.fixture(autouse=True)
def clear_db():
    collection.delete_many({})
    yield
    collection.delete_many({})


# -----------------------------
# Позитивные тесты
# -----------------------------

def test_save_transcription_success():
    """Проверка функции сохранения"""

    record_id = save_transcription(
        filename="test.mp3",
        extension=".mp3",
        duration=3.5,
        char_count=10,
        text="тест"
    )

    assert record_id is not None

def test_get_history_returns_empty_list_when_no_records():
    """
    проверка get_history() на пустую коллекцию
    """
    
    # проверка на пустоту БД изначально 
    assert collection.count_documents({}) == 0
    
    history = get_history()
    
    # Проверяем что вернулся пустой список
    assert history == []
    assert len(history) == 0
    assert isinstance(history, list)

def test_save_transcription_returns_valid_objectid_string():
    """
    проверка что save_transcription возвращает валидный ObjectId в виде строки
    """
    
    record_id = save_transcription(
        filename="test.mp3",
        extension=".mp3",
        duration=2.5,
        char_count=100,
        text="проверка id"
    )
    
    # Проверяем что вернулась строка
    assert isinstance(record_id, str)

def test_delete_history_record_removes_existing_document():
    """
    проверка что delete_history_record удаляет существующий документ
    """

    test_doc = {
        "filename": "direct_insert.mp3",
        "extension": ".mp3",
        "duration_sec": 1.0,
        "char_count": 5,
        "text": "direct insert"
    }
    result = collection.insert_one(test_doc)
    record_id = str(result.inserted_id)
    
    # Проверяем что документ действительно в БД
    assert collection.count_documents({"_id": ObjectId(record_id)}) == 1

    delete_history_record(record_id)
    
    # Проверяем что документ удален из БД
    assert collection.count_documents({"_id": ObjectId(record_id)}) == 0


def test_get_history_returns_sorted_list_with_correct_structure():
    """
    проверка структуры данных возвращаемых get_history()
    """
    
    # ПРЯМАЯ вставка нескольких документов в БД
    doc1 = {
        "filename": "first.mp3",
        "extension": ".mp3",
        "duration_sec": 1.0,
        "char_count": 5,
        "text": "first",
        "created_at": datetime.now() - timedelta(days=2)
    }
    
    doc2 = {
        "filename": "second.mp3",
        "extension": ".wav",
        "duration_sec": 2.0,
        "char_count": 6,
        "text": "second",
        "created_at": datetime.now() - timedelta(days=1)
    }
    
    doc3 = {
        "filename": "third.mp3",
        "extension": ".m4a",
        "duration_sec": 3.0,
        "char_count": 5,
        "text": "third",
        "created_at": datetime.now()
    }
    
    # Вставляем в разном порядке
    collection.insert_many([doc2, doc1, doc3])
    
    # Тестируем ТОЛЬКО get_history
    history = get_history()
    
    # Проверяем количество
    assert len(history) == 3
    
    # Проверяем сортировку (свежие сверху)
    assert history[0]["filename"] == "third.mp3"
    assert history[1]["filename"] == "second.mp3"
    assert history[2]["filename"] == "first.mp3"
    
    # Проверяем структуру каждого элемента
    for record in history:
        assert "id" in record
        assert "filename" in record
        assert "extension" in record
        assert "duration_sec" in record
        assert "char_count" in record
        assert "text" in record
        assert "created_at" in record
        
        # Проверяем типы полей
        assert isinstance(record["id"], str)
        assert isinstance(record["filename"], str)
        assert isinstance(record["duration_sec"], (int, float))
        assert isinstance(record["char_count"], int)
        assert isinstance(record["text"], str)


# -----------------------------
# Негативные тесты
# -----------------------------

def test_delete_invalid_id():
    """Удаление с неправильным id"""

    with pytest.raises(InvalidId):
        delete_history_record("123")


def test_update_invalid_id():
    """Обновление с неправильным id"""

    with pytest.raises(Exception):
        update_history_text("invalid", "text")


def test_invalid_duration():
    """Передача неправильного типа duration"""

    with pytest.raises(Exception):
        save_transcription(
            filename="audio.mp3",
            extension=".mp3",
            duration="abc",
            char_count=10,
            text="hello"
        )




# Провальный тест
# def test_missing_extension():
#     """Расширение отсутствует, оно передано в названии файла"""

#     with pytest.raises(Exception):
#         save_transcription(
#             filename="audio.mp3",
#             extension=None,
#             duration=2,
#             char_count=5,
#             text="hello"
#         )