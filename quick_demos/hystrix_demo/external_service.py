import random

class ExternalService:
    def call(self):
        if random.choice([True, False]):
            raise Exception("Service failure")
        return "Success"
