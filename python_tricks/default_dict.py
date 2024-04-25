# using default dict to count the occurence of a character in a string.

from collections import defaultdict

text = 'antikythera'

char_count = defaultdict(int)

for i in text:
    char_count[i] += 1

print(char_count)