#!/bin/bash

# Ensure log file exists
touch /var/log/cron.log

# Start cron service
service cron start

# Keep container running by tailing the log file
tail -f /var/log/cron.log

echo "Startup: $(date)" >> /var/log/cron.log
