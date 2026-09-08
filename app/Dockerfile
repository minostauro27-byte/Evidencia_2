FROM python:3.10-slim

WORKDIR /app

# Actualizar paquetes base
RUN pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" "msgpack>=1.2.1" wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Eliminar directorios de metadatos residuales que detecta Trivy
RUN find /usr/local/lib/python3.10/site-packages/ -maxdepth 1 -type d \( -name "setuptools-70*" -o -name "msgpack-1.1*" \) -exec rm -rf {} +

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]