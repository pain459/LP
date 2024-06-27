FROM python:3.9-slim

WORKDIR /app

# Install netcat
RUN apt-get update && apt-get install -y netcat-traditional

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["./wait-for-it.sh", "db", "5432", "flask", "run", "--host=0.0.0.0"]
