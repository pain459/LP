from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, validator
import re
from app.db import create_db_and_tables, get_db
import aiomysql

app = FastAPI()

# Pydantic model for validating the flight data
class FlightCreate(BaseModel):
    flight_number: str
    from_location: str
    to_location: str
    status: str
    next_update: str

    @validator('next_update')
    def validate_next_update(cls, v):
        # Ensure next_update is in HHMM format
        if not re.match(r'^[0-2][0-9][0-5][0-9]$', v):
            raise ValueError("next_update must be in HHMM format")
        return v

# Initialize the database when the application starts
@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()

# Welcome message route
@app.get("/")
async def welcome():
    return {"message": "Welcome to the FastAPI Airport Dashboard"}

# CRUD API: Create a flight entry with HHMM validation
@app.post("/flights/")
async def create_flight(flight: FlightCreate, db: aiomysql.Connection = Depends(get_db)):
    async with db.cursor() as cursor:
        await cursor.execute(
            "INSERT INTO flights (flight_number, from_location, to_location, status, next_update) VALUES (%s, %s, %s, %s, %s)",
            (flight.flight_number, flight.from_location, flight.to_location, flight.status, flight.next_update)
        )
    await db.commit()
    return {"message": "Flight created successfully"}

# CRUD API: Read all flights
@app.get("/flights/")
async def get_flights(db: aiomysql.Connection = Depends(get_db)):
    async with db.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute("SELECT * FROM flights")
        flights = await cursor.fetchall()
    return {"flights": flights}

# CRUD API: Update a flight's status and next_update
@app.put("/flights/{flight_id}")
async def update_flight(flight_id: int, flight: FlightCreate, db: aiomysql.Connection = Depends(get_db)):
    async with db.cursor() as cursor:
        await cursor.execute(
            "UPDATE flights SET status = %s, next_update = %s WHERE id = %s",
            (flight.status, flight.next_update, flight_id)
        )
    await db.commit()
    return {"message": "Flight updated successfully"}

# CRUD API: Delete a flight
@app.delete("/flights/{flight_id}")
async def delete_flight(flight_id: int, db: aiomysql.Connection = Depends(get_db)):
    async with db.cursor() as cursor:
        await cursor.execute("DELETE FROM flights WHERE id = %s", (flight_id,))
    await db.commit()
    return {"message": "Flight deleted successfully"}
