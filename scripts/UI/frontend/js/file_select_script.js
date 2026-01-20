document.addEventListener('DOMContentLoaded', () => {

    const validExtensions = [
        '.wav', '.mp3', '.mp4', '.avi', '.mov', '.mkv',
        '.flac', '.aac', '.wma', '.wmv', '.alac', '.ogg',
        '.aiff', '.dsd', '.webm', '.flv'
    ];

    const chooseFileBtn = document.querySelector('.choose-file-btn');
    const fileInputField = document.querySelector('.file-input');
    const textArea = document.querySelector('.text-field');

    if (!chooseFileBtn || !fileInputField) return;

    // Проверка расширения файла
    const isValidFile = (fileName) => {
        const ext = fileName.slice(fileName.lastIndexOf('.')).toLowerCase();
        return validExtensions.includes(ext);
    };

    // ===== ВЫЗОВ FASTAPI =====
    const startTranscription = (file) => {
        const formData = new FormData();
        formData.append("file", file);

        if (textArea) {
            textArea.value = "Идёт транскрибация... ⏳";
        }

        fetch("http://127.0.0.1:8000/transcribe", {
            method: "POST",
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            if (data.text) {
                if (textArea) textArea.value = data.text;
            } else {
                alert("Ошибка транскрибации");
                if (textArea) textArea.value = "";
            }
        })
        .catch(() => {
            alert("Не удалось подключиться к серверу");
            if (textArea) textArea.value = "";
        });
    };

    // Открытие диалога выбора файла
    const openFileDialog = () => {
        const fileSelector = document.createElement('input');
        fileSelector.type = 'file';
        fileSelector.accept = validExtensions.join(',');

        fileSelector.onchange = () => {
            const file = fileSelector.files[0];
            if (!file) return;

            const fileName = file.name;

            if (!isValidFile(fileName)) {
                alert(
                    "Внимание! Выбранный файл не является аудио или видео формата.\n" +
                    "Пожалуйста, выберите другой файл!"
                );
                return;
            }

            // Отображаем имя файла
            fileInputField.value = fileName;

            const start = confirm(
                "Начать процесс транскрибации выбранного файла?"
            );

            if (start) {
                console.log("Запуск процесса транскрибации для файла:", fileName);
                startTranscription(file);
            }
        };

        fileSelector.click();
    };

    // Кнопка "Выбрать"
    chooseFileBtn.addEventListener('click', () => {
        const currentFile = fileInputField.value.trim();

        if (!currentFile || !isValidFile(currentFile)) {
            openFileDialog();
        } else {
            const start = confirm(
                "Начать процесс транскрибации выбранного файла?"
            );

            if (start) {
                console.log("Запуск процесса транскрибации для файла:", currentFile);
                // ⚠️ нет File-объекта → открываем диалог заново
                openFileDialog();
            } else {
                openFileDialog();
            }
        }
    });

    // Клик по input — всегда открываем диалог
    fileInputField.addEventListener('click', () => {
        openFileDialog();
    });

});
