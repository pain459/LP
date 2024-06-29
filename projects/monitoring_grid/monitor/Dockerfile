FROM python:3.9-slim

WORKDIR /app

COPY monitor.py /app
COPY endpoints.txt /app
COPY endpoints.yaml /app

RUN pip install flask requests pyyaml
RUN apt-get update && apt-get install -y curl

EXPOSE 80

CMD ["python", "monitor.py"]
