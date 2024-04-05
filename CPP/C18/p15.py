# regex to retrieve phone number
import re
str = 'candidate1, 9848022338'
result = re.findall(r'\b\d+', str)
print(result)