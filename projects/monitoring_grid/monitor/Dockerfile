FROM python:3.9-slim

WORKDIR /app

COPY monitor.py /app
# COPY endpoints.txt /app
COPY endpoints.yaml /app
COPY services /app/services

RUN pip install flask requests pyyaml Flask-Cors==1.10.3
RUN apt-get update && apt-get install -y curl

EXPOSE 80

CMD ["python", "monitor.py"]
