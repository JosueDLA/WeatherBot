# WeatherBot
Twitter bot that provides weather information. This bot generates an image with the weather forecast of a city entered by the user through a tweet.

![Output Image](https://josuedla.github.io/assets/images/project01/pic02.jpg)

![Tweet](https://josuedla.github.io/assets/images/project01/pic03.jpg)

## Setup

### Needed Libraries

To create this project we used multiple libraries. The main ones where.

**PIL**
```sh
> pip install Pillow
```

**Numpy**
```sh
> pip install numpy
```

**Tweepy**
```sh
> pip install tweepy
```

## API Key
**OpenWeatherAPI**
Get your OpenWeather API key [here](https://openweathermap.org/api)

**Twitter Developer**
Apply for your twitter API key [here](https://developer.twitter.com/en/apply-for-access)

## Files
- **Weatehrgt.py** - This is the main file, includes all the weather info, generates the output image and post it on twitter.
- **ImageTest.py** - Includes the basic layout of the output image.
- **botTest.py** - Basic code, includes all the bot code without weather info.
- **forecastDataTest** - Incluedes all the weather data and forecast info.
- **LastTweetId.txt** - This file contains the last ID that Weathergt.py has seen.
- **temp.png** - Sample output image.
- **twitter.png** - Twitter screenshot.

## Folders
- **Fonts** - Contains all the fonts used by the project.
