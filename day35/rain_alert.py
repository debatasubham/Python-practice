import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "5d6e74201800e0d28225ca66e046de47"

weather_params = {
    "lat": 20.462521,
    "lon": 85.882988,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}
response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
weather_data = response.json()
print(weather_data)

