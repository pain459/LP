FROM python:3.10-slim

RUN apt update && apt install -y chrony

WORKDIR /app
COPY app.py requirements.txt ./

RUN pip install -r requirements.txt

COPY chrony.conf /etc/chrony/chrony.conf

# CMD service chrony restart && chronyd -q && python app.py
CMD chronyd -q && python app.py

