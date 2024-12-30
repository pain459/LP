class BankAccount:
    interest_rate = 0.03  # Class-level attribute

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


    @staticmethod
    def calculate_interest(balance):
        """Utility method to calculate interest on a given balance."""
        return balance * BankAccount.interest_rate
    

    @classmethod
    def create_with_default_balance(cls, name):
        """Alternative constructor to create accounts with a default balance"""
        default_balance = 1000
        return cls(name, default_balance)
    

# Example Uage
# Using the static method
interest = BankAccount.calculate_interest(5000)
print(f"Interest on 5000: {interest}")


# Using the class method
account = BankAccount.create_with_default_balance("Alice")
print(account.name)
print(account.balance)