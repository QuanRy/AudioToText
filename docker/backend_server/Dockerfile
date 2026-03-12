FROM python:3.10-slim

WORKDIR /app

# Системные зависимости
RUN apt-get update && apt-get install -y ffmpeg

# СОЗДАЕМ ВСЕ ПАПКИ------------------------------------
RUN mkdir -p /app/test_formats/WAV    
RUN mkdir -p /app/test_formats/MP3
RUN mkdir -p /app/test_formats/MP4
RUN mkdir -p /app/test_formats/TXT
RUN mkdir -p /app/uploads
RUN mkdir -p /app/temp
RUN mkdir -p /app/scripts/temp         
# ------------------------------------------------------

# Копируем requirements.txt из Dockerfile
COPY docker/backend_server/requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скачиваем NLTK ресурсы
RUN python -m nltk.downloader punkt punkt_tab

# Копируем код приложения (скрипты)
COPY scripts/ /app/scripts/

# Устанавливаем рабочую директорию для скриптов
WORKDIR /app/scripts

EXPOSE 8000

CMD ["uvicorn", "fastapi_server:app", "--host", "0.0.0.0", "--port", "8000"]