# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 for the application
EXPOSE 5000

# Set the environment variable for Flask to point to the app instance
ENV FLASK_APP=run.py

# Run the application using Gunicorn in production
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
