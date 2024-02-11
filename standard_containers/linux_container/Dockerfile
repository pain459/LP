# Use a Debian-based image as the base
FROM debian:latest

# Update package lists and install PostgreSQL client
RUN apt-get update && \
    apt-get install -y postgresql-client

# Define the default command to run when the container starts
CMD ["bash"]
