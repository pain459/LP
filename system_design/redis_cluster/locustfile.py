from locust import User, task, between, constant_pacing
import redis

class RedisLoadTestUser(User):
    wait_time = constant_pacing(1)

    def on_start(self):
        # Connect to Redis
        self.client = redis.StrictRedis(
            host='localhost',  # Replace with the appropriate host if needed
            port=6379,
            password='your_password',
            decode_responses=True
        )

    @task
    def set_get_delete(self):
        # Perform a set operation
        self.client.set('locust_key', 'locust_value')
        
        # Perform a get operation
        value = self.client.get('locust_key')
        
        # Perform a delete operation
        self.client.delete('locust_key')

# No need to specify a host since we are not using HTTP requests
