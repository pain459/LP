# Words starting with words an or ak
import re
str = 'akatsuki adam antony andy'
result = re.findall(r'a[nk][\w]*', str)
print(result)