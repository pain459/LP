FROM python:3.9-slim

WORKDIR /app

COPY user_subscriber.py user_subscriber.py

RUN pip install redis

CMD ["python", "user_subscriber.py"]
