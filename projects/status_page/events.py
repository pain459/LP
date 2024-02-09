import requests

url = "http://localhost:8000/create_event/"

# Sample event data
event_data = {
    "event": "Sample Event",
    "detail": "This is a sample event created for testing purposes.",
    "status": "Open"
}

response = requests.post(url, json=event_data)

if response.status_code == 200:
    print("Event created successfully!")
    print("Event details:", response.json())
else:
    print("Failed to create event. Status code:", response.status_code)
    print("Response:", response.text)
