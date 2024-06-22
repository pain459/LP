from flask import Flask, request, jsonify
import redis
import json
from snowflake_generator import SnowflakeIDGenerator

app = Flask(__name__)

# Redis setup
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

# Snowflake ID generator for the master node
master_generator = SnowflakeIDGenerator(node_id=0)

@app.route('/generate_ids', methods=['POST'])
def generate_ids():
    try:
        data = request.get_json()
        num_ids = data.get('num_ids', 1)
        task_id = master_generator.generate_id()
        
        # Distribute the task to worker nodes
        task_data = {'num_ids': num_ids, 'task_id': task_id}
        redis_client.lpush('tasks', json.dumps(task_data))
        
        # Collect results from workers
        ids = []
        while len(ids) < num_ids:
            result = redis_client.blpop(f'results:{task_id}', timeout=10)
            if result:
                ids.extend(json.loads(result[1]))
        
        return jsonify(ids=ids)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
