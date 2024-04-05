# regex to retrieve all words starting with 'k' in a given string
import re

str = 'deidara hidan itachi juzo kakuzu kisame konan ktes tkra orochimaru sasori tobi zetsu'
result = re.findall(r'k[\w]*', str)
print(result)

# to add space before and after the word selection which eliminates false matches
result = re.findall(r'\bk[\w]*\b', str)
print(result)