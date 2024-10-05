from fastapi import FastAPI

app = FastAPI()

# Welcome message route
@app.get("/")
async def welcome():
    return {"message": "Welcome to the FastAPI Airport Dashboard"}

# DB connectivity check (dummy for now)
@app.get("/check-db")
async def check_db():
    # Here we will implement actual DB check later
    return {"message": "DB connectivity check route"}
