# A class to handle deposits and withdrawals in a bank.
import sys


class Bank(object):
    """Bank related transactions"""

    # to initialize name and balance instance vars
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    # To add deposit amount to balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # To deduct withdrawal from balance
    def withdrawal(self, amount):
        if amount > self.balance:
            print('Balance amount is less. No withdrawal is allowed.')
        else:
            self.balance -= amount
        return self.balance


# Use the Bank class
# Create an account with the given name and balance 0.00
name = input("Enter name:")
b = Bank(name)

while True:
    print(f'Hello {b.name}')
    print('d -deposit, w -withdrawal, e -Exit')
    choice = input('Your choice: ')
    if choice == 'e' or choice == 'E':
        sys.exit(1)
    amt = float(input('Enter amount: '))
    if choice == 'd' or choice == 'D':
        print(f'Balance after deposit {b.deposit(amt)}')
    elif choice == 'w' or choice == 'W':
        print(f'Balance after withdrawal {b.withdrawal(amt)}')
