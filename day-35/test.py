import requests
import json
from twilio.rest import Client


OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = ""
location = {
    "Place":[ 
    {
        "Latitude": "51.685669",
        "Longitude": "9.015250"}
    ]
}

parameters = {
            "lat":float(location["Place"][0]["Latitude"]),
            "lon":float(location["Place"][0]["Longitude"]),
            "exclude":"current,minutely,daily",
            "appid":API_KEY
}

response = requests.get(url=OMW_ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()

condition_code = [hour["weather"][0]["id"] for hour in weather_data["hourly"][:12]]

precipitation = [True for condition in condition_code if condition < 700]

if len(precipitation) > 0:
    print("It will rain in the next 12 hours")
    
#print(json.dumps(weather_data, sort_keys=True, indent=4))
