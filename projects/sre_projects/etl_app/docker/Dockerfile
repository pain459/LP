# Base Image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python ETL script
COPY etl_app.py .

# Set environment variables
ENV DB_HOST=db
ENV DB_NAME=etl_db
ENV DB_USER=user
ENV DB_PASS=password

# Run the ETL script
CMD ["python", "etl_app.py"]
