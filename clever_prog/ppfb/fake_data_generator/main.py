from fastapi import FastAPI, Query
from faker import Faker
import pandas as pd

app = FastAPI()
fake = Faker()

@app.get("/generate_profiles/")
def generate_profiles(num_records: int = Query(default=10, ge=1, le=100)):
    data = [fake.profile() for _ in range(num_records)]
    df = pd.DataFrame(data)
    return df.to_dict(orient="records")
