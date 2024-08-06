from multiprocessing.connection import wait
import requests
from datetime import datetime
import smtplib
import time
import json
import os
# ---------------------------- PATHS ----------------------------#
here = os.path.dirname(os.path.abspath(__file__))
coordinates_file = os.path.join(here, 'my_coordinates.json')
# ---------------------------- CONSTANTS ----------------------------#
MY_EMAIL = "" # add here your email
MY_PASSWORD = "" # add here your key

# ---------------------------- IS IT NIGHT AND ISS IS CLOSE ----------------------------#
def watch_out_function(lat, long):
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"ISS Positon is Latitude {iss_latitude}, Longitude {iss_longitude}")

    response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={lat}&lng={long}&formatted=0")

    data = response.json()

    sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0]) + 2 #converting to Berlin time
    sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0]) + 2 #converting to Berlin time
    time_now = datetime.now()

    if time_now.hour not in range(sunrise, sunset):
        print("it is dark")

        if abs(iss_latitude-lat) < 5 and abs(iss_longitude-long) < 5:
            print("Heads up, ISS is overhead")
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:ISS there upside\n\nWatch out, there is an ISS overhead"
                )
                print("Log: Email sent")





while True:
    with open(coordinates_file, mode="r") as coor_file:
        my_coordinates = list(json.load(coor_file).items())
    latitude = float(my_coordinates[0][1][0]["Latitude"])
    longitude = float(my_coordinates[0][1][0]["Longitude"])

    watch_out_function(latitude, longitude) # function

    time.sleep(60) #wait 10 minutes


#TODO If the ISS is close to my current position
#TODo and it sis currenly dark
#send email to tell me to look up
#BONUS run the code every 60 seconds
