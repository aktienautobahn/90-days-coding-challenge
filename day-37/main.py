import requests
from datetime import datetime


USERNAME = ""
TOKEN = ""
GRAPH = "graph1" 

pixela_endpoint = "https://pixe.la/v1/users"



# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


user_params = {
    "id":"graph1",
    "name":"Walkin",
    "unit":"Min",
    "type":"int",
    "color":"ajisai",

}

header_params = {
    "X-USER-TOKEN":TOKEN
}

#today = datetime.now()
today = datetime(year=2022, month=6, day=27)
#print(today.strftime("%Y%m%d"))

pixel_params = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"27",
    "optionalData":"{\"km\":\"2.19\"}"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph1_endpoint = f"{graph_endpoint}/{GRAPH}" 

# response = requests.post(url=graph1_endpoint, json=pixel_params, headers=header_params)
# print(response.text)

pixel_endpoint = f"{graph1_endpoint}/{today.strftime('%Y%m%d')}"
pixel_update_params = {
                    "quantity":"27",
}
# response = requests.put(url=pixel_endpoint, json=pixel_update_params, headers=header_params)
# print(response.text)

#DELETE
response = requests.delete(url=pixel_endpoint, headers=header_params)
print(response.text)