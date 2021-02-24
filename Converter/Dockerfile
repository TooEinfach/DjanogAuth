FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app/

ADD . /app

RUN pip3 install Django

RUN pip3 install djangorestframework

RUN pip3 install celery

RUN pip3 install django-celery-beat