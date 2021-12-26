from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = eval(input("Enter the amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
print(f'{from_currency} TO {to_currency} {amount}')
result = c.convert(from_currency, to_currency, amount)
print(result)