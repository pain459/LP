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

# Set root password
RUN echo 'root:password' | chpasswd

# Permit root login via SSH
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Start SSH server in the background
CMD /usr/sbin/sshd -D -e -f /etc/ssh/sshd_config & tail -f /dev/null
