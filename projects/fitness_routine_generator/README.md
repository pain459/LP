Sample payload

{
  "goal": "build muscle",
  "fitness_level": "intermediate",
  "workout_preference": "strength training",
  "available_equipment": ["dumbbells", "bodyweight"],
  "time_per_day": 45,
  "days_per_week": 5
}



Sample response

{
  "plan": [
    {
      "day": "Monday",
      "exercises": [
        {
          "name": "Dumbbell Bench Press",
          "sets": 4,
          "reps": 10,
          "rest": "60 seconds",
          "video": "https://link_to_video.com"
        },
        {
          "name": "Bodyweight Push-ups",
          "sets": 3,
          "reps": 15,
          "rest": "45 seconds",
          "video": "https://link_to_video.com"
        }
      ]
    },
    ...
  ],
  "schedule": "4-week program",
  "notes": "Rest days on Wednesday and Sunday."
}


Sample call

curl -X 'POST' \
  'http://localhost:8000/generate-workout' \
  -H 'Content-Type: application/json' \
  -d '{
  "goal": "build muscle",
  "fitness_level": "intermediate",
  "workout_preference": "strength training",
  "available_equipment": ["dumbbells", "bodyweight"],
  "time_per_day": 45,
  "days_per_week": 5
}'

