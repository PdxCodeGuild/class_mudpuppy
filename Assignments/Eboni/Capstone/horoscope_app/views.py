from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date
from .secrets import api_key, api_id
from .models import Sign, Birthday

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

    date_object = datetime.strptime(date, "%Y-%m-%d")
    # print(date_object)

    if month == 11 and day <= 22:
       sign = 'Sagittarius'
    elif month == 12 and day <=21:
        sign = 'Sagittarius'

    if month == 12 and day <= 22:
        sign = 'Capricorn'
    elif month == 1 and day <=19:
        sign = 'Capricorn'

    if month == 1 and day <=20:
        sign = 'Aquarius'
    elif month == 2 and day <= 18:
        sign = 'Aquarius'

    if month == 2 and day <= 19:
        sign = 'Pisces'
    elif month == 3 and day <= 20:
        sign = 'Pisces'

    if month == 3 and day <= 21:
        sign = 'Aries'
    elif month == 4 and day <=19:
        sign = 'Aries'

    if month == 4 and day <=20:
        sign = 'Taurus'
    elif month == 5 and day <=20:
        sign = 'Taurus'

    if month == 5 and day <=21:
        sign = 'Gemini'
    # if month == 6
    #     if day <=20: 
    #         sign = 'Gemini'
    #     elif day >=21:
    #         sign = 'Cancer'
        
    if month == 6 and day <=21:
        sign = 'Cancer'
    elif month == 7 and day <=22:
        sign = 'Cancer'

    if month == 7 and day <=23:
        sign = 'Leo'
    elif month == 8 and day <=22:
        sign = 'Leo'

    if month == 8 and day <=23:
        sign = 'Virgo'
    elif month == 9 and day <=22:
        sign = 'Virgo'

    if month == 9 and day <=23:
        sign = 'Libra'
    elif month == 10 and day <=22:
        sign = 'Libra'

    user_sign = Sign.objects.get(sign=sign)
    user_birthday = Birthday(date=date_object, sign=user_sign)
    user_birthday.save()

    


                
    print(f"month={month} and day={day}")
    return render(request, "horoscope_app/index.html")

# def detail_two(request):
    


# Create your views here.
# Python has class called "date/time"