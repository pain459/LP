import pyinputplus as pyip

response = pyip.inputInt('Enter a number, except (2468): ', blockRegexes=[r'[2468]$'])
print(f'Response is {response}')