from django.shortcuts import render     #render mashes up a context dictionary and the html file to make html of http response variables show up on my browser
from django.http import HttpResponse
import random
import string

# Create your views here.
def url_create():
    letters = string.ascii_letters
    numbers = string.digits
    short_string = ''
    
    for i in range(6):
        char = random.choice(letters + numbers)
        short_string += char

    return short_string

def index(request):
    print(render(None, "index.html", {"color": 'red'}).content)     #.content means we want the html content of the http response
    return HttpResponse(url_create())