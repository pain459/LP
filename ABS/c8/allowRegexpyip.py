import pyinputplus as pyip

response = pyip.inputInt(allowRegexes=[r'(I|V|X|L|C|D|M)', r'ZERO'])
print(response)