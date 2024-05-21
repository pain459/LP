# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Create a directory for logs
RUN mkdir /app/logs

# Give write access (if necessary, depending on your app's requirements)
RUN chmod 777 /app/logs


# Copy the requirements file and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install curl CLI for checks.
RUN apt-get update && apt-get install -y curl

# Copy the scripts directory into the container at /app
COPY scripts/ ./

# Make port 5002 available to the world outside this container
EXPOSE 5002

# Define the command to run the application
CMD ["python", "executor.py"]
