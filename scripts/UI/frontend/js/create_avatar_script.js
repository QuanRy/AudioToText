document.addEventListener('DOMContentLoaded', () => {

    const recordBtn  = document.querySelector('.record-btn');
    const timerEl    = document.querySelector('.timer');
    const infoField  = document.querySelector('.info-field');

    const img        = recordBtn.querySelector('img');
    const modal      = document.getElementById("modal");
    const okBtn      = document.querySelector(".modal-btn");

    const ICON_DEFAULT   = "../../../../icons/record_btn.svg";
    const ICON_RECORDING = "../../../../icons/record_btn_red.svg";

    const DURATION       = 15000;               // 15 секунд записи
    const CHUNK_TIME_MS  = 5000;                // отправляем чанк каждые 5 сек
    const AVATAR_API     = "http://127.0.0.1:9000";

    // ─── состояние ──────────────────────────────────────────────
    let running    = false;
    let paused     = false;
    let sessionId  = null;

    // таймер
    let startTime  = null;
    let pauseTime  = 0;
    let pauseStart = 0;
    let raf        = null;

    // аудио
    let audioContext = null;
    let processor    = null;
    let input        = null;
    let stream       = null;

    let audioBuffer  = [];
    let lastChunkTs  = 0;

    infoField.value = "Нажмите кнопку записи";

    // ─── Конвертация Float32 → Int16 PCM ────────────────────────
    const floatTo16BitPCM = (float32arr) => {
        const pcm = new Int16Array(float32arr.length);
        for (let i = 0; i < float32arr.length; i++) {
            pcm[i] = Math.max(-1, Math.min(1, float32arr[i])) * 0x7fff;
        }
        return pcm;
    };

    // ─── Отправка чанка на бэкенд ───────────────────────────────
    const sendChunk = async (pcm16) => {
        if (!sessionId) return;
        const blob = new Blob([pcm16.buffer], { type: 'application/octet-stream' });
        const form = new FormData();
        form.append('file', blob, 'chunk.pcm');
        try {
            await fetch(`${AVATAR_API}/avatar/chunk/${sessionId}`, {
                method: 'POST',
                body: form
            });
        } catch (e) {
            console.error("Ошибка отправки чанка:", e);
        }
    };

    // ─── Финализация: строим эмбеддинг ──────────────────────────
    const finishRecording = async () => {
        // последний остаток аудио
        if (audioBuffer.length > 0) {
            const pcm16 = floatTo16BitPCM(new Float32Array(audioBuffer));
            audioBuffer = [];
            await sendChunk(pcm16);
        }

        // останавливаем аудио-цепочку
        if (processor) processor.disconnect();
        if (input)     input.disconnect();
        if (audioContext) audioContext.close();
        if (stream)    stream.getTracks().forEach(t => t.stop());

        infoField.value = "Обработка голосового профиля...";

        try {
            const res  = await fetch(`${AVATAR_API}/avatar/finish/${sessionId}`, {
                method: 'POST'
            });
            const data = await res.json();

            if (data.status === "created") {
                infoField.value = `Аватар создан: ${data.avatar_name}`;
                showModal(data.avatar_name);
            } else {
                infoField.value = "Ошибка создания аватара";
                console.error(data);
            }
        } catch (e) {
            infoField.value = "Ошибка соединения с сервером";
            console.error(e);
        }

        sessionId = null;
    };

    // ─── Таймер (обратный отсчёт) ───────────────────────────────
    function format(ms) {
        const totalSec = Math.floor(ms / 1000);
        const min      = String(Math.floor(totalSec / 60)).padStart(2, "0");
        const sec      = String(totalSec % 60).padStart(2, "0");
        const ms2      = String(Math.floor((ms % 1000) / 10)).padStart(2, "0");
        return `${min}:${sec}:${ms2}`;
    }

    function loop(t) {
        if (!startTime) startTime = t;
        const elapsed   = t - startTime - pauseTime;
        const remaining = DURATION - elapsed;

        if (remaining <= 0) {
            timerEl.textContent = "00:00:00";
            stopAll();
            return;
        }

        timerEl.textContent = format(remaining);
        raf = requestAnimationFrame(loop);
    }

    // ─── Остановка всего ────────────────────────────────────────
    async function stopAll() {
        running = false;
        paused  = false;
        cancelAnimationFrame(raf);
        img.src = ICON_DEFAULT;
        await finishRecording();
    }

    // ─── Клик по кнопке записи ──────────────────────────────────
    recordBtn.addEventListener("click", async () => {

        // ── СТАРТ ────────────────────────────────────────────────
        if (!running) {
            running    = true;
            paused     = false;
            startTime  = null;
            pauseTime  = 0;

            img.src         = ICON_RECORDING;
            infoField.value = "Идёт запись...";

            // Стартуем сессию на сервере
            try {
                const res  = await fetch(`${AVATAR_API}/avatar/start`, { method: 'POST' });
                const data = await res.json();
                sessionId  = data.session_id;
            } catch (e) {
                infoField.value = "Нет связи с сервером";
                running = false;
                img.src = ICON_DEFAULT;
                return;
            }

            // Захват микрофона
            stream       = await navigator.mediaDevices.getUserMedia({ audio: true });
            audioContext = new AudioContext({ sampleRate: 16000 });
            input        = audioContext.createMediaStreamSource(stream);
            processor    = audioContext.createScriptProcessor(4096, 1, 1);

            lastChunkTs = Date.now();

            processor.onaudioprocess = async (e) => {
                if (!running || paused) return;

                audioBuffer.push(...e.inputBuffer.getChannelData(0));

                if (Date.now() - lastChunkTs >= CHUNK_TIME_MS) {
                    const pcm16 = floatTo16BitPCM(new Float32Array(audioBuffer));
                    audioBuffer  = [];
                    lastChunkTs  = Date.now();
                    await sendChunk(pcm16);
                }
            };

            input.connect(processor);
            processor.connect(audioContext.destination);

            raf = requestAnimationFrame(loop);
            return;
        }

        // ── ПАУЗА ────────────────────────────────────────────────
        if (running && !paused) {
            paused     = true;
            pauseStart = performance.now();
            cancelAnimationFrame(raf);
            img.src         = ICON_DEFAULT;
            infoField.value = "Пауза";
            return;
        }

        // ── ПРОДОЛЖЕНИЕ ──────────────────────────────────────────
        if (running && paused) {
            paused     = false;
            pauseTime += performance.now() - pauseStart;
            img.src         = ICON_RECORDING;
            infoField.value = "Продолжение записи...";
            raf = requestAnimationFrame(loop);
        }
    });

    // ─── Модальное окно ─────────────────────────────────────────
    function showModal(avatarName) {
        const lines = modal.querySelectorAll('.modal-content div');
        if (lines[0]) lines[0].textContent = `Голосовой профиль создан!`;
        if (lines[1]) lines[1].textContent = `Ваш аватар: ${avatarName}`;

        modal.classList.add("show");

        const close = () => modal.classList.remove("show");
        okBtn.onclick = close;
        setTimeout(close, 2000);
    }

    // ─── Сброс при закрытии страницы ────────────────────────────
    window.addEventListener('beforeunload', () => {
        if (sessionId) {
            navigator.sendBeacon(`${AVATAR_API}/avatar/finish/${sessionId}`);
        }
    });

});