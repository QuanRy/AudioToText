document.addEventListener('DOMContentLoaded', async () => {

    const historyList = document.getElementById('historyList');
    const modalOverlay = document.getElementById('modalOverlay');
    const confirmOverlay = document.getElementById('confirmOverlay');

    const modalFilename  = document.getElementById('modalFilename');
    const modalExtension = document.getElementById('modalExtension');
    const modalDuration  = document.getElementById('modalDuration');
    const modalCharCount = document.getElementById('modalCharCount');
    const modalCreatedAt = document.getElementById('modalCreatedAt');
    const modalUpdatedAt = document.getElementById('modalUpdatedAt');
    const modalText      = document.getElementById('modalText');

    const modalClose  = document.getElementById('modalClose');
    const modalSave   = document.getElementById('modalSave');
    const modalDelete = document.getElementById('modalDelete');
    const confirmYes  = document.getElementById('confirmYes');
    const confirmNo   = document.getElementById('confirmNo');

    let currentId = null;
    let originalText = '';

    /* =====================
       ФОРМАТИРОВАНИЕ
    ===================== */
    const formatDate = (dateStr) => {
        if (!dateStr) return '—';
        const d = new Date(dateStr);
        const pad = (n) => n.toString().padStart(2, '0');
        return `${pad(d.getDate())}.${pad(d.getMonth()+1)}.${d.getFullYear()} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
    };

    const formatName = (filename) => {
        if (filename === 'live_recording') return '🎙 Прямая речь';
        return filename;
    };

    /* =====================
       ЗАГРУЗКА ИСТОРИИ
    ===================== */
    const loadHistory = async () => {
        historyList.innerHTML = '<div class="history-loading">Загрузка...</div>';
        try {
            const res = await fetch('http://127.0.0.1:8000/history');
            const data = await res.json();

            if (!data.records || data.records.length === 0) {
                historyList.innerHTML = '<div class="history-empty">История пуста</div>';
                return;
            }

            historyList.innerHTML = '';
            data.records.forEach(record => {
                const row = document.createElement('div');
                row.className = 'history-row';
                row.innerHTML = `
                    <span title="${record.filename}">${formatName(record.filename)}</span>
                    <span>${record.extension}</span>
                    <span>${record.duration_sec}</span>
                    <span>${record.char_count}</span>
                    <span title="${record.text}">${record.text}</span>
                    <span>${formatDate(record.created_at)}</span>
                    <span>${formatDate(record.updated_at)}</span>
                `;
                row.addEventListener('click', () => openModal(record));
                historyList.appendChild(row);
            });

        } catch (e) {
            historyList.innerHTML = '<div class="history-empty">Ошибка загрузки истории</div>';
            console.error(e);
        }
    };

    /* =====================
       ОТКРЫТИЕ МОДАЛКИ
    ===================== */
    const openModal = (record) => {
        currentId = record.id;
        originalText = record.text;

        modalFilename.value  = formatName(record.filename);
        modalExtension.value = record.extension;
        modalDuration.value  = record.duration_sec + ' сек';
        modalCharCount.value = record.char_count + ' симв.';
        modalCreatedAt.value = formatDate(record.created_at);
        modalUpdatedAt.value = formatDate(record.updated_at);
        modalText.value      = record.text;

        // кнопка сохранить — неактивна
        modalSave.disabled = true;
        modalSave.classList.remove('active');

        modalOverlay.classList.add('active');
    };

    /* =====================
       ЗАКРЫТИЕ МОДАЛКИ
    ===================== */
    modalClose.addEventListener('click', () => {
        modalOverlay.classList.remove('active');
        currentId = null;
    });

    /* =====================
       СЛЕДИМ ЗА ИЗМЕНЕНИЕМ ТЕКСТА
    ===================== */
    modalText.addEventListener('input', () => {
        const changed = modalText.value !== originalText;
        modalSave.disabled = !changed;
        if (changed) {
            modalSave.classList.add('active');
        } else {
            modalSave.classList.remove('active');
        }
    });

    /* =====================
       СОХРАНИТЬ ИЗМЕНЕНИЯ
    ===================== */
    modalSave.addEventListener('click', async () => {
        if (!currentId) return;
        try {
            await fetch(`http://127.0.0.1:8000/history/${currentId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: modalText.value })
            });
            modalOverlay.classList.remove('active');
            await loadHistory();
        } catch (e) {
            console.error('Ошибка сохранения:', e);
        }
    });

    /* =====================
       УДАЛИТЬ
    ===================== */
    modalDelete.addEventListener('click', () => {
        confirmOverlay.classList.add('active');
    });

    confirmNo.addEventListener('click', () => {
        confirmOverlay.classList.remove('active');
    });

    confirmYes.addEventListener('click', async () => {
        if (!currentId) return;
        try {
            await fetch(`http://127.0.0.1:8000/history/${currentId}`, {
                method: 'DELETE'
            });
            confirmOverlay.classList.remove('active');
            modalOverlay.classList.remove('active');
            await loadHistory();
        } catch (e) {
            console.error('Ошибка удаления:', e);
        }
    });

    // Старт
    await loadHistory();
});