import requests
from datetime import  datetime

from jsonpointer import resolve_pointer

USERNAME ="arafatalijama"
TOKEN = "akakakakakaka"
GRAPH_ID = "graph1"
DATe = datetime.now()
pixela_end_point = "https://pixe.la/v1/users"
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",

}
# response = requests.post(url= pixela_end_point , json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_end_point}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "cycling",
    "unit" : "km",
    "type" : "float",
    "color" : "shibafu",
}

headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers = headers)
# print(response.text)

value_endpoint = f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

value_config = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity" : "9",
}

# response = requests.post(url=value_endpoint, json=value_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
new_pixela_data = {
    "quantity" : "12"
}
# response= requests.put(url=update_endpoint,json=new_pixela_data,headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)















