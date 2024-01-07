import logging
from fastapi import FastAPI, Query
from faker import Faker
import pandas as pd

app = FastAPI()
fake = Faker()

# Configure logging
logging.basicConfig(filename='backend_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.get("/generate_profiles/")
def generate_profiles(num_records: int = Query(default=10, ge=1, le=100)):
    # Log the requested number of records
    logging.info(f"Requested {num_records} profiles generation")

    # Generate profiles
    data = [fake.profile() for _ in range(num_records)]
    df = pd.DataFrame(data)

    # Log the created records information
    logging.info(f"Created profiles:\n{df.to_string(index=False)}")

    return df.to_dict(orient="records")
