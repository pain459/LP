# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from planner import generate_workout_plan

app = FastAPI()

class WorkoutRequest(BaseModel):
    goal: str
    fitness_level: str
    workout_preference: str
    available_equipment: list
    time_per_day: int
    days_per_week: int

@app.post("/generate-workout")
def create_workout_plan(request: WorkoutRequest):
    return generate_workout_plan(request.dict())

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fitness Routine Generator API!"}
