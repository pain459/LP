FROM postgres:latest

ENV POSTGRES_DB=hospital_data_warehouse
ENV POSTGRES_USER=warehouse_admin
ENV POSTGRES_PASSWORD=warehouse_password

COPY init.sql /docker-entrypoint-initdb.d/
