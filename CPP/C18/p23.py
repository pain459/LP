# Regex to retrieve the times either am or pm
import re

str = 'The meeting may be at 8am or 9am or 4pm or 5pm'
result = re.findall(r'\dam|\dpm', str)
print(result)