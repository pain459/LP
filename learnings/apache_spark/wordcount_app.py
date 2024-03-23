from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("WordCount") \
    .getOrCreate()

# Read input text file
lines = spark.sparkContext.textFile("pride_and_prejudice.txt")

# Split each line into words
words = lines.flatMap(lambda line: line.split())

# Count the occurrence of each word
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# Print the word counts
for word, count in word_counts.collect():
    print(f"{word}: {count}")

# Stop SparkSession
spark.stop()
