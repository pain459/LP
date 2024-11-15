import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Parameters for data generation
num_records = 1000  # Adjust the number of records as needed
product_categories = ['Electronics', 'Furniture', 'Office Supplies', 'Apparel', 'Toys']
regions = ['North', 'South', 'East', 'West']

# Generate data
data = []
for _ in range(num_records):
    # Generate a random date within the last year
    date = fake.date_between(start_date='-1y', end_date='today')
    
    # Randomly select product category and region
    category = random.choice(product_categories)
    region = random.choice(regions)
    
    # Generate a sales amount and units sold
    sales_amount = round(random.uniform(50, 5000), 2)
    units_sold = random.randint(1, 20)
    
    # Append data to the list
    data.append({
        'Date': date,
        'Product Category': category,
        'Region': region,
        'Sales Amount': sales_amount,
        'Units Sold': units_sold
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('sales_data.csv', index=False)
print("Sales data generated and saved to 'sales_data.csv'")
