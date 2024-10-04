# app/planner.py
import random
from workout_db import exercises_db

def generate_workout_plan(user_data):
    goal = user_data['goal']
    fitness_level = user_data['fitness_level']
    available_equipment = user_data['available_equipment']
    time_per_day = user_data['time_per_day']
    days_per_week = user_data['days_per_week']

    # Create a weekly workout plan
    workout_plan = []

    for day in range(days_per_week):
        day_plan = {"day": f"Day {day + 1}", "exercises": []}
        for _ in range(3):  # Example: 3 exercises per day
            exercise = random.choice(exercises_db)
            if any(equip in exercise['equipment'] for equip in available_equipment):
                day_plan['exercises'].append({
                    "name": exercise['name'],
                    "sets": random.randint(3, 5),
                    "reps": random.randint(8, 15),
                    "rest": f"{random.randint(30, 90)} seconds",
                    "video": exercise.get('video', 'N/A')
                })
        workout_plan.append(day_plan)

    return {"plan": workout_plan, "schedule": f"{days_per_week}-day program"}

