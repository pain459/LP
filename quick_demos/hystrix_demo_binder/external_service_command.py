import pybreaker

class ExternalServiceCommand:
    def __init__(self, external_service):
        self.external_service = external_service
        self.breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=10)

    def execute(self):
        try:
            return self.breaker.call(self.external_service.call)
        except pybreaker.CircuitBreakerError:
            return "Fallback: Service is unavailable"
        except Exception as e:
            self.breaker._state_storage.increment_counter()
            return "Fallback: Service failed"
