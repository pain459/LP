from flask import Flask, request, jsonify
import redis
import json
from snowflake_generator import SnowflakeIDGenerator
import threading
import time

app = Flask(__name__)

# Redis setup
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

# Snowflake ID generator for the master node
master_generator = SnowflakeIDGenerator(node_id=0)

# Number of workers
NUM_WORKERS = 12

@app.route('/generate_ids', methods=['POST'])
def generate_ids():
    try:
        data = request.get_json()
        num_ids = data.get('num_ids', 1)
        task_id = master_generator.generate_id()
        
        batch_size = 50000  # Adjust this size based on your requirements

        # Calculate the number of IDs each worker should generate in total
        ids_per_worker = num_ids // NUM_WORKERS
        extra_ids = num_ids % NUM_WORKERS

        # Distribute the task to worker nodes in batches
        for i in range(NUM_WORKERS):
            num_ids_for_worker = ids_per_worker + (1 if i < extra_ids else 0)
            for j in range(0, num_ids_for_worker, batch_size):
                current_batch_size = min(batch_size, num_ids_for_worker - j)
                subtask_id = f"{task_id}-{i}-{j // batch_size}"
                task_data = {'num_ids': current_batch_size, 'subtask_id': subtask_id}
                redis_client.lpush('tasks', json.dumps(task_data))

        # Collect results from workers
        ids = []
        for i in range(NUM_WORKERS):
            num_ids_for_worker = ids_per_worker + (1 if i < extra_ids else 0)
            num_batches = (num_ids_for_worker + batch_size - 1) // batch_size
            for j in range(num_batches):
                subtask_id = f"{task_id}-{i}-{j}"
                while len(ids) < num_ids:
                    result = redis_client.blpop(f'results:{subtask_id}', timeout=10)
                    if result:
                        ids.extend(json.loads(result[1]))
                        break

        return jsonify(ids=ids[:num_ids])
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
