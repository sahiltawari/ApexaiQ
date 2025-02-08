import requests
import json

# API URL for random dog images
API_URL = "https://dog.ceo/api/breeds/image/random"

# Fetch data from the API
response = requests.get(API_URL)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Convert response to JSON format

    # Save JSON data into a file
    with open("dog_image.json", "w") as file:
        json.dump(data, file, indent=4)

    print("JSON data saved successfully!")
else:
    print("Failed to fetch data. Status Code:", response.status_code)
