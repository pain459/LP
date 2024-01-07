import logging
from fastapi import FastAPI, Query, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from faker import Faker
import pandas as pd
import time
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
fake = Faker()
security = HTTPBasic()

# Username and password for authentication
USERNAME = "user"
PASSWORD = "password"

# Configure logging
logging.basicConfig(filename='backend_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:8080",
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = credentials.username == USERNAME
    correct_password = credentials.password == PASSWORD
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True

@app.get("/api/generate_profiles/")
def generate_profiles(authenticated: bool = Depends(authenticate_user), num_records: int = Query(default=10, ge=1, le=100)):
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
