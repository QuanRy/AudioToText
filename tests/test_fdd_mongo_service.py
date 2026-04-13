import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from bson.errors import InvalidId

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


def test_get_history_after_insert():
    """Проверка функции получения истории"""

    save_transcription(
        filename="audio.mp3",
        extension=".mp3",
        duration=2,
        char_count=5,
        text="hello"
    )

    history = get_history()

    assert len(history) == 1
    assert history[0]["filename"] == "audio.mp3"


def test_update_history_text():
    """Проверка обновления текста"""

    record_id = save_transcription(
        filename="audio.mp3",
        extension=".mp3",
        duration=1.5,
        char_count=5,
        text="старый текст"
    )

    update_history_text(record_id, "новый текст")

    history = get_history()

    assert history[0]["text"] == "новый текст"


def test_delete_history_record():
    """Проверка удаления записи"""

    record_id = save_transcription(
        filename="audio.mp3",
        extension=".mp3",
        duration=1,
        char_count=5,
        text="hello"
    )

    delete_history_record(record_id)

    history = get_history()

    assert len(history) == 0


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
