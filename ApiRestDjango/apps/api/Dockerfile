FROM python:3.12.7-alpine3.20

WORKDIR /app

# Instala pip y actualiza
RUN pip install --upgrade pip

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

# No crea archivos .pyc (bytecode) en el contenedor
ENV PYTHONDONTWRITEBYTECODE=1 
# Hace que la salida del print() y logs se impriman inmediatamente en la consola
ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]