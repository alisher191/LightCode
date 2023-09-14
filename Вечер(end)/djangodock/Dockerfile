FROM python:3.11-slim

# SHELL [ "/bin/bash/", "-c" ]

#Запрещает создавать файлы с кешом (.pyc)
ENV PYTHONDONTWRITEBYTECODE 1 

#Запрещает буфферизировать сообщения с логами
ENV PYTHONUNBUFFERED 1

#Обновляем pip
RUN pip install --upgrade pip

RUN mkdir app
WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r requirements.txt

# install psycopg dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
 
ADD . /app/
ADD .env.docker /app/.env

CMD ["gunicorn", "store.wsgi:application", "-b", "0.0.0.0:8000"]
