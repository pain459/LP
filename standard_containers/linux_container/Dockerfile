# Use the official Ubuntu base image
FROM ubuntu:latest

# Install Git and Vim
RUN apt-get update && \
    apt-get install -y git vim && \
    apt-get clean

# Set working directory
WORKDIR /workspace

# Default command
CMD ["/bin/bash"]
