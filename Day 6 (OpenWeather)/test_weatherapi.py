import requests

API_KEY = "2ef88736157cb0418b465ad08252e2dc"
BASE_URL = "https://api.openweathermap.org/data/2.5"

LAT = 19.0760
LON = 72.8777

ENDPOINTS = {
    "current_weather": f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}",
    "5_day_forecast": f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}"
}

# Test if API responses return status code 200
def test_api_responses():
    for endpoint, url in ENDPOINTS.items():
        response = requests.get(url)
        assert response.status_code == 200, f"Failed {endpoint}: {response.status_code}"
