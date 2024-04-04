import re

str = 'one two three four'
result = re.match(r't\w\w', str)
print(result)  # wont print anything as this search for first words only
