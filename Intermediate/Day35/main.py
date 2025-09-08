import requests
from twilio.rest import Client
import os

# OpenWeatherMap API
owm_end_point = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")  # Set your OpenWeatherMap key as an env variable

# Twilio setup (safe: use environment variables)
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

# Weather parameters
weather_params = {
    "lat": 4.051056,
    "lon": 9.767869,
    "appid": api_key,
    "cnt": 4,
    "units": "metric"
}

# Fetch weather data
response = requests.get(owm_end_point, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Check for rain
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:  # Codes < 700 = rain, drizzle, snow, etc.
        will_rain = True

# Send SMS if rain is expected
if will_rain:
    message = client.messages.create(
        body="🌧 It might rain in the next few hours. Bring an umbrella! ☔",
        from_="+19094875734",  # Your Twilio number
        to="+252907625228",    # Your verified number
    )
    print(f"Message sent: {message.body}")
else:
    print("No rain expected. 🌞")
