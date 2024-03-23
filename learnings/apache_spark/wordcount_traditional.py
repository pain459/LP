# Read input text file
with open("pride_and_prejudice.txt", "r") as file:
    lines = file.readlines()

# Initialize an empty dictionary to store word counts
word_counts = {}

# Iterate over each line
for line in lines:
    # Split the line into words
    words = line.split()
    # Iterate over each word
    for word in words:
        # Update word count in the dictionary
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

# Print the word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")
