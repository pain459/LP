from collections import Counter

example_list = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 2, 2, 21, 1, 4, 4, 4]

# Use counter to count the occurences of elements
counter = Counter(example_list)

# Find the most common elements
most_common_elements = counter.most_common()

# print the result
print("Most common elements:")
for element, count in most_common_elements:
    print(f'{element} {count} times')