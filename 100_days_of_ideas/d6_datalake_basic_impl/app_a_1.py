from flask import Flask, jsonify
import random
import time
import os
import json
from datetime import datetime
from threading import Lock, Timer

app = Flask(__name__)

DATALAKE_DIR = 'datalake'
BATCH_SIZE = 10          # how many metrics to accumulate before writing
FLUSH_INTERVAL = 30.0    # in seconds, how often to flush if batch not reached

metrics_buffer = []
buffer_lock = Lock()
flush_timer = None

def ensure_partition_dirs():
    # Create partition directories based on current date: YYYY/MM/DD
    today = datetime.utcnow().strftime('%Y/%m/%d')
    partition_path = os.path.join(DATALAKE_DIR, today)
    if not os.path.exists(partition_path):
        os.makedirs(partition_path)
    return partition_path

def start_flush_timer():
    global flush_timer
    if flush_timer is not None:
        flush_timer.cancel()
    flush_timer = Timer(FLUSH_INTERVAL, flush_metrics)
    flush_timer.start()

def flush_metrics():
    """Flush in-memory metrics to a file in the datalake partition."""
    global metrics_buffer
    with buffer_lock:
        if not metrics_buffer:
            return  # nothing to flush

        partition_path = ensure_partition_dirs()
        # We'll append metrics to a daily JSON lines file
        # Example file name: metrics_YYYY-MM-DD.jsonl
        filename = 'metrics_{}.jsonl'.format(datetime.utcnow().strftime('%Y-%m-%d'))
        filepath = os.path.join(partition_path, filename)

        # Append each metric as a JSON line
        with open(filepath, 'a') as f:
            for metric in metrics_buffer:
                f.write(json.dumps(metric) + '\n')

        # Clear the buffer
        metrics_buffer = []

    # restart timer for next flush
    start_flush_timer()

@app.route('/log_metric', methods=['GET'])
def log_metric():
    metric_status = random.choice(["up", "down"])
    timestamp = int(time.time())
    metric_record = {
        "timestamp": timestamp,
        "status": metric_status
    }

    with buffer_lock:
        metrics_buffer.append(metric_record)
        # If we reached our batch size, flush immediately
        if len(metrics_buffer) >= BATCH_SIZE:
            flush_metrics()
        else:
            # If timer isn't running, start it
            if flush_timer is None:
                start_flush_timer()

    return jsonify({"message": "Metric buffered", "metric": metric_record})

if __name__ == '__main__':
    if not os.path.exists(DATALAKE_DIR):
        os.makedirs(DATALAKE_DIR)
    start_flush_timer()  # start flush timer when app starts
    app.run(host='0.0.0.0', port=5000)
