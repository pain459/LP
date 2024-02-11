# Use the official PostgreSQL image from Docker Hub
FROM postgres:latest

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_PORT=5433

# Expose the PostgreSQL port
EXPOSE $POSTGRES_PORT

# Copy the custom configuration file to the container
COPY ./postgresql.conf /etc/postgresql/postgresql.conf

# Resource limits
# Limiting CPU usage to 1 core and memory to 1GB
CMD ["postgres", "-c", "max_connections=100", "-c", "shared_buffers=512MB", "-c", "work_mem=16MB", "-c", "maintenance_work_mem=128MB", "-c", "listen_addresses=*", "-c", "port=5433", "-c", "logging_collector=on", "-c", "log_directory=pg_log", "-c", "log_filename=postgresql-%Y-%m-%d_%H%M%S.log", "-c", "log_statement=all", "-c", "max_worker_processes=8", "-c", "max_parallel_workers_per_gather=4"]
