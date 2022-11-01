FROM python:3.10

EXPOSE 7777

RUN mkdir -p /opt/services/bot/homework-geektech
WORKDIR /opt/services/bot/homework-geektech

COPY . /opt/services/bot/homework-geektech

RUN pip install -r requirements.txt

CMD["python", "/opt/services/bot/homework-geekrech/main.py"]