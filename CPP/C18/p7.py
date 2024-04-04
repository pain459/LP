# regex to retrieve all words starting with 'k' in a given string
import re

str = 'deidara hidan itachi juzo kakuzu kisame konan orochimaru sasori tobi zetsu'
result = re.findall(r'k[\w]*', str)
print(result)