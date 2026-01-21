FROM python:3.10-slim

# ДОБАВЬ ЭТИ СТРОКИ В САМОМ НАЧАЛЕ!
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

WORKDIR /app

# Системные зависимости
RUN apt-get update

# Копируем requirements из папки с Dockerfile
COPY docker/backend_stream/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY scripts/ /app/scripts/

WORKDIR /app/scripts

EXPOSE 9000

CMD ["uvicorn", "fastapi_stream:app", "--host", "0.0.0.0", "--port", "9000"]