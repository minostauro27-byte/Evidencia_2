FROM python:3.10-slim

WORKDIR /app

# Eliminar explícitamente rastros de versiones obsoletas preinstaladas en la imagen base
RUN rm -rf /usr/local/lib/python3.10/site-packages/setuptools* \
           /usr/local/lib/python3.10/site-packages/msgpack*

# Reinstalar dependencias limpias y actualizadas
RUN pip install --no-cache-dir --upgrade "pip>=24.0" "setuptools>=78.1.1" "msgpack>=1.2.1" "wheel>=0.48.0"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
