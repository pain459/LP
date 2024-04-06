# Regex to find if the string starts with He or now
import re

str = 'Hello World!'
result = re.search(r'^He', str)
# print(result.group())
if result:
    print('String starts with He.')
else:
    print('String doesn\'t start with He.')