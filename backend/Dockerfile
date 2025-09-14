# Usa Python 3.11
FROM python:3.11-slim

# Establece directorio de trabajo
WORKDIR /app

# Copia los requirements primero para cachear
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el proyecto al contenedor
COPY . .

# Expone el puerto que usa Django
EXPOSE 8000

# Comando por defecto para correr el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
