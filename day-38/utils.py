from textwrap import indent
import requests
from datetime import datetime
import json



X_APP_ID = ""
X_APP_KEY = ""
#func for converting nlp to structured information
def workout_nlp(GENDER, WEIGHT_KG, HEIGHT_CM, AGE):
    user_input = input("Tell me which exercides you did: ")

    headers = {
        "x-app-id":X_APP_ID,
        "x-app-key":X_APP_KEY,
        "Content-Type":"application/json"
    }

    request_params = {
            "query":user_input,
            "gender":GENDER,
            "weight_kg":WEIGHT_KG,
            "height_cm":HEIGHT_CM,
            "age":AGE

    }
    nutritionix_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
    response = requests.post(url=nutritionix_end_point, json=request_params, headers=headers)
    response_dict = response.json()
    #print(json.dumps(response_dict, indent=4))
    return response_dict


#post data to google sheets
def save_to_sheety(response_dict):
    headers = {"Authorization":""}
    url = ""
    date = datetime.now().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%X")


    for exercise in response_dict["exercises"]:
        body = {
            "workout":
            {
            "date":date,
            "time":time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
            }
        }
        try:
            response = requests.post(url=url, headers=headers, json=body)
            response.raise_for_status()
            print(f"{exercise['name'].title()} is saved")
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

            
        #print(response.json())


#get data from google sheet
def get_sheety_workouts():
    headers = {"Authorization":""}
    url = ""
    response = requests.get(url=url, headers=headers)
    print(response.json())