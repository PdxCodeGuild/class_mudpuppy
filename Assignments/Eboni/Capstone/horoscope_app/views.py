from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date
from .secrets import api_key, api_id
from .models import Sign, Birthday
import requests 
import json
import pytz

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
    date_object.replace(tzinfo=pytz.UTC)
    

    matched_horo = None
    for sign in Sign.objects.all():
        if sign.check_date(date_object):
            matched_horo = sign
            break

    # print(date_object)
    '''
    if month == 6:
        if day <=20: 
            sign = 'Gemini'
        elif day >=21:
            sign = 'Cancer'
        
    if month == 7:
        if day <=22:
            sign = 'Cancer'
        elif day >=23:
            sign ='Leo'

    if month == 8: 
        if day <=22:
            sign = 'Leo'
        elif day >=23:
            sign = 'Virgo'

    if month == 9: 
        if day <=22:
            sign = 'Virgo'
        elif day >=23:
            sign = 'Libra'

    if month == 10: 
        if day <=22:
            sign = 'Libra'
        elif day >=23:
            sign = 'Scorpio'

    if month == 11:
        if day <=21:
            sign = 'Scorpio'
        elif day >=22:
            sign = 'Sagittarius'

    if month == 12:
        if day <=21:
            sign = 'Sagittarius'
        elif day >=22: 
            sign = 'Capricorn'

    if month == 1:
        if day <=19:
            sign= 'Capricorn'
        elif day >= 20:
            sign = 'Aquarius'

    if month == 2:
        if day <=18:
            sign = 'Aquarius'
        elif day >=19:
            sign = 'Pisces'

    if month == 3:
        if day <=20:
            sign = 'Pisces'
        elif day >21:
            sign = 'Aries'
    
    if month == 4:
        if day <= 19:
            sign = 'Aries'
        elif day >=20:
            sign = 'Taurus'

    if month == 5:
        if day <=20:
            sign = 'Taurus'
        elif day >=21:
            sign = 'Gemini'



    user_sign = Sign.objects.get(sign=sign)
    '''
    user_birthday = Birthday(date=date_object, sign=matched_horo)
    user_birthday.save()

    


                
    print(f"month={month} and day={day}")
    response = requests.get(f'http://horoscope-api.herokuapp.com/horoscope/today/{user_birthday.sign}')
    data = json.loads(response.text)
    context = {
        "birthday":user_birthday, "horoscope":data['horoscope']

    }
    return render(request, "horoscope_app/detail.html", context)


# def detail_two(request):
    


# Create your views here.
# Python has class called "date/time"