import os
import json
import pprint

here = os.path.dirname(os.path.abspath(__file__))
search_results =os.path.join(here, 'search_results.json')

class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self) -> None:
        self.result = {}
        self.fair_price = 0
        self.bag_price = 0
        self.stop_overs_number = 0
        self.stop_over_cities = []
        self.via_city = ""
        self.origin_city = ""
        self.origin_airport = ""
        self.destination_city = ""
        self.destination_airport = ""
        self.nights_in_dest = 0
        self.out_date = ""
        self.in_date = ""
        self.deep_link = ""

    def search_price(self, response):
        try:

            data = response["data"][0]
            with open(search_results, "w") as file:
                json.dump(data, file)

        except IndexError:
            return None
        else:
            
            if len(data["route"]) > 2:
               self.return_stopover_cities(data) 

                    
            self.origin_city = data["cityFrom"]
            self.destination_city = data["cityTo"] + ", " + data["countryTo"]["name"]
            self.origin_airport = data["flyFrom"]
            self.destination_airport = data["flyTo"]
            self.fair_price = data["price"]
            self.bag_price = data["bags_price"]["1"]
            self.nights_in_dest = data["nightsInDest"]
            self.out_date = data["route"][0]["local_departure"].split("T")[0]
            for route in data["route"]:
                if route["cityFrom"] == data["cityTo"]:
                    self.in_date = route["local_departure"].split("T")[0]
            self.deep_link = data["deep_link"]

            self.result_printer()

    def return_stopover_cities(self, routes):# write a code for handling flights with stopovers
        city_from = routes["cityFrom"]
        city_to = routes["cityTo"]
        stopovers = []
        for route in routes["route"]: 
            if not route["cityTo"] == city_from and not route["cityTo"] == city_to:

                stopovers.append(route["cityTo"])
        self.stop_over_cities = set(stopovers)
        self.stop_overs_number = len(self.stop_over_cities)

 

    def result_printer(self):
       #print search results relevant data if available

        if self.fair_price == 0:
            print(f"\nThere are no tickets for direct flights to {None}.")
            
        else:


            print(f"\nFlight to {self.destination_city} with min price: €{self.fair_price} + baggage price: €{round(self.bag_price)} = €{round(self.fair_price+self.bag_price)}\n\
                Stay duration (days): {self.nights_in_dest}\n\
                Outbound flight: {self.out_date}\n\
                Inbound flight: {self.in_date}\n\
                Stopover(s): {self.stop_overs_number} in {', '.join(map(str, self.stop_over_cities))}\n\
                " 
                )
                #{self.deep_link}

    

