# Взять официальный базовый образ Python платформы Docker
FROM python:3.11.1

# Задать переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установить рабочую директорию
WORKDIR /dip

# Установить зависимости
RUN pip install --upgrade pip
COPY requirements.txt /dip/
RUN pip install -r requirements.txt

# Копировать файлы
COPY . /dip/

RUN chmod +x wait-for-it.sh



