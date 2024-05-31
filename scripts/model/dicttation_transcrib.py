# ---------------------------------------------- БИБЛИОТЕКИ ------------------------------------------------------------
import json, pyaudio
from vosk import Model, KaldiRecognizer
# ----------------------------------------------------------------------------------------------------------------------
"""
    Это файл лаборабории и песочницы, для оценки и тестирования модели, он никак не связан с UI и основным приложением.
    
    При запуске этого файла можно получать расшифровку своего аудио, при диктовании в микровон прямо в консоль
"""

# model_path = "../model/vosk-model-ru-0.42"   # БОЛЬШАЯ МОДЕЛЬ
model_path = "../model/vosk-model-small-ru-0.22"  # малая модель
model = Model(model_path)

recognition = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def  listen():                   # Запуск потока аудио
    print(" Говорите: ")
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (recognition.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(recognition.Result())
            if answer["text"]:
                yield answer["text"]

for text in listen():          # Печать результатов в консоль
    print(text)