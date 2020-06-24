from django.shortcuts import render     #render mashes up a context dictionary and the html file to make html of http response variables show up on my browser
from django.http import HttpResponse
import random
import string
from .models import Urls

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
    context = None
    if request.method == "POST":
        new_url = Urls(org_url = request.POST['user_url'], short_url = url_create())
        new_url.save()

        # url_data = Urls.objects.all()
        context = {
            'url_data': new_url,     #the string will be looking inside the {} in my index.html
        }
    return render(request, "url_shortener/index.html", context)

def redirect_url(request, short_url):
    #look at link_slug function in links lab guide
    #     
