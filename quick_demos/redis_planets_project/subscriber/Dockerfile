FROM python:3.9-slim

WORKDIR /app

COPY subscriber.py subscriber.py

RUN pip install redis

CMD ["python", "subscriber.py"]
