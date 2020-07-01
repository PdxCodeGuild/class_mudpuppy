from django.shortcuts import render
from django.http import HttpResponse
from .models import URL
import string as s
from random import choice as rc


def index(request):
    return HttpResponse('test')


def index(request):
    context = None
    if request.method == "POST":
        new_url = URL(
            full_url=request.POST['orig_url'], tiny_url=urlGen())
        new_url.save()

        context = {
            'url_data': new_url
        }
    return render(request, "url_app/index.html", context)


def urlGen():
    digLet = s.ascii_letters + s.digits
    tinyURL = ''
    for i in range(6):
        char = rc(digLet)
        tinyURL += char
    return tinyURL
