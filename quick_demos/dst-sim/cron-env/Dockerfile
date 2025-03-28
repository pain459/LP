FROM ubuntu:22.04

RUN apt update && apt install -y cron tzdata

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN echo "* * * * * echo 'Cron running at $(date)' >> /var/log/cron.log" > /etc/cron.d/test-cron
RUN chmod 0644 /etc/cron.d/test-cron
RUN crontab /etc/cron.d/test-cron

ENTRYPOINT ["/entrypoint.sh"]
