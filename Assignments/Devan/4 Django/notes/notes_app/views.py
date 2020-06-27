from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    return HttpResponse(
        '<br>'.join(
            [notes.text for note in Note.objects.all()]
        )
        )