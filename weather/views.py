from django.shortcuts import render
from datetime import datetime
import pytz
import requests

# Create your views here.

def home(request):
    country = request.GET.get('country')
    # country = "Bangladesh,BD"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={country}&appid=ad6d44534e30e7b2126fc5dd67e214f2"

    data = requests.get(url).json()

    load_data = {
                'country': data['name'], 
                'weather': data['weather'][0]['main'],
                'icon': data['weather'][0]['icon'],
                'celsius_temperature': int(data['main']['temp'] - 273),
                'temp_min': int(data['main']['temp_min']),
                'temp_max': int(data['main']['temp_max']),
                'pressure': data['main']['pressure'],
                'humidity': data['main']['humidity'],
                'feels_like': int(data['main']['feels_like']),
                'city': data['sys']['country'],
                'wind': data['wind'],
                'description': data['weather'][0]['description'],
                }

    # Get current time
    tz_country = pytz.timezone('Asia/Dhaka')
    datetime_country = datetime.now(tz_country)

    # This format is 12:41AM
    current_time = datetime_country.strftime("%I:%M%p")

    # This format is Apr 20 2021 12:40AM
    # current_time = datetime_country.strftime("%b %d %Y %I:%M%p")
    # print(load_data)
    # print(current_time)

    context = { 'load_data':load_data, 
                'current_time':current_time }
    return render(request, 'index.html', context) 