// Получаем кнопку назад
document.addEventListener('DOMContentLoaded', () => {
    const backButton = document.querySelector('.back-btn');
    if (!backButton) return;

    // Сначала удаляем старые обработчики (на случай повторной инициализации)
    backButton.replaceWith(backButton.cloneNode(true));

    // Берем заново
    const newBackButton = document.querySelector('.back-btn');

    newBackButton.addEventListener('click', () => {
        // Перенаправляем на главную страницу
        window.location.href = 'main.html';
    });
});