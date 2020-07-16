import requests
from django.shortcuts import render

def index(request):
    city = 'Las Vegas'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=44cd440e01a6b7df19d3f5601cc8e86f&units=imperial"
    
    
    res = requests.get(url)
    print(res.text)
    return render(request, 'weather/userlanding.html')