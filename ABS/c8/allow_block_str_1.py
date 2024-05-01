import pyinputplus as pyip

response = pyip.inputStr('Don\'t enter taboo word: ',
                         allowRegexes=[r'caterpillar', r'category'],
                         blockRegexes=[r'cat'])

print(f'You entered {response}')