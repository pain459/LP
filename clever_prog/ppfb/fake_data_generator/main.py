import logging
from fastapi import FastAPI, Query
from faker import Faker
import pandas as pd
import time

app = FastAPI()
fake = Faker()

# Configure logging
logging.basicConfig(filename='backend_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.get("/api/generate_profiles/")
def generate_profiles(num_records: int = Query(default=10, ge=1, le=100)):
    # Log the requested number of records
    logging.info(f"Requested {num_records} profiles generation")

    # Start time
    start_time = time.time()

    # Generate profiles
    data = []
    for _ in range(num_records):
        profile = {
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "job": fake.job(),
            # Add more fields as needed based on your requirements
        }
        data.append(profile)

    df = pd.DataFrame(data)

    # Log the time taken to complete the task
    end_time = time.time()
    duration = end_time - start_time
    logging.info(f"Task completed in {duration:.4f} seconds")

    # Log the created records information
    logging.info(f"Created profiles:\n{df.to_string(index=False)}")

    return df.to_dict(orient="records")
