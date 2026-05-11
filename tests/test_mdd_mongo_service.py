import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from bson import ObjectId

from scripts.mongo_service import (
    save_transcription,
    get_history,
    update_history_text,
    delete_history_record,
    collection
)


@pytest.fixture(autouse=True)
def clear_db():
    collection.delete_many({})
    yield
    collection.delete_many({})


def test_full_module_flow():
    """
    Полный сценарий работы модуля:
    создание - обновление - удаление
    """

    record_id = save_transcription(
        filename="scenario.mp3",
        extension=".mp3",
        duration=4,
        char_count=12,
        text="начальный текст"
    )

    history = get_history()
    assert len(history) == 1

    update_history_text(record_id, "изменённый текст")

    history = get_history()
    assert history[0]["text"] == "изменённый текст"

    delete_history_record(record_id)

    history = get_history()
    assert len(history) == 0

# Создание + проверка модуля истории
def test_history_module_insert_flow():
    """
    save_transcription - get_history
    """

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

# Создание + Изменение
def test_history_module_update_flow():
    """
    save - update - get
    """

    record_id = save_transcription(
        filename="audio.mp3",
        extension=".mp3",
        duration=1.5,
        char_count=5,
        text="старый текст"
    )

    update_history_text(record_id, "новый текст")

    history = get_history()

    assert len(history) == 1
    assert history[0]["text"] == "новый текст"

# Создание + удаление
def test_history_module_delete_flow():
    """
    save - delete - get
    """

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

def test_update_after_delete_raises_exception():
    """
    попытка обновить удаленную запись
    """
    
    record_id = save_transcription(
        filename="audio.mp3",
        extension=".mp3",
        duration=3,
        char_count=5,
        text="hello"
    )
    delete_history_record(record_id)
    
    # Обновление несуществующей записи
    with pytest.raises(Exception) as exc_info:  
        update_history_text(record_id, "новый текст")
    
    # дополнительно проверяем ТИП исключения
    assert "not found" in str(exc_info.value).lower() or \
           "does not exist" in str(exc_info.value).lower()
    
    # проверяем что БД осталась пустой
    assert len(get_history()) == 0

def test_delete_already_deleted_record_raises_exception():
    """
    попытка удалить уже удаленную запись
    save + delete + delete 
    """
    
    record_id = save_transcription(
        filename="audio.mp3",
        extension=".mp3",
        duration=3,
        char_count=5,
        text="hello"
    )
    
    delete_history_record(record_id)
    
    # Второе удаление той же записи
    with pytest.raises(Exception) as exc_info:
        delete_history_record(record_id)
    
    # сообщение об ошибке
    assert "not found" in str(exc_info.value).lower() or \
           "does not exist" in str(exc_info.value).lower() or \
           "не найдена" in str(exc_info.value).lower()
    
    # проверяем что БД действительно пуста
    history = get_history()
    assert len(history) == 0
    
    # проверяем что нельзя получить удаленную запись
    assert collection.find_one({"_id": ObjectId(record_id)}) is None


def test_update_with_empty_text_saves_correctly():
    """
    Обновление записи пустым текстом (удаление текста, без удаления записи)
    save + update с пустой строкой
    """

    record_id = save_transcription(
        filename="audio.mp3",
        extension=".mp3",
        duration=3,
        char_count=5,
        text="hello"
    )
    
    # Обновляем пустым текстом (пользователь решил удалить текст, но не запись)
    update_history_text(record_id, "")
    
    history = get_history()
    
    # Проверки на пустоту, неизменность ID, даты обновления...
    assert len(history) == 1
    assert history[0]["text"] == ""
    assert history[0]["char_count"] == 0 
    assert history[0]["id"] == record_id
    assert history[0]["updated_at"] is not None

# -----------------------------
# Провальные тесты
# -----------------------------

# def test_mdd_intentional_failure():
#     """
#     Длина файла != выделенной памяти. Пересчет произойдет лишь при Update()
#     """

#     # создаём запись с ОШИБОЧНЫМ char_count
#     record_id = save_transcription(
#         filename="bug.mp3",
#         extension=".mp3",
#         duration=3,
#         char_count=999,   # Излишнее значение для заполнения БД
#         text="hello"
#     )

#     history = get_history()
#     record = history[0]

#     # char_count НЕ совпадает с len(text)
#     assert record["char_count"] == len(record["text"])