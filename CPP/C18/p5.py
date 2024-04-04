# program to split a string into pieces for every non alpha numeric char
import re

str = 'This; is the: "Core" Python\'s book'
result = re.split(r'\W+', str)
print(result)