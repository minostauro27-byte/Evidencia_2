FROM python:3.10-slim

WORKDIR /app

# 1. Actualización forzada del gestor y herramientas base
RUN python -m pip install --no-cache-dir --upgrade pip setuptools>=78.1.1 wheel

# 2. Instalación de requisitos + parche específico para msgpack
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt && \
    python -m pip install --no-cache-dir --upgrade "msgpack>=1.2.1" "setuptools>=78.1.1"

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
