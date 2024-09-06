import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate random datetime
def random_datetime(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def generate_it_service_data(record_count):
    # Define the parameters
    severities = ['critical', 'high', 'medium', 'low']
    services = [f'Service {i+1}' for i in range(10)]  # 10 unique services
    subjects = [
        "Printer not responding", "Paper jam", "Low ink warning", "Cannot connect to printer",
        "Driver installation error", "Slow printing", "Network issues", "Printer spooler error",
        "Cannot print PDF", "Toner not recognized"
    ]

    # Date range for generating timestamps
    start_date = datetime(2023, 1, 1, 9, 0, 0)
    end_date = datetime(2024, 1, 1, 18, 0, 0)

    records = []
    req_number = 100000  # Starting req#

    for _ in range(record_count):  # Generate user-defined number of records
        severity = random.choice(severities)
        subject = random.choice(subjects)
        logged_date = random_datetime(start_date, end_date)
        last_updated = logged_date + timedelta(hours=random.randint(1, 72))  # Last updated within 1-72 hours
        service = random.choice(services)
        
        # Randomly increment req# and allow gaps
        req_number += random.randint(1, 5)  
        
        records.append({
            'severity': severity,
            'req#': req_number,
            'subject': subject,
            'logged_date': logged_date.strftime('%m/%d/%Y %H:%M:%S IST'),
            'last_updated': last_updated.strftime('%m/%d/%Y %H:%M:%S IST'),
            'service': service
        })

    # Convert to DataFrame
    df = pd.DataFrame(records)
    
    # Save the data to a CSV file
    csv_filename = 'generated_it_service_data.csv'
    df.to_csv(csv_filename, index=False)
    print(f"{record_count} records have been generated and saved to {csv_filename}")

# Main program to ask user input for the number of records
if __name__ == "__main__":
    record_count = int(input("Enter the number of records to generate: "))
    generate_it_service_data(record_count)
