FROM python:3.11.5

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=server.settings

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
