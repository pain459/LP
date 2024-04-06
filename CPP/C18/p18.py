# Regex to retrieve date of births from the string
import re
str = 'name1 1 1-5-2001, name2 2 22-10-1990, name3 3 15-09-2000'
result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)
print(result)
