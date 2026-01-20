document.addEventListener('DOMContentLoaded', () => {

    const recordBtn = document.querySelector('.record-btn');
    const infoField = document.querySelector('.info-field');
    const timerDisplay = document.querySelector('.timer');

    if (!recordBtn || !infoField || !timerDisplay) return;

    const defaultIcon = "../../../../icons/record_btn.svg";
    const recordingIcon = "../../../../icons/record_btn_red.svg";

    let isRecording = false;
    let timer = null;
    let startTime = 0; // время старта в миллисекундах
    let elapsedBeforePause = 0; // время прошедшее до паузы

    const formatTime = (ms) => {
        let totalSeconds = Math.floor(ms / 1000);
        let minutes = Math.floor(totalSeconds / 60);
        let seconds = totalSeconds % 60;
        let centiseconds = Math.floor((ms % 1000) / 10);

        const pad = (n, digits = 2) => n.toString().padStart(digits, '0');

        return `${pad(Math.floor(minutes / 60))}:${pad(minutes % 60)}:${pad(seconds)}`;
    };

    const startTimer = () => {
        startTime = Date.now();
        timer = setInterval(() => {
            const now = Date.now();
            const elapsed = elapsedBeforePause + (now - startTime);
            timerDisplay.textContent = formatTime(elapsed);
        }, 10); // обновляем каждые 10ms
    };

    const stopTimer = () => {
        clearInterval(timer);
        const now = Date.now();
        elapsedBeforePause += (now - startTime);
    };

    recordBtn.addEventListener('click', () => {
        if (!isRecording) {
            // Начинаем запись
            isRecording = true;
            recordBtn.querySelector('img').src = recordingIcon;
            infoField.value = "Говорите...";
            startTimer();
        } else {
            // Пауза
            isRecording = false;
            stopTimer();
            recordBtn.querySelector('img').src = defaultIcon;
            infoField.value = "Для продолжения записи нажмите на кнопку...";
        }
    });

});
