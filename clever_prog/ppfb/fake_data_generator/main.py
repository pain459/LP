from fastapi import FastAPI
from faker import Faker
import pandas as pd

app = FastAPI()
fake = Faker()

@app.get("/generate_profiles/")
def generate_profiles(num_records: int = 10):
    data = [fake.profile() for _ in range(num_records)]
    df = pd.DataFrame(data)
    return df.to_dict(orient="records")
