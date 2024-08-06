from pprint import pprint
import requests
from flight_search import FlightSearch







TOKEN = {"Authorization":""}
SHEETY_END_POINT = ""


class DataManager:
    def __init__(self,) -> None:
        self.items = requests.get(url=SHEETY_END_POINT, headers=TOKEN).json()["prices"]
        self.iata = ""
        self.populate_iata_codes()

    
#----------------------------POPULATE AIRPORT CODES----------------------------#

    def populate_iata_codes(self):
        search =  FlightSearch()
        for city in self.items:
            if city["iataCode"] == 0 or city["iataCode"] =="":
                self.iata = search.get_destination_code(city["city"])
                city["iataCode"]=self.iata
                id = city["id"]
                self.update_sheety_prices(iata_code=self.iata, id=id)


    #get data from google sheet
    def update_sheety_prices(self, iata_code, id):
        data = {"price":
                        {"iataCode" : iata_code}
                }
        
        respond = requests.put(url=f"{SHEETY_END_POINT}/{id}", 
                                headers=TOKEN, 
                                json= data
                                )
        #print(respond.json())