# Find if the string is ending with world

import re
str = 'Hello World!'
result = re.search(r'World!$', str)

# print(result)
if result:
    print('String ends with World!')
else:
    print('String doesn\'t end with world')