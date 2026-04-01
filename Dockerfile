# Використовуємо Python 3.10
FROM python:3.10-slim

WORKDIR /app

# Копіюємо файли
COPY requirements.txt .
COPY app.py .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Виставляємо порт
EXPOSE 3000

# Запускаємо додаток
CMD ["python", "app.py"]