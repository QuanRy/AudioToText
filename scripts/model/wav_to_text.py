# ---------------------------------------------- БИБЛИОТЕКИ ------------------------------------------------------------
from vosk import Model, KaldiRecognizer
import wave, json, time, nltk, os
# ----------------------------------------------------------------------------------------------------------------------

def transcribe_audio(file_path):                                              # транскрибация аудио файда
    model_path = "../model/vosk-model-small-ru-0.22"  # малая модель

    model = Model(model_path)
    start_time_model = time.perf_counter()   # старт замера времени выполнения работы модели

    # Открытие файла с аудио
    wf = wave.open(file_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    # Чтение данных и распознавание
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            print("Процесс распознавания...")

    # Получение итогового результата
    result = rec.FinalResult()
    result_dict = json.loads(result)
    transcribed_text = result_dict["text"]

    # Конец времени выполнения программы
    end_time_model = time.perf_counter()
    execution_time_model = end_time_model - start_time_model

    # Преобразование времени выполнения в минуты и секунды
    minutes = int(execution_time_model // 60)
    seconds = int(execution_time_model % 60)
    hundredths = int((execution_time_model * 100) % 100)

    print(f"\n Время выполнения транскрибации: {minutes} минут, {seconds} секунд, {hundredths} сотых секунд. \n")

    return transcribed_text

def add_punctuation_and_capitalize(text):                           # добавление заглавных букв и знаков препинания
    sentences = nltk.sent_tokenize(text)  # Токенизация текста
    corrected_sentences = []

    for sentence in sentences:
        words = nltk.word_tokenize(sentence)  # Разделяем предложение на слова
        corrected_sentence = ""
        for i, word in enumerate(words):
            if i == 0:  # Если это первое слово в предложении
                corrected_sentence += word.capitalize()  # Начинаем с заглавной буквы
            else:
                corrected_sentence += word.lower()  # Остальные слова в нижнем регистре

            if i < len(words) - 1:
                corrected_sentence += " "  # Добавляем пробел между словами
            else:
                corrected_sentence += "."  # Добавляем точку в конце предложения

        corrected_sentences.append(corrected_sentence)

    return ' '.join(corrected_sentences)


def start_model(audio_file_path):         # запуск модели
    transcribed_text_temp_path = os.path.abspath("../test_formats/TXT/transcribed_text_temp.txt")

    text = transcribe_audio(audio_file_path)
    text_with_punctuation = add_punctuation_and_capitalize(text)

    with open(transcribed_text_temp_path, "w") as text_file:
        text_file.write(text_with_punctuation)
        print("Текст успешно сохранен в файл 'transcribed_text_temp.txt'.")


    return transcribed_text_temp_path           # Возвращение пути к временному файлу с транскрибацией