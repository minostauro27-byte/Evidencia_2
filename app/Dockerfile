FROM python:3.10-slim

WORKDIR /app

# Actualizar paquetes base
RUN pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" "msgpack>=1.2.1" wheel

COPY requirements.txt .
RUN python -m pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" wheel \
    && python -m pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]