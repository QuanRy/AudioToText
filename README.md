<h1 align="center"> :sound: AudioToText :sound: </h1>

## 1.	Для чего эта программа?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Программный модуль будет использоваться для извлечения и преобразования аудиоданных из файлов различных форматов (например, аудио: MP3, WAV, FLAC, AAC, VOC, WMA, видео: MP4, AVI и другие) в текстовый формат. Модуль будет поддерживать возможность «подредактировать» текст сразу после транскрибации прямо в окне приложения, а затем уже подредаченный текст можно будет сохранить, если нам это понадобится, обеспечивая адаптацию под конкретные задачи и ожидания конечного результата пользователей.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Также данный программный модуль позволит не только перевести уже готовые аудио / видео в текстовый формат, но и самому пользователю провести «надиктовку» текста прямо с устройства, на котором запущена программа, причем пользователь будет получать текст в реальном времени, прямо во время надиктовки. Также будет иметься возможность скорректировать некие неточности распознавания или же отредактировать имена, даты и т.п.

## 2.	Какие форматы принимаются на вход?
#### •	Аудио: MP3, FLAC, WAV, AAC, VOC, WMA, ALAC :sound:
#### •	Видео: MP4, AVI, MOV, WMV, MKV, FLV :movie_camera:
#### •	Прямую речь в микрофон :microphone:

## 3.	Какая модель используется для распознавания?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; В качестве модели для распознавания русской речи используется модель от компании Alpha Cephei - Vosk. А именно **Vosk-ru-0.22**. :wrench:

Обучающий набор данных:
#### •  Набор данных "OpenSTT" от проекта Silero, 
#### •  **2,3 ТБ данных**,
#### •  **20 000 часов аудио** на русском языке (в формате .WAV)

## 4.	Какие инструменты были использованы?
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Библиотеки:
#### •  PySide6 и PyQt6 (версия: 6.4.2)
#### •  Vosk (версия: 0.3.45)
#### •  NLTK (версия: 3.8.1)
#### •  PyAudio (версия: 0.25.1)
#### •  PyDub (версия: 0.2.14)
#### •  MoviePy (версия: 1.0.3)

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Язык программирования 
#### •  Python (версия: 3.11)

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; IDE:
#### •  PyCharm Community Edition (версия: 2023.2.1)

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Модель:
#### •  Модель vosk-model-ru-0.22

## 5.	Как выглядит программа?
<div id="header" align="center">
  <img src="https://github.com/QuanRy/AudioToText/blob/main/img_for_git/main_window.png" width="700"/>
  <p> Рисунок 1 – Стартовое окно </p> 
</div>
<div id="header" align="center">
  <img src="https://github.com/QuanRy/AudioToText/blob/main/img_for_git/info_window.png" width="500"/>
  <p> Рисунок 2 – Окно со справочной информацией </p> 
</div>
<div id="header" align="center">
  <img src="https://github.com/QuanRy/AudioToText/blob/main/img_for_git/transcrib_from_file_window.png" width="700"/>
  <p> Рисунок 3 – Окно транскрибации готового файла </p> 
</div>
<div id="header" align="center">
  <img src="https://github.com/QuanRy/AudioToText/blob/main/img_for_git/transcrib_from_real_speech.png" width="700"/>
  <p> Рисунок 4 – Окно транскрибации при надиктовке </p> 
</div>
<div id="header" align="center">
  <img src="https://github.com/QuanRy/AudioToText/blob/main/img_for_git/example_transcrib_from_file.png" width="700"/>
  <p> Рисунок 5 – Пример транскрибации из готового файла </p> 
</div>
<div id="header" align="center">
  <img src="https://github.com/QuanRy/AudioToText/blob/main/img_for_git/transcrib_from_real_speech.png" width="700"/>
  <p> Рисунок 6 – Пример транскрибации из прямой речи </p> 
</div>

