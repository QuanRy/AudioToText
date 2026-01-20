document.addEventListener('DOMContentLoaded', () => {

    const validExtensions = [
        '.wav', '.mp3', '.mp4', '.avi', '.mov', '.mkv', 
        '.flac', '.aac', '.wma', '.wmv', '.alac', '.ogg', 
        '.aiff', '.dsd', '.webm', '.flv'
    ];

    const chooseFileBtn = document.querySelector('.choose-file-btn');
    const fileInputField = document.querySelector('.file-input');

    if (!chooseFileBtn || !fileInputField) return;

    // Проверка, что файл допустимый
    const isValidFile = (fileName) => {
        const ext = fileName.slice(fileName.lastIndexOf('.')).toLowerCase();
        return validExtensions.includes(ext);
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
                alert("Внимание! Выбранный файл не является аудио или видео формата. Пожалуйста, выберите другой файл!");
                return;
            }

            // Ставим путь в поле
            fileInputField.value = fileName;

            // После выбора файла сразу можно предложить начать транскрибацию
            const start = confirm("Начать процесс транскрибации выбранного файла?");
            if (start) {
                console.log("Запуск процесса транскрибации для файла:", fileName);
                // Здесь можно вызвать функцию транскрибации
            }
        };

        fileSelector.click();
    };

    // Клик по кнопке "Выбрать"
    chooseFileBtn.addEventListener('click', () => {
        const currentFile = fileInputField.value.trim();

        if (!currentFile || !isValidFile(currentFile)) {
            // Если поле пустое или файл неверный — открываем диалог выбора
            openFileDialog();
        } else {
            // Если поле уже заполнено корректным файлом — спрашиваем о запуске транскрибации
            const start = confirm("Начать процесс транскрибации выбранного файла?");
            if (start) {
                console.log("Запуск процесса транскрибации для файла:", currentFile);
                // Здесь можно вызвать функцию транскрибации
            } else {
                // Можно предложить выбрать другой файл
                openFileDialog();
            }
        }
    });

    // Клик по полю input
    fileInputField.addEventListener('click', () => {
        openFileDialog();
    });

});
