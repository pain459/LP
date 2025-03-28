FROM alpine:latest
RUN apk add --no-cache chrony

COPY custom_ntpd.conf /etc/chrony/chrony.conf

CMD ["chronyd", "-d", "-f", "/etc/chrony/chrony.conf"]
