words = []

with open('economics.txt', 'r') as f:
    for line in f:
        words.extend(line.split())

print(words) # This will split the line into words and form a list out of it.

from collections import Counter
counts = Counter(words)
top5 = counts.most_common(5)
print(top5)