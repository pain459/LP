from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder \
    .appName("ETL Example") \
    .master("spark://localhost:7077") \
    .getOrCreate()

# Define the ETL process as a function
def perform_etl():
    # Read the CSV file into a DataFrame
    sales_df = spark.read.csv("hdfs://spark-master:9000/data/sales_data.csv", header=True, inferSchema=True)

    # Perform transformations: filter and aggregate
    product_sales = sales_df.groupBy("Product") \
                            .agg({"Price": "sum", "Quantity": "sum"}) \
                            .withColumnRenamed("sum(Price)", "Total_Price") \
                            .withColumnRenamed("sum(Quantity)", "Total_Quantity")

    # Select relevant columns and reorder
    product_sales = product_sales.select("Product", "Total_Price", "Total_Quantity")

    # Show the transformed data
    product_sales.show()

    # Write the transformed data to a new CSV file
    product_sales.write.csv("hdfs://spark-master:9000/data/product_sales_summary.csv", header=True, mode="overwrite")

# Call the ETL function
perform_etl()

# Stop the SparkSession
spark.stop()
