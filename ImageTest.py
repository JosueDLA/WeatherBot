"""
Basic layout of image
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests
from pprint import pprint
from io import BytesIO

#Basic configuration
mode = 'RGB'
size = (650,500)
color = ('orange')
filename = 'test.png'

#Font Sizes
img = Image.new(mode, size, color)
draw = ImageDraw.Draw(img)
icon = requests.get('http://openweathermap.org/img/wn/10d@2x.png')
ico = Image.open(BytesIO(icon.content))

titleFont = ImageFont.truetype('/Fonts/arial.ttf', 30)
mainFont = ImageFont.truetype('/Fonts/arial.ttf', 15)
tempFont = ImageFont.truetype('/Fonts/arial.ttf', 50)

#Drawing elements on image
draw.text((20,20), "Ciudad", font=titleFont, fill=(250,250,250))
draw.text((20,55), "Fecha", font=mainFont, fill=(250,250,250))
draw.text((20,75), "Descripcion", font=mainFont, fill=(250,250,250))
draw.text((90,120), "00°", font=tempFont, fill=(250,250,250))
draw.text((165,125), "C", font=mainFont, fill=(250,250,250))
draw.text((365,120), "Precipitacion", font=mainFont, fill=(250,250,250))
draw.text((365,140), "Humedad", font=mainFont, fill=(250,250,250))
draw.text((365,160), "Viento", font=mainFont, fill=(250,250,250))

img.paste(ico, (0,100), ico)

img.paste(ico, (15,325), ico)
draw.text((45,400), "Dia", font=mainFont, fill=(250,250,250))
draw.text((45,420), "Temp", font=mainFont, fill=(250,250,250))
draw.text((45,440), "Viento", font=mainFont, fill=(250,250,250))

img.paste(ico, (145,325), ico)
draw.text((175,400), "Dia", font=mainFont, fill=(250,250,250))
draw.text((175,420), "Temp", font=mainFont, fill=(250,250,250))
draw.text((175,440), "Viento", font=mainFont, fill=(250,250,250))

img.paste(ico, (275,325), ico)
draw.text((305,400), "Dia", font=mainFont, fill=(250,250,250))
draw.text((305,420), "Temp", font=mainFont, fill=(250,250,250))
draw.text((305,440), "Viento", font=mainFont, fill=(250,250,250))

img.paste(ico, (405,325), ico)
draw.text((435,400), "Dia", font=mainFont, fill=(250,250,250))
draw.text((435,420), "Temp", font=mainFont, fill=(250,250,250))
draw.text((435,440), "Viento", font=mainFont, fill=(250,250,250))

img.paste(ico, (525,325), ico)
draw.text((565,400), "Dia", font=mainFont, fill=(250,250,250))
draw.text((565,420), "Temp", font=mainFont, fill=(250,250,250))
draw.text((565,440), "Viento", font=mainFont, fill=(250,250,250))

img.save(filename)
img.show()