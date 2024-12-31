"""
Encapsulation restricts access to certain attributes or methods to protect the internal state of an object. This is achieved using public, private, or protected access specifiers.
"""

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance  # Private attribute

    
    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit value must be positive!")
        

    def withdraw(self, amount):
        """Public methos to withdraw money"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount!")
        

    def get_balance(self):
        """Public method to access the private balance"""
        return self.__balance
    


# Usage
account = BankAccount("123456", 500)
account.deposit(200)
print(account.get_balance())
account.withdraw(100)
print(account.get_balance())