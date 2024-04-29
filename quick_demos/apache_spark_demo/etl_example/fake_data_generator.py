from faker import Faker
import csv
import random
from datetime import datetime, timedelta

fake = Faker()

# Generate fake sales data
def generate_sales_data(num_records):
    data = []
    for _ in range(num_records):
        date = fake.date_between(start_date='-30d', end_date='today').strftime('%Y-%m-%d')
        product = fake.word().capitalize()
        price = round(random.uniform(10.0, 100.0), 2)
        quantity = random.randint(1, 10)
        data.append([date, product, price, quantity])
    return data

# Write generated data to CSV file
def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Product', 'Price', 'Quantity'])
        writer.writerows(data)

# Generate 1000 fake sales records
sales_data = generate_sales_data(1000)

# Write generated data to CSV file
write_to_csv(sales_data, 'sales_data.csv')
