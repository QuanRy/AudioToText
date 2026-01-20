document.addEventListener('DOMContentLoaded', async () => {

    const recordBtn = document.querySelector('.record-btn');
    const infoField = document.querySelector('.info-field');
    const timerDisplay = document.querySelector('.timer');
    const textField = document.querySelector('.text-field');

    if (!recordBtn || !infoField || !timerDisplay || !textField) return;

    const defaultIcon = "../../../../icons/record_btn.svg";
    const recordingIcon = "../../../../icons/record_btn_red.svg";

    let isRecording = false;

    /* =======================
       ТАЙМЕР + КНОПКА Record
    ======================= */
    let timer = null;
    let startTime = 0;
    let elapsedBeforePause = 0;

    const formatTime = (ms) => {
        let totalSeconds = Math.floor(ms / 1000);
        let minutes = Math.floor(totalSeconds / 60);
        let seconds = totalSeconds % 60;

        const pad = (n) => n.toString().padStart(2, '0');
        return `${pad(Math.floor(minutes / 60))}:${pad(minutes % 60)}:${pad(seconds)}`;
    };

    const startTimer = () => {
        startTime = Date.now();
        timer = setInterval(() => {
            const now = Date.now();
            const elapsed = elapsedBeforePause + (now - startTime);
            timerDisplay.textContent = formatTime(elapsed);
        }, 10);
    };

    const stopTimer = () => {
        clearInterval(timer);
        elapsedBeforePause += Date.now() - startTime;
    };

    /* =======================
       АУДИО + СТРИМИНГ
    ======================= */
    let audioContext;
    let processor;
    let input;
    let stream;

    let audioBuffer = [];
    const CHUNK_TIME = 5000;
    let lastChunkTime = 0;

    const floatTo16BitPCM = (float32) => {
        const pcm16 = new Int16Array(float32.length);
        for (let i = 0; i < float32.length; i++) {
            pcm16[i] = Math.max(-1, Math.min(1, float32[i])) * 0x7fff;
        }
        return pcm16;
    };

    const sendChunk = async (pcm16) => {
        const blob = new Blob([pcm16.buffer], { type: 'application/octet-stream' });
        const formData = new FormData();
        formData.append('file', blob, 'chunk.pcm');

        try {
            const res = await fetch('http://127.0.0.1:9000/transcribe_chunk', {
                method: 'POST',
                body: formData
            });
            const data = await res.json();
            if (data.text) {
                textField.value += data.text + ' ';
            }
        } catch (e) {
            console.error("Ошибка отправки:", e);
        }
    };

    recordBtn.addEventListener('click', async () => {

        if (!isRecording) {
            /* ====== СТАРТ ====== */
            isRecording = true;
            recordBtn.querySelector('img').src = recordingIcon;
            infoField.value = "Говорите...";
            startTimer();

            stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            audioContext = new AudioContext({ sampleRate: 16000 });

            input = audioContext.createMediaStreamSource(stream);
            processor = audioContext.createScriptProcessor(4096, 1, 1);

            lastChunkTime = Date.now();

            processor.onaudioprocess = async (e) => {
                if (!isRecording) return;

                audioBuffer.push(...e.inputBuffer.getChannelData(0));

                if (Date.now() - lastChunkTime >= CHUNK_TIME) {
                    const pcm16 = floatTo16BitPCM(new Float32Array(audioBuffer));
                    audioBuffer = [];
                    lastChunkTime = Date.now();
                    await sendChunk(pcm16);
                }
            };

            input.connect(processor);
            processor.connect(audioContext.destination);

        } else {
            /* ====== ПАУЗА ====== */
            isRecording = false;
            stopTimer();

            recordBtn.querySelector('img').src = defaultIcon;
            infoField.value = "Для продолжения записи нажмите на кнопку...";

            // отправляем остаток (< 5 сек)
            if (audioBuffer.length > 0) {
                const pcm16 = floatTo16BitPCM(new Float32Array(audioBuffer));
                audioBuffer = [];
                await sendChunk(pcm16);
            }

            processor.disconnect();
            input.disconnect();
            audioContext.close();
            stream.getTracks().forEach(t => t.stop());
        }
    });
});
