import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass


url = "https://api.sheety.co/7fda9457fd9c8184947c825a52944bf6/flightDeals/prices"
object_ID = None

response = requests.get(url=url)

data = response.json()

update_data = {
    "price": {
        'iataCode': "TESTING"
    }
}

print(data["prices"])
print(type(data))

for i in data["prices"]:
    print(i)
    object_ID = i['id']
    print(object_ID)
    response2 = requests.put(url=f"{url}/{object_ID}", json=update_data)
