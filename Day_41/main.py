from datetime import datetime as dt
import requests
import json


def post_data(date1, time1, exercise, duration, calories):
    url2 =
    post_data = {
        'workout': {
            'date': date1,
            'time': time1,
            'exercise': exercise,
            'duration': str(duration),
            'calories': str(calories),
        }
    }
    response2 = requests.post(url=url2, json=post_data)
    print(type(duration))


# set date and time
date = str(dt.now()).split(" ")[0]
time = str(dt.now()).split(" ")[1].split(".")[0]

# Set your API key
headers = {
    'x-app-id': '7fb4819c',
    'x-app-key': '387932a51c0cb0fbeee745862050eb41',
}

input_data = input("Tell me what exercise you did: ")

# Define the endpoint URL and the parameters for the request
url = "https://trackapi.nutritionix.com/v2/natural/exercise"
params = {
    'query': input_data,
    'gender': 'male',
    'weight_kg': 129.56,
    'height_cm': 175872,
    'age': 20
}

# Make the request to the API
response = requests.post(url, headers=headers, json=params)

# Print the response data
print(response.status_code)
data = json.loads(response.text)

for i in data['exercises']:
    print(i)
    print(i["user_input"])
    workout = i["user_input"]
    print(i["duration_min"])
    dur_min = i["duration_min"]
    print(i["nf_calories"])
    nf_cal = i["nf_calories"]

    post_data(date1=date, time1=time, exercise=workout, duration=dur_min, calories=nf_cal)

print(input_data)
print(type(input_data))
