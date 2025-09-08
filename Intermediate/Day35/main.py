import requests
from twilio.rest import Client
import os

owm_end_point = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "f83cf73f10124786a1a52d1bb4924716"

# Twilio setup (make sure these env vars are set)
account_sid = "ACc34b441ddedc7f5509331100474a15b8"
auth_token = "ef2e81f6520986624dd2ebe1e045ac60"
client = Client(account_sid, auth_token)

weather_params = {
    "lat": 4.051056,
    "lon": 9.767869,
    "appid": api_key,
    "cnt": 4,
    "units": "metric"
}

response = requests.get(owm_end_point, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:  # Codes < 700 mean rain, drizzle, snow, etc.
        will_rain = True

if will_rain:
    message = client.messages.create(
        body="🌧 It might rain in the next few hours. Bring an umbrella! ☔",
        from_="+19094875734",  # Twilio number
        to="+252907625228",    # Your verified number
    )
    print(f"Message sent: {message.body}")
else:
    print("No rain expected. 🌞")
