# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install DuckDB Python package, wget, and unzip
RUN apt-get update && \
    apt-get install -y wget unzip && \
    pip install duckdb && \
    wget https://github.com/duckdb/duckdb/releases/download/v0.7.1/duckdb_cli-linux-amd64.zip && \
    unzip duckdb_cli-linux-amd64.zip && \
    mv duckdb /usr/local/bin/ && \
    rm duckdb_cli-linux-amd64.zip

# Copy the current directory contents into the container at /app
COPY . /app

# Run a command line shell by default
CMD ["bash"]
