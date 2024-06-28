# FROM apache/airflow:2.2.4-python3.8

# USER root

# RUN apt-get update && apt-get install -y \
#     postgresql-client \
#     netcat-traditional

# USER airflow

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY dags /opt/airflow/dags
# COPY wait-for-it.sh /wait-for-it.sh
# COPY entrypoint.sh /entrypoint.sh

# ENTRYPOINT ["/wait-for-it.sh", "postgres_warehouse", "5432", "--", "entrypoint.sh"]


FROM apache/airflow:2.2.4-python3.8

USER root

RUN apt-get update && apt-get install -y \
    postgresql-client \
    netcat-traditional

USER airflow

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dags /opt/airflow/dags
COPY wait-for-it.sh /wait-for-it.sh
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
