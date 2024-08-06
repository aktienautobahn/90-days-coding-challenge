#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import os
from datetime import datetime, timedelta

#----------------------------INPUT DATA----------------------------#
tomorrow = (datetime.now()+ timedelta(days=1)).strftime("%d/%m/%Y")
in_six_months = (datetime.now()+ timedelta(days=180)).strftime("%d/%m/%Y") 

FROM_AIRPORT = "airport:MUC"
START_TRAVEL_DATE_FROM = tomorrow
START_TRAVEL_DATE_TO = in_six_months
DURATION_MIN = 20
DURATION_MAX = 40
MAX_STOPOVERS = 3
# --> add other search kriteria

#----------------------------PRINT RESULTS----------------------------#
os.system('cls' if os.name == 'nt' else 'clear')
print("WELCOME TO MIN PRICE SEARCHER FOR FLIGHTS")
print(f"Search parameters:\n\
        Flight from: {FROM_AIRPORT}\n\
        Flight Type: Round Trip \n\
        Outbound flight from: {START_TRAVEL_DATE_FROM}\n\
        Outbound flight till: {START_TRAVEL_DATE_TO}\n\
        Min stay days: {DURATION_MIN}\n\
        Max stay days: {DURATION_MAX}\n\
        \nSearch results: ")

#----------------------------SEARCH OBJECTS----------------------------#
                        
destination_objects = DataManager()

for search_item in destination_objects.items:
    search_request = FlightSearch()
    flight_data = FlightData()
    search_results_json = search_request.flight_search(from_airport=FROM_AIRPORT,
                                                    to_airport=search_item["iataCode"],
                                                    start_travel_from=START_TRAVEL_DATE_FROM,
                                                    start_travel_to=START_TRAVEL_DATE_TO,
                                                    dur_min=DURATION_MIN,
                                                    dur_max=DURATION_MAX,
                                                    max_stops=MAX_STOPOVERS,
                                                    )
    flight_data.search_price(search_results_json)

    #check if price matched
    notification = NotificationManager()
    try:
        total_price = flight_data.fair_price+flight_data.bag_price
        if notification.wished_price(min_price=total_price,
                                    wished_price=search_item["lowestPrice"]):
            print("Your price is matched. Hurry up!")
            notification.send_email(flight_data)
    except:
        pass