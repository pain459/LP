import pyinputplus as pyip

response = pyip.inputInt('Will allow roman or integer: ', allowRegexes=[r'i|v|x|l|c|d|m', r'zero'])
print(f'Response is {response}')