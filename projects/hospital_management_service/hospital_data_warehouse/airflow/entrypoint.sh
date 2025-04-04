#!/usr/bin/env bash

# entrypoint.sh

# Wait for PostgreSQL to be available
./wait-for-it.sh postgres_warehouse:5432 -- echo "PostgreSQL is up - executing command"

# Initialize the Airflow database
airflow db init

# Create default user
airflow users create \
    --username airflow \
    --firstname Airflow \
    --lastname Admin \
    --role Admin \
    --email admin@example.com \
    --password airflow

# Start the Airflow web server and scheduler
airflow webserver --port 8080 & airflow scheduler
