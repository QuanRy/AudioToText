FROM python:3.10-slim

WORKDIR /app

# Копируем только фронтенд
COPY scripts/UI/frontend ./frontend

WORKDIR /app/frontend

EXPOSE 5500

CMD ["python", "-m", "http.server", "5500"]