document.addEventListener('DOMContentLoaded', () => {

    const saveBtn = document.querySelector('.save-btn');
    const savePathField = document.querySelector('.save-path-field');
    const textField = document.querySelector('.text-field');

    if (!saveBtn || !savePathField || !textField) return;

    // Функция для сохранения файла через диалог "Сохранить как"
    const saveFile = (defaultName, content) => {
        const blob = new Blob([content], { type: 'text/plain' });
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = defaultName.endsWith('.txt') ? defaultName : `${defaultName}.txt`;

        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        // После сохранения обновляем поле пути
        savePathField.value = defaultName.endsWith('.txt') ? defaultName : `${defaultName}.txt`;
    };

    // Функция проверки перед сохранением
    const checkAndSave = () => {
        const textContent = textField.value.trim();
        const currentPath = savePathField.value.trim() || 'file.txt';

        if (!textContent) {
            const proceed = confirm(
                "Поле текста пустое.\nХотите сохранить пустой файл перед созданием нового?"
            );
            if (!proceed) return;
        } else if (savePathField.value.trim()) {
            const proceed = confirm(
                "Поле для транскрибации не пустое.\nЕсли хотите сохранить, нажмите ОК, иначе выберите другой путь."
            );
            if (!proceed) {
                savePathField.value = '';
                return;
            }
        }

        saveFile(currentPath, textContent);
    };

    // Клик по кнопке "Сохранить"
    saveBtn.addEventListener('click', () => {
        checkAndSave();
    });

    // Клик по полю выбора пути
    savePathField.addEventListener('click', () => {
        checkAndSave();
    });

});
