FROM python:3.10-slim

WORKDIR /app

# Копируем фронтенд
COPY scripts/UI/frontend ./frontend

# Копируем иконки
COPY icons ./frontend/icons

WORKDIR /app/frontend

EXPOSE 5500

CMD ["python", "-m", "http.server", "5500"]