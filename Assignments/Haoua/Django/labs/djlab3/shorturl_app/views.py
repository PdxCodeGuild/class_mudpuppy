from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from . models import *


# Create your views here.
def index(request):
    return redirect("/long/")