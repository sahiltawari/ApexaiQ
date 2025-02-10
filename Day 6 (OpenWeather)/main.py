import requests
import json
from datetime import datetime
from config import API_KEY

# OpenWeather API Key
# API_KEY = "2ef88736157cb0418b465ad08252e2dc"

# Mumbai Coordinates
LAT, LON = 19.0760, 72.8777

# OpenWeather API Endpoints
ENDPOINTS = {
    "current_weather": f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric",
    "5_day_forecast": f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
}

# Function to convert Unix timestamp to human-readable format
def convert_timestamps(data, keys):
    """Convert specified Unix timestamp keys to human-readable format."""
    for key in keys:
        if key in data:
            data[key] = datetime.utcfromtimestamp(data[key]).strftime('%Y-%m-%d %H:%M:%S')

# Function to fetch and process data
def fetch_weather_data(endpoint_name, session):
    try:
        response = session.get(ENDPOINTS[endpoint_name])
        response.raise_for_status()  # Raises an error for HTTP failures
        data = response.json()

        # Convert timestamps in current weather
        if endpoint_name == "current_weather":
            convert_timestamps(data, ["dt"])
            convert_timestamps(data.get("sys", {}), ["sunrise", "sunset"])

            if "weather" in data and len(data["weather"]) > 0:
                description = data["weather"][0]["description"]
                print(f"Current Weather Description: {description}")

        # Convert timestamps in 5-day forecast
        elif endpoint_name == "5_day_forecast":
            for entry in data.get("list", []):
                convert_timestamps(entry, ["dt"])

                if "weather" in entry and len(entry["weather"]) > 0:
                    description = entry["weather"][0]["description"]
                    date_time = entry["dt_txt"]  # Forecast time
                    print(f"Forecast on {date_time}: {description}")

        # Save JSON
        with open(f"{endpoint_name}.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved for {endpoint_name}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {endpoint_name}: {e}")

# Main function to call API
def main():
    with requests.Session() as session:  # Use a session for efficiency
        for endpoint in ENDPOINTS:
            fetch_weather_data(endpoint, session)

# Run the script
if __name__ == "__main__":
    main()
