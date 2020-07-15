from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    context= {

    }
    return render(request, 'main/index.html', context)