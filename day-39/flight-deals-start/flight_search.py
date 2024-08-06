import requests


KIWI_LOCATION_SEARCH_END_POINT = "https://tequila-api.kiwi.com/locations/query"
KIWI_FLIGHT_SEARCH_END_POINT = "https://tequila-api.kiwi.com/v2/search"
API_KEY = {"apikey":""}




class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self) -> None:
        #self.search_input_data = user_data
        self.airport_origin = "" 
        self.airport_destination = "" 
        self.start_travel_date_from = ""
        self.start_travel_date_to = ""        
        self.duration_min = ""
        self.duration_max = ""
        self.max_stopovers = ""
        pass

    def get_destination_code(self, city):
        query = {
            "term":city,
            "active_only":"true",
            "location_types":"airport"
        }

        response = requests.get(url=KIWI_LOCATION_SEARCH_END_POINT, headers=API_KEY, params=query)

        codes = []
        for list_element in range(len(response.json()["locations"])):
            codes.append(response.json()["locations"][list_element]["city"]["code"])
        return codes[0]
    
    def flight_search(self, from_airport, to_airport, start_travel_from, start_travel_to, dur_min, dur_max, max_stops=2):
        self.airport_origin = from_airport
        self.airport_destination = to_airport
        self.start_travel_date_from = start_travel_from
        self.start_travel_date_to = start_travel_to        
        self.duration_min = dur_min
        self.duration_max = dur_max
        self.max_stopovers = max_stops

        query = {
            "fly_from":self.airport_origin,
            "fly_to":self.airport_destination,
            "date_from":self.start_travel_date_from,
            "date_to":self.start_travel_date_to,
            "nights_in_dst_from":self.duration_min,
            "nights_in_dst_to":self.duration_max,
            "max_stopovers":self.max_stopovers
        }

        search_results = requests.get(url=KIWI_FLIGHT_SEARCH_END_POINT, headers=API_KEY, params=query)

        return search_results.json()
