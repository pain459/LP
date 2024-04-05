# Find the characters which have length of atleast 4 characters
import re

str = 'one two three four five six seven'
result = re.findall(r'\b\w{4,}\b', str)  # atleast \w{4,} translates to search all words with minimum 4 characters.

print(result)
