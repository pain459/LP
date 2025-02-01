# Use an official python runtime as a parent image
FROM python:3.9-slim

# Install pika (RabbitMQ client library)
RUN pip install pika

# Copy consumer code
COPY consumer.py /app/

# Set the working directory
WORKDIR /app

# Run the producer script
CMD ["python", "consumer.py"]