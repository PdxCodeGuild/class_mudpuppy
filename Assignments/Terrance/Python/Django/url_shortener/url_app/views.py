from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.crypto import get_random_string
from .models import URL

def index(request):
    context = {
        "food" : "sushi",
        "city" : "Honolulu",
    }
    return render(request, "url_app/index.html", context)

def add(request):
    full=request.POST["full"]
    short=get_random_string(length=8)
    new_url=URL(
        full=full, short=short,
    )
    new_url.save()
    return HttpResponseRedirect("/url/")

def go(request, code):
    print(code)
    found_URL=URL.objects.get(short=code)
    return HttpResponseRedirect(found_URL.full)    

# Create your views here.
