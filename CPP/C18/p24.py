# Find email addresses in the given text file

import re

with open('mails.txt', 'r') as f:
    for i in f:
        # print(i)
        res = re.findall(r'\S+@\S+', i)
    print(res)