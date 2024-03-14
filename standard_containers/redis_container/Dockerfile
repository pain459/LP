FROM redis:latest
LABEL authors="pain"

# Variables
ENV REDIS_PORT 6379

# Create a new user
RUN useradd -ms /bin/bash redis_user

# set ownership of /data to newly created user
RUN chown -R redis_user:redis_user /data

# set Redis to run as the new user
USER redis_user

# Expose redis port
EXPOSE $REDIS_PORT

# Start redis server
CMD ["redis-server", "--protected-mode", "no"]