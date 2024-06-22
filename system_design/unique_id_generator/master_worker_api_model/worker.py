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
    batch_size = 500  # Maximum batch size

    while True:
        task = redis_client.brpop('tasks', timeout=3600)
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
                logger.info(f"Generated {len(ids)} unique IDs for subtask {subtask_id}")

if __name__ == '__main__':
    process_tasks()
