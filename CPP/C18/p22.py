# regex to retrieve marks and names from the given string.
import re

str = 'Rahul got 75 marks, Vijay got 55 marks, where as Subbu got 98 marks.'

# extract only marks having 2 digits.
marks = re.findall(r'\d{2}', str)
print(marks)
# Extract starting with a capital letter and remaining alphabetic characters
names = re.findall(r'[A-Z][a-z]*', str)
print(names)