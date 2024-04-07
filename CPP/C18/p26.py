# filter the file items.html and retrive the information

import re
import urllib.request

file_path = 'items.html'

# Open the html file with urlopen() method
with open(file_path, 'r') as f:
    html_content = f.read()


print(html_content)
result = re.findall(r'<td>(.*?)<\/td>\s*<td>(.*?)<\/td>\s*<td>(.*?)<\/td>', html_content)

print(result)
for i, j, k in result:
    print(f'Item = {2}          Price = {k}')