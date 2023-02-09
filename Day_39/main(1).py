import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "7ca6443d5bc8d8a017ea5e1121144152"

weather_parameters = {
    "lat": 19.180247,
    "lon": 77.308105,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_parameters)
print(response.json())
