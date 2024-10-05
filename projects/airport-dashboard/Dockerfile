# Dockerfile
FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

# Set FLASK_APP environment variable
ENV FLASK_APP=run.py

# Use Gunicorn to run the app in production mode
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
