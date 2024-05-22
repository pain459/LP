FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scripts/ .

# Setup log and output directories
RUN mkdir /app/logs /app/output \
&& chown -R nobody:nogroup /app/logs /app/output \
&& chmod -R 777 /app/logs /app/output
VOLUME ["/app/logs", "/app/output"]

CMD ["python", "executor.py"]
