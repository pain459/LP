# search the word which starts with a number and space to start with
import re

str = 'The 21st century fox production presents its 170th movie on 12th this month.'

result = re.findall(r'\b\d[\w]*\b', str) # \b for space \d for number [\w]* for all alphanumerical and \b for space
print(result)