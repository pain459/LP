import re

str = 'feel pain tell pain know pain'
result = re.findall(r'p\w\w\w', str)
print(result)