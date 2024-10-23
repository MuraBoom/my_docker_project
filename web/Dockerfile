# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в контейнер
COPY app.py .

# Устанавливаем зависимости
RUN pip install Flask psycopg2-binary

# Открываем порт
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]
