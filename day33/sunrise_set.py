import requests
from datetime import datetime

parameters = {
    "lat" : 20.593683,
    "lng" : 78.962883,
    }
response = requests.get(url = "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)   
time_now = datetime.now()
print(time_now)
