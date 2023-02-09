from urllib.request import urlopen
import json


def _get_location():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    return json.load(response)

loc = _get_location()['loc']
print(loc)

def _get_weather():
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=51.5085&lon=-0.1257&appid=8537d9ef6386cb97156fd47d832f479c&units=metric'
    response = urlopen(url)
    return json.load(response)

deg = _get_weather()['wind']['deg']
deg = round(deg/45.0)
print(deg)