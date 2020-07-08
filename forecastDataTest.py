"""
Get forecast information
"""
import matplotlib.pyplot as plt
import dateutil.parser
import numpy as np
import requests
import json
from pprint import pprint


city = 'YOUR_CITY'
apikey = 'YOUR_OPEN_WEATHER_API_KEY'
unit = 'metric'
language = 'es'

weekWeather = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units={}&lang={}'.format(city, apikey, unit, language)

req = requests.get(weekWeather)
data = req.json()

lastDate = ""
forecastWeek = []

timeForecast = []
tempForecast = []

if( data['cnt'] >= 40 ):
    #Get different days in weather forecast 
    for lst in data['list']:
        newDate = dateutil.parser.parse(lst['dt_txt']).date()
        #If is new date
        if( lastDate != newDate ):
            lastDate = newDate
            forecastWeek.append(lst)

    #If there are at least 5 different days
    if(len(forecastWeek) >= 5):
        for day in forecastWeek:
            date = dateutil.parser.parse(day['dt_txt']).date()
            temperature = day['main']['temp']
            wind = day['wind']['speed']

    for x in range(7):
        timeForecast.append(data['list'][x]['main']['temp'])
        tempForecast.append(str(dateutil.parser.parse(data['list'][x]['dt_txt']).time().strftime("%H:%M")))
        print(data['list'][x]['main']['temp'])
        print(dateutil.parser.parse(data['list'][x]['dt_txt']).time())

    #Draw forecast chart

    plt.figure(figsize=(6,2))
    plt.plot(tempForecast,timeForecast)
    plt.ylabel('Temperatura C°')
    plt.xlabel('Hora')
    plt.fill(tempForecast, timeForecast, alpha=0.3)
    plt.show()

"""
print(data['list'][0])
print("---------------")
print(data['list'][5])
"""