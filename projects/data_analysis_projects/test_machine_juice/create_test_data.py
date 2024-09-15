import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
from multiprocessing import Pool, cpu_count

# Initialize Faker for generating fake data
fake = Faker()

# Helper function to generate random timestamps over the past 5 years
def random_date():
    start_date = datetime.now() - timedelta(days=365*5)
    random_days = random.randint(0, 365*5)
    return start_date + timedelta(days=random_days, seconds=random.randint(0, 86400))

# Function to generate a chunk of the dataset
def generate_data_chunk(n_rows):
    customer_ids = np.random.randint(1, 10000000, size=n_rows)
    transaction_dates = [random_date() for _ in range(n_rows)]
    product_ids = np.random.randint(1, 500000, size=n_rows)
    product_categories = np.random.choice([f"Category_{i}" for i in range(1, 51)], size=n_rows)
    prices = np.round(np.random.uniform(1, 10000, size=n_rows), 2)
    quantities = np.random.randint(1, 100, size=n_rows)
    total_transaction_amounts = prices * quantities
    customer_locations = [fake.country() for _ in range(n_rows)]
    payment_methods = np.random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Cash'], size=n_rows)
    discount_applied = np.random.choice([True, False], size=n_rows)
    customer_feedback = np.round(np.random.uniform(-1, 1, size=n_rows), 2)
    delivery_times = np.random.randint(1, 30, size=n_rows)
    
    return pd.DataFrame({
        'Customer_ID': customer_ids,
        'Transaction_Date': transaction_dates,
        'Product_ID': product_ids,
        'Product_Category': product_categories,
        'Price': prices,
        'Quantity_Purchased': quantities,
        'Total_Transaction_Amount': total_transaction_amounts,
        'Customer_Location': customer_locations,
        'Payment_Method': payment_methods,
        'Discount_Applied': discount_applied,
        'Customer_Feedback': customer_feedback,
        'Delivery_Time': delivery_times
    })

# Function to run the data generation in parallel
def generate_large_dataset(n_rows, n_cores):
    # Determine the number of rows per core
    rows_per_core = n_rows // n_cores
    
    # Create a multiprocessing pool
    with Pool(n_cores) as pool:
        # Assign each core a chunk of rows to process
        chunk_sizes = [rows_per_core] * n_cores
        # If there are leftover rows, assign them to the last core
        leftover = n_rows % n_cores
        if leftover > 0:
            chunk_sizes[-1] += leftover
        
        # Generate data in parallel
        data_chunks = pool.map(generate_data_chunk, chunk_sizes)
    
    # Combine all the data chunks into a single DataFrame
    return pd.concat(data_chunks, ignore_index=True)

# Number of rows to generate
n_rows = 100000000  # 100 million rows
# Number of cores to use (you can get the number of available cores on your machine)
n_cores = cpu_count()

# Generate the dataset using multiprocessing
df = generate_large_dataset(n_rows, n_cores)

# Display the first few rows of the generated dataset
print(df.head())

# Optionally, save the dataset to a CSV file (uncomment the line below if you wish to save the file)
df.to_csv("large_ecommerce_dataset_parallel.csv", index=False)
