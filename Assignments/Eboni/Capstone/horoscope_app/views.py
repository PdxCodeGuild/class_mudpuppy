from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date
from .secrets import api_key, api_id

def index(request):
    if request.method == "POST": 
        print(request.POST)
    return render(request, "horoscope_app/index.html") 

def detail(request):
    if request.method == "POST":
        print(api_key, api_id)
    return render(request, "horoscope_app/detail.html")

# def detail_two(request):
    


# Create your views here.
# Python has class called "date/time"
