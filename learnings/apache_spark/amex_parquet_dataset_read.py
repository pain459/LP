from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("AMEX Dataset Analysis") \
    .getOrCreate()

# Path to the AMEX Parquet dataset file
dataset_path = "path/to/AMEX_dataset.parquet"

# Read the dataset into a DataFrame
df = spark.read.parquet(dataset_path)

# Show the schema of the DataFrame
print("Schema:")
df.printSchema()

# Show the first few rows of the DataFrame
print("Sample Data:")
df.show(5)

# Perform some basic analysis
print("Basic Statistics:")
# Example: Calculate the number of rows in the dataset
row_count = df.count()
print("Number of Rows:", row_count)

# Example: Calculate the average value of a numeric column
# Replace "numeric_column" with the name of a numeric column in your dataset
avg_numeric_value = df.selectExpr("avg(numeric_column)").collect()[0][0]
print("Average Numeric Value:", avg_numeric_value)

# Example: Calculate the distinct values in a categorical column
# Replace "categorical_column" with the name of a categorical column in your dataset
distinct_values = df.select("categorical_column").distinct().count()
print("Distinct Values in Categorical Column:", distinct_values)

# Stop SparkSession
spark.stop()
