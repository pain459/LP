# using groupby from itertools. Basically using length of string as key.

import itertools

# Example list of words
words = ['apple', 'banana', 'kiwi', 'orange', 'pear']

grouped_words = {length: list(group) for length, group in itertools.groupby(sorted(words, key=len), key=len)}

print(grouped_words)