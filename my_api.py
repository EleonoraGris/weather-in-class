from urllib.request import urlopen
import json

def _get_location():
    url = 'http://ipinfo.io/json'
    response = json.load(urlopen(url))
    lat = response['loc'].split(',')[0]
    lon = response['loc'].split(',')[1]
    return float(lat), float(lon)

def _get_temp(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=8537d9ef6386cb97156fd47d832f479c&units=metric'
    response = json.load(urlopen(url))
    return response['temp']

def _get_temp_feels(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=8537d9ef6386cb97156fd47d832f479c&units=metric'
    response = json.load(urlopen(url))
    return response['feels_like']

def _get_pressure(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=8537d9ef6386cb97156fd47d832f479c&units=metric'
    response = json.load(urlopen(url))
    return response['pressure']