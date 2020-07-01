from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Snake

# Create your views here.

def index(request):
    all_snakes = Snake.objects.all()
    context = {
        'all_snakes_template': all_snakes,
    }
    return render(request, 'snakes_app/index.html', context)