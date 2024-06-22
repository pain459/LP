from locust import HttpUser, TaskSet, task, between

class GenerateIDsTaskSet(TaskSet):
    
    @task
    def generate_ids(self):
        headers = {'Content-Type': 'application/json'}
        data = {
            "num_ids": 100000
        }
        self.client.post("/generate_ids", json=data, headers=headers)

class WebsiteUser(HttpUser):
    tasks = [GenerateIDsTaskSet]
    wait_time = between(1, 5)  # wait between 1 and 5 seconds between tasks
