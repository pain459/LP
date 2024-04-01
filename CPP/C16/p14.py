# user defined exceptions
# Create your own class as sub class to Exception class
class MyException(Exception):
    def __init__(self, arg):
        self.msg = arg


# Write code where exception may raise
def check(dict):
    for k, v in dict.items():
        print(f'Name = {k}  Balance = {v}')
        if v < 2000.00:
            raise MyException(f'Balance amount is less in the account of {k}')


# Our own exception is handled using try and except blocks.
bank = {'A': 2500, 'B': 3500, 'C': 1500}
try:
    check(bank)
except MyException as e:
    print(e)
