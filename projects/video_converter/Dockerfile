# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and requirements file into the container at /app
COPY main.py /app/main.py

# Install any dependencies specified in requirements.txt
RUN pip install moviepy loguru

# Run the Python script when the container launches
CMD ["python", "main.py"]
