from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date

def index(request):
    if request.method == "POST": 
        print(request.POST)
    return render(request, "horoscope_app/index.html") 

def detail(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, "horoscope_app/detail.html")



# Create your views here.
# Python has class called "date/time"
