<h1 align="center"> :sound: AudioToText :sound: </h1>

Ссылки:

[1.	Для чего эта программа?](https://github.com/QuanRy/AudioToText/tree/main#1для-чего-эта-программа)

&nbsp;&nbsp;&nbsp;&nbsp;[2.	Какие форматы принимаются на вход?](https://github.com/QuanRy/AudioToText/tree/main#2какие-форматы-принимаются-на-вход)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3.	Какая модель используется для распознавания?](https://github.com/QuanRy/AudioToText/tree/main#3какая-модель-используется-для-распознавания)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4.	Какие инструменты были использованы?](https://github.com/QuanRy/AudioToText/tree/main#4какие-инструменты-были-использованы)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5.	Как выглядит программа?](https://github.com/QuanRy/AudioToText/tree/main#5как-выглядит-программа)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6.	Какие результаты были получены?](https://github.com/QuanRy/AudioToText/tree/main#6какие-результаты-были-получены)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7.	Как запустить программу?](https://github.com/QuanRy/AudioToText/tree/main#7как-запустить-программу)

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
  <p> Рисунок 5 – Пример транскрибации из готового файла</p> 
</div>
<div id="header" align="center">
  <img src="https://github.com/QuanRy/AudioToText/blob/main/img_for_git/Гифка%20транскрибации.gif" width="700"/>
  <p> GIF 1 – Пример процесса транскрибации</p>
</div>

<div id="header" align="center">
  <img src="https://github.com/QuanRy/AudioToText/blob/main/img_for_git/example_transcib_from_speech.png" width="700"/>
  <p> Рисунок 6 – Пример транскрибации из прямой речи </p> 
</div>
<div id="header" align="center">
  <img src="https://github.com/QuanRy/AudioToText/blob/main/img_for_git/Гифка%20надиктовки.gif" width="700"/>
  <p> GIF 2 – Пример процесса транскрибации из прямой речи </p>
</div>


## 6.	Какие результаты были получены?

<div id="header" align="center">
  <img src="https://github.com/QuanRy/AudioToText/blob/main/img_for_git/Test_table_my_prog.png" width="1000"/>
  <p> Рисунок 7 – Сравнительная таблица результатов работы </p> 
</div>

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Пояснение:*

:white_check_mark: Процент сокращения времени – показатель, насколько транскрибация быстрее длительности файла.

:white_check_mark: Процент несовпадения – показатель отношения расстояния Левенштейна к кол-ву символов в файле.

:white_check_mark: В качестве метрики описывающей точность работы, использовалось расстояние Левенштейна - это метрика, показывающая минимальное количество редакторских операций (вставка, удаление, замена символов) необходимых, чтобы превратить транскрибированный текст в оригинальный (Эталонный).

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; В итоге были протестированы различные файлы, как по длительности, начиная короткими в десяток секунд аудио, заканчивая аудио в 40 минут, так и по содержанию, измеряемому в кол-ве символов. 



## 7.	Как запустить программу?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Чтобы запустить программу вам потребуется запустить файл main.py, расположенный по пути "AudioToText/scripts/main.py" в любо обработчике кода Python, главное, чтобы этот обработчик поддерживал расширения.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :heavy_exclamation_mark: Перед запуском main.py **настоятельно рекомендуется** прочитать инструкцию по установке дополнительных библиотек, необходимых для успешного функционирования данной программы.

Для этого вы можете перейти по пути: "AudioToText/res/как ставить библиотеки.txt" или следовать следующим шагам:

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.  Запустите любую IDE поддерживающию язык программирования Python и его библиотеки (в нашем случае был использован PyCharm Community Edition 2023.2.1)
#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.  Откройте терминал IDE и впишите следующую команду *pip install -r res/requirements.txt* (это установит все необходимые библиотеки для запуска приложения) / установите библиотеки вручную из списка предложенного [тут](https://github.com/QuanRy/AudioToText/tree/main?tab=readme-ov-file#-библиотеки)
#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Запустите файл main.py и у вас запустится [следующее окно](https://github.com/QuanRy/AudioToText/tree/main?tab=readme-ov-file#5как-выглядит-программа)

<div id="header" align="ri">
  <img src="https://raw.githubusercontent.com/trinib/trinib/a5f17399d881c5651a89bfe4a621014b08346cf0/images/marquee.svg" width="1000"/>
</div>

<div id="header" align="center">
  <img src="https://raw.githubusercontent.com/trinib/trinib/82213791fa9ff58d3ca768ddd6de2489ec23ffca/images/footer.svg" width="1000"/>
</div>

