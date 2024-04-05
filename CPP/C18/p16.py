# retrieve only name but not number in the string
import re
str = 'candidate1: 9848022338'
result = re.findall(r'\D+', str)
print(result[0])