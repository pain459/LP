from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

@app.post('/get-weather-today')
async def get_weather_today(location: str = Form(...)):
    try:
        # Make a request to the weather API
        api_key = 'YOUR_WEATHER_API_KEY'
        weather_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}')
        weather_info = weather_response.json()

        # Format weather data into Slack response
        response_text = f"The weather in {location} is {weather_info['weather'][0]['description']}."

        # Send response to Slack
        return JSONResponse(content={
            'response_type': 'in_channel',
            'text': response_text
        })
    except Exception as e:
        print('Error fetching weather:', e)
        return JSONResponse(content={'text': 'Error fetching weather data.'}, status_code=500)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
