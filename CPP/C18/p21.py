# regex to search the ending of the string by ignoring case.
import re

str = 'Hello World'
result = re.search(r'world$', str, re.IGNORECASE)
# print(result)
if result:
    print('String ends with world!')
else:
    print('String doesn\'t ends with world!')