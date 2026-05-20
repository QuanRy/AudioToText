document.addEventListener('DOMContentLoaded', async () => {

    const avatarList    = document.getElementById('avatarList');
    const modalOverlay  = document.getElementById('modalOverlay');
    const confirmOverlay = document.getElementById('confirmOverlay');

    const modalName      = document.getElementById('modalName');
    const modalVoice     = document.getElementById('modalVoice');
    const modalLang      = document.getElementById('modalLang');
    const modalCharCount = document.getElementById('modalCharCount');
    const modalCreatedAt = document.getElementById('modalCreatedAt');
    const modalUpdatedAt = document.getElementById('modalUpdatedAt');
    const modalDesc      = document.getElementById('modalDesc');

    const modalClose  = document.getElementById('modalClose');
    const modalSave   = document.getElementById('modalSave');
    const modalDelete = document.getElementById('modalDelete');
    const confirmYes  = document.getElementById('confirmYes');
    const confirmNo   = document.getElementById('confirmNo');

    document.getElementById('createAvatarBtn').addEventListener('click', () => {
        window.location.href = 'create_avatar_menu.html';
    });

    let currentId    = null;
    let originalDesc = '';

    /* =====================
       ФОРМАТИРОВАНИЕ
    ===================== */
    const formatDate = (dateStr) => {
        if (!dateStr) return '—';
        const d = new Date(dateStr);
        const pad = (n) => n.toString().padStart(2, '0');
        return `${pad(d.getDate())}.${pad(d.getMonth()+1)}.${d.getFullYear()} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
    };

    /* =====================
       ЗАГРУЗКА АВАТАРОВ
    ===================== */
    const loadAvatars = async () => {
        avatarList.innerHTML = '<div class="history-loading">Загрузка...</div>';
        try {
            const res  = await fetch('http://127.0.0.1:9000/avatars');
            const data = await res.json();

            if (!data.records || data.records.length === 0) {
                avatarList.innerHTML = '<div class="history-empty">Вы не добавили ни одного аватара!</div>';
                return;
            }

            avatarList.innerHTML = '';
            data.records.forEach(record => {
                const row = document.createElement('div');
                row.className = 'history-row';
                row.innerHTML = `
                    <span title="${record.name}">${record.name}</span>
                    <span>${record.voice || '—'}</span>
                    <span>${record.language || '—'}</span>
                    <span>${record.char_count ?? '—'}</span>
                    <span title="${record.description}">${record.description || ''}</span>
                    <span>${formatDate(record.created_at)}</span>
                    <span>${formatDate(record.updated_at)}</span>
                `;
                row.addEventListener('click', () => openModal(record));
                avatarList.appendChild(row);
            });

        } catch (e) {
            avatarList.innerHTML = '<div class="history-empty">Ошибка загрузки аватаров</div>';
            console.error(e);
        }
    };

    /* =====================
       ОТКРЫТИЕ МОДАЛКИ
    ===================== */
    const openModal = (record) => {
        currentId    = record.id;
        originalDesc = record.description || '';

        modalName.value      = record.name || '—';
        modalVoice.value     = record.voice || '—';
        modalLang.value      = record.language || '—';
        modalCharCount.value = (record.char_count ?? '—') + (record.char_count != null ? ' симв.' : '');
        modalCreatedAt.value = formatDate(record.created_at);
        modalUpdatedAt.value = formatDate(record.updated_at);
        modalDesc.value      = record.description || '';

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
    modalDesc.addEventListener('input', () => {
        const changed = modalDesc.value !== originalDesc;
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
            await fetch(`http://127.0.0.1:9000/avatars/${currentId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ description: modalDesc.value })
            });
            modalOverlay.classList.remove('active');
            await loadAvatars();
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
            await fetch(`http://127.0.0.1:9000/avatars/${currentId}`, {
                method: 'DELETE'
            });
            confirmOverlay.classList.remove('active');
            modalOverlay.classList.remove('active');
            await loadAvatars();
        } catch (e) {
            console.error('Ошибка удаления:', e);
        }
    });

    // Старт
    await loadAvatars();
});