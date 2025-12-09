import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
X_APP_ID = os.getenv("X_APP_ID")
TOKEN = os.getenv("TOKEN")

GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 180
AGE = 27

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
exercise_text = input("Tell me the exercise you did today? ")

spreed_sheet_endpoint = "https://api.sheety.co/942a1363877a5d9b029f6d9912feca85/workoutTracking/workouts"

# Nutrition API headers
nutrition_headers = {
    "x-app-id": X_APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Call Nutrition API
response = requests.post(url=exercise_endpoint, json=parameters, headers=nutrition_headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%H:%M:%S")

# Sheety headers (Bearer)
sheety_headers = {
    "Authorization": f"Bearer {TOKEN}"
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        url=spreed_sheet_endpoint,
        json=sheet_inputs,
        headers=sheety_headers
    )
    print(sheet_response.text)
