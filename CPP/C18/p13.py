# create regex to retrieve only single digits from the string
import re
str = 'one two three four five six seven 6 7 8 99'
result = re.findall(r'\b\d\b', str)
print(result)