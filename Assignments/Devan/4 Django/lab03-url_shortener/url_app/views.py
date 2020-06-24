from django.shortcuts import render
from django.http import HttpResponse
from .models import URL
import string
import random


def index(request):
    return HttpResponse('test')


# Create your views here.
