import requests
import json

# API URL for weather data (Shegaon, India)
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=20.7932&longitude=76.6992&hourly=temperature_2m&forecast_days=3"

# Fetch data from the API
response = requests.get(API_URL)

# Check if request was successful
if response.status_code == 200:
    data = response.json()  # Convert response to JSON format

    # Save JSON data into a file
    with open("shegaon_weather.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Weather data Shegaon saved successfully!")
else:
    print("Failed to fetch data. Status Code:", response.status_code)