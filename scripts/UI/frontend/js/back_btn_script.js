// Получаем кнопку назад
document.addEventListener('DOMContentLoaded', () => {
    const backButton = document.querySelector('.back-btn');
    if (!backButton) return;

    backButton.replaceWith(backButton.cloneNode(true));
    const newBackButton = document.querySelector('.back-btn');

    newBackButton.addEventListener('click', async () => {
        // сбрасываем сессию MongoDB перед переходом
        try {
            await fetch("http://127.0.0.1:9000/reset", { method: "POST" });
        } catch (e) {
            console.error("Ошибка сброса сессии:", e);
        }
        window.location.href = 'main.html';
    });
});