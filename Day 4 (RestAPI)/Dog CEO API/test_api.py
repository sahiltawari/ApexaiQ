import json

# Load the saved JSON file
with open("dog_image.json", "r") as file:
    data = json.load(file)

# Test if JSON contains expected keys
def test_json_keys():
    assert "message" in data  # Check if 'message' key exists
    assert "status" in data   # Check if 'status' key exists

# Test if 'message' contains a URL (dog image link)
def test_message_is_url():
    assert data["message"].startswith("https://")  # Must start with 'https://'

# Test if 'status' is 'success'
def test_status():
    assert data["status"] == "success"
