from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("WordCount") \
    .master("spark://172.18.0.2:7077").getOrCreate()  # Spark master URL

# Path to the input text file
input_file_path = "pride_and_prejudice.txt"

# Read input text file into a DataFrame
lines = spark.read.text(input_file_path).rdd.map(lambda r: r[0])

# Split each line into words
words = lines.flatMap(lambda line: line.split())

# Count the occurrence of each word
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# Collect the word counts and print them
for word, count in word_counts.collect():
    print(f"{word}: {count}")

# Stop SparkSession
spark.stop()
