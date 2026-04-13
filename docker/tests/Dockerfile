FROM python:3.10-slim

WORKDIR /app

COPY docker/tests/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY scripts/ /app/scripts/
COPY tests/ /app/tests/

WORKDIR /app

CMD ["pytest", "tests/", "-v"]