FROM python:3.10-slim

WORKDIR /app

# Системные зависимости
RUN apt-get update

# Копируем requirements.txt из Dockerfile
COPY docker/backend_server/requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения (скрипты)
COPY scripts/ /app/scripts/

# Устанавливаем рабочую директорию для скриптов
WORKDIR /app/scripts

EXPOSE 8000

CMD ["uvicorn", "fastapi_server:app", "--host", "0.0.0.0", "--port", "8000"]