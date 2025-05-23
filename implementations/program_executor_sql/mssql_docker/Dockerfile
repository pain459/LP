FROM python:3.9-slim

# Install required packages
RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    freetds-dev \
    tdsodbc \
    && rm -rf /var/lib/apt/lists/*

# Install ODBC driver for SQL Server
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    curl \
    gnupg \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Install Faker library for generating dummy data
RUN pip install faker

# Install pyodbc
RUN pip install pyodbc

# Set the working directory in the container
WORKDIR /app

# Copy the Python scripts into the container
COPY connect_to_sql.py /app/connect_to_sql.py
COPY generate_dummy_data.py /app/generate_dummy_data.py

# Set the entrypoint
CMD ["python", "connect_to_sql.py"]
