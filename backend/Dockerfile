FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Dependencias de sistema necesarias
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc

# Copiar requirements y pip install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar resto de la app (en dev se monta el volumen)
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EOF