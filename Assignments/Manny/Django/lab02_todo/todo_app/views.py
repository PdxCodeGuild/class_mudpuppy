from django.shortcuts import render
from django.http import HttpResponse 
from . import models

def index(request):
    print(models.ToDo.objects.all())
    return HttpResponse('test')
