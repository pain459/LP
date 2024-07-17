import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('crawled_data.csv')

# Display the first few rows of the DataFrame
print("First few rows of the dataset:")
print(df.head())

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# Count the number of unique URLs
unique_urls = df['URL'].nunique()
print(f"\nNumber of unique URLs: {unique_urls}")

# Count the occurrences of each title
title_counts = df['Title'].value_counts()
print("\nTitle counts:")
print(title_counts)

# Find the most common words in the titles
word_counts = pd.Series(' '.join(df['Title']).lower().split()).value_counts()[:10]
print("\nMost common words in titles:")
print(word_counts)

# Plotting the most common words (requires matplotlib)
import matplotlib.pyplot as plt

word_counts.plot(kind='bar', title='Most Common Words in Titles')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.show()
