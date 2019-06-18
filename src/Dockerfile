FROM python:3.5.4

RUN mkdir -pv app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000
ENTRYPOINT [ "python" ]

CMD [ "App.py" ]