# Use a base image with a Linux distribution of your choice
FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    openssh-server \
    iproute2 \
    net-tools \
    procps \
    lshw \
    pciutils \
    usbutils \
    && rm -rf /var/lib/apt/lists/*

# Install paramiko library
RUN pip3 install paramiko

# Expose SSH port
EXPOSE 22

# Copy the script files into the container
COPY collect_stats.py /usr/src/app/
COPY wrapper.py /usr/src/app/

# Set working directory
WORKDIR /usr/src/app
