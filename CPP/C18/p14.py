# Retrieve last word of the string if it starts with t
import re

str = 'one two three four five six twenty'
result = re.findall(r'\bt[\w]*\Z', str)  # \Z matches only the end of the string.
print(result)