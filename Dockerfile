FROM python:3.7-alpine
MAINTAINER S3-Infosoft

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app
