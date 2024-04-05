# Retrieve all words with 3 to 5 characters
import re

str = 'one two three four five six seven 6 7 8 99'

result = re.findall(r'\b\w{3,5}\b', str)
print(result)