# Find 5 character words using re.search

import re

str = 'one two three four five six seven'
result = re.search(r'\b\w{5}\b', str)

print(result.group())  # just three as output as re.search will give the first result only.