import json

# Load the saved Shegaon weather JSON file
with open("shegaon_weather.json", "r") as file:
    data = json.load(file)

# Test if JSON contains expected keys
def test_json_keys():
    assert "latitude" in data
    assert "longitude" in data
    assert "hourly" in data
    assert "temperature_2m" in data["hourly"]

# Test if hourly temperature data is available
def test_temperature_data():
    # Ensure the hourly temperature data exists and is in the expected format
    assert len(data["hourly"]["temperature_2m"]) > 0  # Should have at least one hourly record
    
    # Check if each item in the list is a number (float or int)
    for temp in data["hourly"]["temperature_2m"]:
        assert isinstance(temp, (int, float))  # Temperature should be a number (int or float)

def test_time_abbreviation():
    assert "timezone_abbreviation" in data  
    assert data["timezone_abbreviation"] == "GMT"
