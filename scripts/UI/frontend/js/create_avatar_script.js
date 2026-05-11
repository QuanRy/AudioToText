document.addEventListener('DOMContentLoaded', () => {

    const recordBtn = document.querySelector('.record-btn');
    const timerEl = document.querySelector('.timer');
    const infoField = document.querySelector('.info-field');

    const img = recordBtn.querySelector('img');

    const modal = document.getElementById("modal");
    const okBtn = document.querySelector(".modal-btn");

    const ICON_DEFAULT = "../../../../icons/record_btn.svg";
    const ICON_RECORDING = "../../../../icons/record_btn_red.svg";

    const DURATION = 15000;

    let running = false;
    let paused = false;

    let startTime = null;
    let pauseTime = 0;
    let raf = null;

    // =========================
    // ФОРМАТ MM:SS:MS
    // =========================
    function format(ms) {

        const totalSec = Math.floor(ms / 1000);
        const min = String(Math.floor(totalSec / 60)).padStart(2, "0");
        const sec = String(totalSec % 60).padStart(2, "0");
        const msPart = String(Math.floor((ms % 1000) / 10)).padStart(2, "0");

        return `${min}:${sec}:${msPart}`;
    }

    // =========================
    // LOOP
    // =========================
    function loop(t) {

        if (!startTime) startTime = t;

        const elapsed = t - startTime - pauseTime;
        const remaining = DURATION - elapsed;

        if (remaining <= 0) {
            timerEl.textContent = "00:00:00";
            stop();
            return;
        }

        timerEl.textContent = format(remaining);

        raf = requestAnimationFrame(loop);
    }

    infoField.value = "Нажмите кнопку записи";

    // =========================
    // CLICK (START / PAUSE / RESUME)
    // =========================
    recordBtn.addEventListener("click", () => {

        // START
        if (!running) {

            running = true;
            paused = false;

            startTime = null;
            pauseTime = 0;

            img.src = ICON_RECORDING;
            infoField.value = "Идёт запись...";

            raf = requestAnimationFrame(loop);
            return;
        }

        // PAUSE
        if (running && !paused) {

            paused = true;

            cancelAnimationFrame(raf);
            pauseStart = performance.now();

            img.src = ICON_DEFAULT;
            infoField.value = "Пауза";

            return;
        }

        // RESUME
        if (running && paused) {

            paused = false;

            pauseTime += performance.now() - pauseStart;

            img.src = ICON_RECORDING;
            infoField.value = "Продолжение записи...";

            raf = requestAnimationFrame(loop);
        }
    });

    // =========================
    // STOP
    // =========================
    function stop() {
        infoField.value = "";

        running = false;
        paused = false;

        cancelAnimationFrame(raf);

        img.src = ICON_DEFAULT;
        infoField.value = "Запись завершена";

        showModal();
    }

    // =========================
    // MODAL
    // =========================
    function showModal() {

        modal.classList.add("show");

        const close = () => modal.classList.remove("show");

        okBtn.onclick = close;

        setTimeout(close, 2000);
    }

});