from PIL import Image, ImageDraw, ImageFont, ImageFilter
from datetime import date
from pprint import pprint
from io import BytesIO
import matplotlib.pyplot as plt
import dateutil.parser
import numpy as np
import requests
import tweepy
import types
import time
import json

class Weather:
    def __init__(self, data):
        self.name = data['name']
        self.date = str(date.today())
        self.description = data['weather'][0]['description']
        self.icon = data['weather'][0]['icon']
        self.temperature = str(data['main']['temp'])
        self.maxtemp = str(data['main']['temp_max'])
        self.mintemp = str(data['main']['temp_min'])
        self.humidity = str(data['main']['humidity'])
        self.pressure = str(data['main']['pressure'])
        self.wind = str(data['wind']['speed'])

    def printData(self):
        print(self.name)
        print(self.date)
        print(self.description)
        print(self.temperature)
        print(self.maxtemp)
        print(self.mintemp)
        print(self.humidity)
        print(self.icon)
        print(self.pressure)
        print(self.wind)

    def getIcon(self, name):
        request = requests.get('http://openweathermap.org/img/wn/{}@2x.png'.format(name))
        icon = Image.open(BytesIO(request.content))
        return icon

    def getImage(self, week, chart):
        #Basic configuration
        mode = 'RGB'
        size = (650,500)
        color = ('orange')
        
        #Font Sizes
        img = Image.new(mode, size, color)
        draw = ImageDraw.Draw(img)

        titleFont = ImageFont.truetype('/Fonts/arial.ttf', 30)
        mainFont = ImageFont.truetype('/Fonts/arial.ttf', 15)
        tempFont = ImageFont.truetype('/Fonts/arial.ttf', 50)

        #Drawing elements on image
        draw.text((20,20), self.name, font=titleFont, fill=(250,250,250))
        draw.text((20,55), self.date, font=mainFont, fill=(250,250,250))
        draw.text((20,75), self.description, font=mainFont, fill=(250,250,250))
        draw.text((90,120), self.temperature, font=tempFont, fill=(250,250,250))
        draw.text((165,125), "°C", font=mainFont, fill=(250,250,250))
        draw.text((365,120), "Presion: {}".format(self.pressure), font=mainFont, fill=(250,250,250))
        draw.text((365,140), "Humedad: {}%".format(self.humidity), font=mainFont, fill=(250,250,250))
        draw.text((365,160), "Viento: a {} Km/h".format(self.wind), font=mainFont, fill=(250,250,250))

        img.paste(self.getIcon(self.icon), (0,100), self.getIcon(self.icon))

        img.paste(self.getIcon(week[0].icon), (15,325), self.getIcon(week[0].icon))
        draw.text((40,400), "{}".format(week[0].date), font=mainFont, fill=(250,250,250))
        draw.text((40,420), "{}°C".format(week[0].temperature), font=mainFont, fill=(250,250,250))
        draw.text((40,440), "{} Km/h".format( week[0].wind), font=mainFont, fill=(250,250,250))

        img.paste(self.getIcon(week[1].icon), (145,325), self.getIcon(week[1].icon))
        draw.text((170,400), "{}".format(week[1].date), font=mainFont, fill=(250,250,250))
        draw.text((170,420), "{}°C".format(week[1].temperature), font=mainFont, fill=(250,250,250))
        draw.text((170,440), "{} Km/h".format( week[1].wind), font=mainFont, fill=(250,250,250))

        img.paste(self.getIcon(week[2].icon), (275,325), self.getIcon(week[2].icon))
        draw.text((300,400), "{}".format(week[2].date), font=mainFont, fill=(250,250,250))
        draw.text((300,420), "{}°C".format(week[2].temperature), font=mainFont, fill=(250,250,250))
        draw.text((300,440), "{} Km/h".format( week[2].wind), font=mainFont, fill=(250,250,250))

        img.paste(self.getIcon(week[3].icon), (405,325), self.getIcon(week[3].icon))
        draw.text((430,400), "{}".format(week[3].date), font=mainFont, fill=(250,250,250))
        draw.text((430,420), "{}°C".format(week[3].temperature), font=mainFont, fill=(250,250,250))
        draw.text((430,440), "{} Km/h".format( week[3].wind), font=mainFont, fill=(250,250,250))

        img.paste(self.getIcon(week[4].icon), (525,325), self.getIcon(week[4].icon))
        draw.text((560,400), "{}".format(week[4].date), font=mainFont, fill=(250,250,250))
        draw.text((560,420), "{}°C".format(week[4].temperature), font=mainFont, fill=(250,250,250))
        draw.text((560,440), "{} Km/h".format( week[4].wind), font=mainFont, fill=(250,250,250))

        return img

