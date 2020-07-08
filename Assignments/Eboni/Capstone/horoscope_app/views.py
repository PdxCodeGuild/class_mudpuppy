from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date
from .secrets import api_key, api_id

def index(request):
    if request.method == "POST": 
        print(request.POST)
    return render(request, "horoscope_app/index.html") 

def detail(request):
    print(request.POST)
    date = request.POST["new"]
    print(date.split('-'))
    date_list = date.split('-')
    month = int(date_list[1])
    day = int(date_list[2])

    if month == 11 and day <= 22:
        print('Sagittarius')
    elif month == 12 and day <=21:
        print('Sagittarius')

    if month == 12 and day <= 22:
        print('Capricorn')
    elif month == 0o1 and day <=19:
        print('Capricorn')

    if month == 0o1 and day <=20:
        print('Aquarius')
    elif month == 0o2 and day <= 18:
        print('Aquarius')

    if month == 0o2 and day <= 19:
        print('Pisces')
    elif month == 0o3 and day <= 20:
        print('Pisces')

    if month == 0o3 and day <= 21:
        print('Aries')
    elif month == 0o4 and day <=19:
        print('Aries')

    if month == 0o4 and day <=20:
        print('Taurus')
    elif month == 0o5 and day <=20:
        print('Taurus')

    if month == 0o5 and day <=21:
        print('Gemini')
    elif month == 0o6 and day <=20:
        print('Gemini')

    if month == 0o6 and day <=21:
        print('Cancer')
    elif month == 0o7 and day <=22:
        print('Cancer')

    if month == 0o7 and day <=23:
        print('Leo')
    elif month == 0o8 and day <=22:
        print('Leo')


                
    print(f"month={month} and day={day}")
    return render(request, "horoscope_app/index.html")

# def detail_two(request):
    


# Create your views here.
# Python has class called "date/time"
