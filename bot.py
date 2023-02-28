from aiogram import *
from aiogram.dispatcher.filters import Text
from my_api import *
import pprint

def _get_location():
    url = 'http://ipinfo.io/json'
    response = json.load(urlopen(url))
    lat = response['loc'].split(',')[0]
    lon = response['loc'].split(',')[1]
    return float(lat), float(lon)

def _get_temp(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=8537d9ef6386cb97156fd47d832f479c&units=metric'
    response = json.load(urlopen(url))
    print(response)
    return response['main']['temp']

def _get_temp_feels(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=8537d9ef6386cb97156fd47d832f479c&units=metric'
    response = json.load(urlopen(url))
    return response['main']['feels_like']

def _get_pressure(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=8537d9ef6386cb97156fd47d832f479c&units=metric'
    response = json.load(urlopen(url))
    return response['main']['pressure']


bot = Bot(token='6161902700:AAFGYKPU0WAfbvLGI0FF1t9ZqffBKX1A0MY')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def hello(message:types.message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('температура', 'давление')
    await message.answer(
        f'Привет {message.from_user.username}, здесь ты можешь узнать погоду', 
        reply_markup = keyboard)

@dp.message_handler(Text(equals='температура'))
async def temp(message):
    lat, lon = _get_location()
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=8537d9ef6386cb97156fd47d832f479c&units=metric'
    response = json.load(urlopen(url))
    t = int(_get_temp(lat, lon))
    await message.answer(f'В вашем городе температура {t}C°')


if __name__ == '__main__':
    executor.start_polling(dp)

