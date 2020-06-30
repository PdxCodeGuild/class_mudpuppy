from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date

def index(request):
    return HttpResponse('Hello')

def birthday(request):
    birthday = datetime.strptime("08/22/84", "%m/%d/%y")

# Create your views here.
# Python has class called "date/time"
