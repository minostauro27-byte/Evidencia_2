FROM python:3.10-slim

WORKDIR /app

# Upgrade forzado de herramientas base y paquetes vulnerables preinstalados
RUN pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" "msgpack>=1.2.1" wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
