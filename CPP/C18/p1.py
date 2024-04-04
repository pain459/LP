import re

str = 'feel pain live pain'
result = re.search(r'p\w\w\w', str)

print(result.group())