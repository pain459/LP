import re

str = 'Six paths of pain includes Rin'
result = re.sub('Rin', 'Nagato', str)
print(result)

# Splitting the result
result = re.split(r'\W+', result)
print(result[-1])