import requests
import json
import os
from twilio.rest import Client


#----------------------------CONSTANTS----------------------------#
OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = ""
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
location = {
    "place":[ 
    {
        "Latitude": "52.695669",
        "Longitude": "10.016250"}
    ]
}

#----------------------------GETTING WEATHER DATA----------------------------#
parameters = {
            "lat":float(location["Placeholder"][0]["Latitude"]),
            "lon":float(location["Placeholder"][0]["Longitude"]),
            "exclude":"current,minutely,daily",
            "appid":API_KEY
}

response = requests.get(url=OMW_ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()

condition_code = [hour["weather"][0]["id"] for hour in weather_data["hourly"][:12]]

precipitation = [True for condition in condition_code if condition < 700]


    
#----------------------------SENDING SMS----------------------------#
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

if len(precipitation) > 0:
    message = client.messages \
                    .create(
                        body="It can rain today for your location '{}'. Get umbrella!",
                        from_=twillio_number,
                        to=recipient
                    )

    print(message.sid)
