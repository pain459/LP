from prometheus_client import start_http_server, Gauge
import time

etl_duration = Gauge('etl_duration_seconds', 'Duration of the ETL pipeline in seconds')

def monitor_etl_pipeline(etl_function):
    start_time = time.time()
    etl_function()
    duration = time.time() - start_time
    etl_duration.set(duration)
