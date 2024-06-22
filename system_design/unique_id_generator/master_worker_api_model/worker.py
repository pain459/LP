import redis
import json
import sys
import logging
from snowflake_generator import SnowflakeIDGenerator
from opensearchpy import OpenSearch
import time

# Redis setup
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

# Worker node setup (Node ID should be passed as an argument)
node_id = int(sys.argv[1])
worker_generator = SnowflakeIDGenerator(node_id=node_id)

# OpenSearch setup with retry logic
def connect_to_opensearch():
    while True:
        try:
            opensearch_client = OpenSearch(
                hosts=[{'host': 'opensearch', 'port': 9200}],
                http_auth=('admin', 'admin'),  # Replace with your OpenSearch credentials
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
log_type = "_doc"

def log_to_opensearch(message):
    log_entry = {
        "message": message,
        "node_id": node_id,
        "timestamp": int(time.time() * 1000)
    }
    opensearch_client.index(index=log_index, body=log_entry)

def process_tasks():
    batch_size = 500  # Maximum batch size

    while True:
        task = redis_client.brpop('tasks', timeout=10)
        if task:
            task_data = json.loads(task[1])
            total_num_ids = task_data['num_ids']
            subtask_id = task_data['subtask_id']
            
            # Process in batches
            for i in range(0, total_num_ids, batch_size):
                current_batch_size = min(batch_size, total_num_ids - i)
                
                # Generate IDs
                ids = [worker_generator.generate_id() for _ in range(current_batch_size)]
                
                # Push results back to Redis
                redis_client.lpush(f'results:{subtask_id}', json.dumps(ids))
                
                # Log the number of IDs generated
                log_to_opensearch(f"Generated {len(ids)} unique IDs for subtask {subtask_id}")

if __name__ == '__main__':
    log_to_opensearch("Worker started")
    process_tasks()
