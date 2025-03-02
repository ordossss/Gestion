# Usar una imagen base de Python
FROM python:3.11

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todos los archivos al contenedor
COPY . .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Definir el comando de inicio
CMD ["python", "main.py"]