class ForecastDay:
    def __init__(self, data):
        self.date = dateutil.parser.parse(data['dt_txt']).date()
        self.time = str(dateutil.parser.parse(data['dt_txt']).time().strftime("%H:%M"))
        self.temperature = data['main']['temp']
        self.wind = data['wind']['speed']
        self.icon = data['weather'][0]['icon']
        
    def printData(self):
        print(self.date)
        print(self.time)
        print(self.temperature)
        print(self.wind)
        print(self.icon)

    def getIcon(self, name):
        request = requests.get('http://openweathermap.org/img/wn/{}@2x.png'.format(name))
        icon = Image.open(BytesIO(request.content))
        return icon

def populateWeek(data):
    if( data['cnt'] >= 40 ):
        lastDate = ""
        forecast = []
        forecastWeek = []

        #Get different days in weather forecast
        for day in data['list']:
            newDay = ForecastDay(day)
            forecast.append(newDay)

            #If is new date
            if( lastDate != newDay.date ):
                lastDate = newDay.date
                forecastWeek.append(newDay)
    return forecast, forecastWeek

def validateWeek(forecastWeek):
    #If there are at least 5 different days
    if(len(forecastWeek) >= 4):
        return True
    return False

def populateChart(forecast):
    tempForecast = []
    timeForecast = []
    
    for x in range(7):
        timeForecast.append(forecast[x].time)
        tempForecast.append(forecast[x].temperature)
    return tempForecast, timeForecast

def plotChart(tempForecast, timeForecast):
    #Draw forecast chart
    plt.figure(figsize=(6,2))
    plt.plot(tempForecast,timeForecast)
    plt.ylabel('Temperatura C°')
    plt.xlabel('Hora')
    plt.fill(tempForecast, timeForecast, alpha=0.3)
    return plt

def getData(city):
    #OpenWeather info
    city = 'YOUR_CITY'
    apikey = 'YOUR_OPEN_WEATHER_API_KEY'
    unit = 'metric'
    language = 'es'

    #Request Data to OpenWeather API
    todayUrl = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}&lang={}'.format(city, apiKey, unit, language)
    forecastUrl = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units={}&lang={}'.format(city, apiKey, unit, language)

    print(todayUrl)
    print(forecastUrl)

    todayData = requests.get(todayUrl).json()
    forecastData = requests.get(forecastUrl).json()

    return todayData, forecastData

def getLastTweetId(fileName):
    read = open(fileName, 'r')
    lastTweetId = int(read.read().strip())
    read.close()
    return lastTweetId

def saveLastTweetId(lastTweetId, fileName):
    write = open(fileName, 'w')
    write.write(str(lastTweetId))
    write.close()
    return

def replyToTweets(api, fileName = 'LastTweetId.txt'):
    #Test Id: YOUR TEST ID
    #Only get unseen tweets

    #mentions = api.mentions_timeline()
    #print(mentions[0].__dict__.keys())
    lastTweetId = getLastTweetId(fileName)
    mentions = api.mentions_timeline(lastTweetId, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        city = mention.full_text.lower()

        lastTweetId = mention.id 
        saveLastTweetId(lastTweetId, fileName)

        if('@gtclima ' in city):
            city = city.replace('@gtclima ', '')
            city = city.replace(' ', ',')
        elif ('@gtclima' in city):
            city = city.replace('@gtclima', '')
            city = city.replace(' ', ',')

        #Get Forecast data
        todayData, forecastData = getData(city)

        if( todayData['cod'] == 200 and forecastData['cod'] == '200' ):
            print('Respondiendo...')

            weather = Weather(todayData)
            forecast, forecastWeek = populateWeek(forecastData)

            #Get Image
            tempForecast, timeForecast = populateChart(forecast)
            chart = plotChart(timeForecast, tempForecast)
            image = weather.getImage(forecastWeek, chart)
            image.save('temp.png')

            api.update_with_media(filename='temp.png', status='@{} Gracias por usar ClimaGt2 :D'.format(mention.user.screen_name), in_reply_to_status_id=mention.id)
        else:
            print('Error...')
            api.update_status(status='@{} Municipio invalido :('.format(mention.user.screen_name), in_reply_to_status_id=mention.id)

if __name__ == "__main__":
    print('ClimaGt Bot')
    
    #Twitter Developer info
    CONSUMER_KEY = 'YOUR_API_KEY'
    CONSUMER_SECRET = 'YOUR_API_SECRET'
    ACCESS_KEY = 'YOUR_ACCESS_KEY'
    ACCESS_SECRET = 'YOUR_ACCESS_SECRET'

    #Request Data to Twitter API
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

    while True:
        try:
            #Reply to Tweets
            replyToTweets(api)
            time.sleep(10)
        except tweepy.TweepError:
            print('Error...')
            continue
        except StopIteration:
            break