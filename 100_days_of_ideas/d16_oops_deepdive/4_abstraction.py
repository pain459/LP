"""
Abstraction hides implementation details and exposes only essential behaviour, often achieved using abstrac base classes.
"""

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing credit card payment of {amount}"


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing PayPal payment {amount}"
    

# Usage
processors = [CreditCardProcessor(), PayPalProcessor()]
for processor in processors:
    print(processor.process_payment(100))