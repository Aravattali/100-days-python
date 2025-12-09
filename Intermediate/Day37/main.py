import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

pixela_end_point = "https://pixe.la/v1/users"

# Create user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create graph
graph_endpoint = f"{pixela_end_point}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "cycling",
    "unit": "km",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Value endpoint
value_endpoint = f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")
value_config = {
    "date": today,
    "quantity": "9",
}

# Update endpoint
update_endpoint = f"{value_endpoint}/{today}"
new_pixela_data = {
    "quantity": "12"
}

# Delete endpoint
delete_endpoint = f"{value_endpoint}/{today}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
