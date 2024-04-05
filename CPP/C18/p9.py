# retrieve the words having 3 character length
import re

str = 'one two three four five six seven'
result = re.findall(r'\b\w{5}\b', str)
print(result)