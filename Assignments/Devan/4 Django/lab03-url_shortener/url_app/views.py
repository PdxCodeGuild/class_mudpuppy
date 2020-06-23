from django.shortcuts import render
from django.http import HttpResponse


def IndexView(self):
    template_name = 'url_shortener/index.html'

    return HttpResponse(template_name)
