document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.buttons');
    if (!container) return;

    // Получаем кнопки заново и очищаем старые обработчики
    const newContainer = container.cloneNode(true);
    container.replaceWith(newContainer);

    const buttons = newContainer.querySelectorAll('button');

    buttons.forEach((button, index) => {
        button.addEventListener('click', () => {
            switch(index) {
                case 0: // "Выбрать"
                    window.location.href = 'transcrib_text_menu.html';
                    break;
                case 1: // "Записать"
                    window.location.href = 'dictation_text_menu.html';
                    break;
                case 2: // "Профиль"
                    window.location.href = 'history_menu.html';
                    break;
                case 3: // "О программе?"
                    window.location.href = 'info_menu.html';
                    break;
            }
        });
    });
});