import json

# Load the saved JSON files
with open("current_weather.json", "r") as file:
    current_weather = json.load(file)

with open("5_day_forecast.json", "r") as file:
    five_day_forecast = json.load(file)

# Test if current weather data contains expected keys
def test_current_weather_keys():
    assert "main" in current_weather
    assert "temp" in current_weather["main"]
    assert "humidity" in current_weather["main"]
    assert isinstance(current_weather["main"]["temp"], (int, float))

# Test if 5-day forecast contains hourly data
def test_5_day_forecast():
    assert "list" in five_day_forecast
    assert len(five_day_forecast["list"]) > 0
    assert isinstance(five_day_forecast["list"], list)


