FROM python:3.10-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install netcat
RUN apt-get update && apt-get install -y netcat-traditional procps && rm -rf /var/lib/apt/lists/*

COPY consumer.py .
COPY wait-for-it.sh .

RUN chmod +x wait-for-it.sh

CMD ["./wait-for-it.sh", "kafka", "9092", "--", "python", "consumer.py"]