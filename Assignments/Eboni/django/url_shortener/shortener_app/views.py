from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Code
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    print('ok')
    context = {'shortener_template_var': 'test'}
    return render(request, 'shortener_app/index.html')

def shorten(request):
    print(request.body)
    print(request.POST)
    print(request.POST["new"])
    new_code = Code(first_code=request.POST["new"], second_code=get_random_string(length=32))
    new_code.save()
    

