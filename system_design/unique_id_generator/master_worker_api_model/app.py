from flask import Flask, request, jsonify
import redis
import json
from snowflake_generator import SnowflakeIDGenerator
import logging
from opensearchpy import OpenSearch
import time
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

# Redis setup
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

# Snowflake ID generator for the master node
master_generator = SnowflakeIDGenerator(node_id=0)

# Number of workers
NUM_WORKERS = 12

# Maximum number of keys that can be generated
MAX_KEYS = 10000000

# OpenSearch setup with retry logic
def connect_to_opensearch():
    while True:
        try:
            opensearch_client = OpenSearch(
                hosts=[{'host': 'opensearch', 'port': 9200}],
                http_auth=('admin', 'admin'),  # Replace with your OpenSearch credentials if necessary
                use_ssl=False,
                verify_certs=False
            )
            return opensearch_client
        except Exception as e:
            print("Error connecting to OpenSearch, retrying in 5 seconds...", e)
            time.sleep(5)

opensearch_client = connect_to_opensearch()

# Logging setup
log_index = "logs"

def log_to_opensearch(message):
    tz = timezone('Asia/Kolkata')  # Replace with your local timezone, e.g., 'America/New_York'
    log_entry = {
        "message": message,
        "timestamp": datetime.now(tz).isoformat()
    }
    opensearch_client.index(index=log_index, body=log_entry)

@app.route('/generate_ids', methods=['POST'])
def generate_ids():
    try:
        data = request.get_json()
        num_ids = data.get('num_ids', 1)

        # Check if the requested number of keys exceeds the limit
        if num_ids > MAX_KEYS:
            error_message = f'Requested number of keys exceeds the limit of {MAX_KEYS}'
            log_to_opensearch(error_message)
            return jsonify({'error': error_message}), 400

        task_id = master_generator.generate_id()

        # Calculate the number of IDs each worker should generate
        ids_per_worker = num_ids // NUM_WORKERS
        extra_ids = num_ids % NUM_WORKERS

        # Distribute the task to worker nodes
        for i in range(NUM_WORKERS):
            subtask_id = f"{task_id}-{i}"
            num_ids_for_worker = ids_per_worker + (1 if i < extra_ids else 0)
            task_data = {'num_ids': num_ids_for_worker, 'subtask_id': subtask_id}
            redis_client.lpush('tasks', json.dumps(task_data))

        # Collect results from workers
        ids = []
        for i in range(NUM_WORKERS):
            subtask_id = f"{task_id}-{i}"
            while len(ids) < num_ids:
                result = redis_client.blpop(f'results:{subtask_id}', timeout=10)
                if result:
                    ids.extend(json.loads(result[1]))
                    break

        log_to_opensearch(f"Generated {num_ids} IDs successfully")
        return jsonify(ids=ids[:num_ids])
    except Exception as e:
        log_to_opensearch(str(e))
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
