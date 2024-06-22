import redis
import json
import sys
import logging
from snowflake_generator import SnowflakeIDGenerator

# Redis setup
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

# Worker node setup (Node ID should be passed as an argument)
node_id = int(sys.argv[1])
worker_generator = SnowflakeIDGenerator(node_id=node_id)

# Logging setup
log_filename = f'worker_{node_id}.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger()

def process_tasks():
    while True:
        task = redis_client.brpop('tasks', timeout=10)
        if task:
            task_data = json.loads(task[1])
            num_ids = task_data['num_ids']
            subtask_id = task_data['subtask_id']
            
            # Generate IDs
            ids = [worker_generator.generate_id() for _ in range(num_ids)]
            
            # Push results back to Redis
            redis_client.lpush(f'results:{subtask_id}', json.dumps(ids))

            # Log the number of IDs generated
            logger.info(f"Generated {len(ids)} unique IDs for subtask {subtask_id}")

if __name__ == '__main__':
    process_tasks()
