# using match method
import re

str = 'deidara hidan itachi juzo kakuzu kisame konan orochimaru sasori tobi zetsu'
result = re.findall(r'j[\w]*', str)
print(result)

str2 = 'fun bun gun sun'
result = re.match(r'f\w\w', str2)  # Will only return the results if it is in the beginning.
print(result.group())