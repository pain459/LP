FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the FastAPI app
COPY . .

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh

# Grant execute permissions to the entrypoint script
RUN chmod +x /entrypoint.sh

# Expose port
EXPOSE 5000

# Run entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
