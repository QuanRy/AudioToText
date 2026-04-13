import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

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
    создание -> обновление -> удаление
    """

    # создание записи
    record_id = save_transcription(
        filename="scenario.mp3",
        extension=".mp3",
        duration=4,
        char_count=12,
        text="начальный текст"
    )

    history = get_history()
    assert len(history) == 1

    # обновление
    update_history_text(record_id, "изменённый текст")

    history = get_history()
    assert history[0]["text"] == "изменённый текст"

    # удаление
    delete_history_record(record_id)

    history = get_history()
    assert len(history) == 0

# Провальный тест
def test_mdd_intentional_failure():
    """
    Длина файла != выделенной памяти. Пересчет произойдет лишь при Update()
    """

    # 1. создаём запись с ОШИБОЧНЫМ char_count
    record_id = save_transcription(
        filename="bug.mp3",
        extension=".mp3",
        duration=3,
        char_count=999,   # Излишнее значение для заполнения БД
        text="hello"
    )

    history = get_history()
    record = history[0]

    # char_count НЕ совпадает с len(text)
    assert record["char_count"] == len(record["text"])