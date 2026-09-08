FROM python:3.8

WORKDIR /app

# Actualizar paquetes base
RUN pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" "msgpack>=1.2.1" wheel

# Eliminar paquetes obsoletos o empaquetados por ensurepip/sistema
RUN find / -name "*setuptools-70*" -o -name "*msgpack-1.1*" -exec rm -rf {} + 2>/dev/null || true

COPY requirements.txt .
RUN python -m pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" wheel \
    && python -m pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]