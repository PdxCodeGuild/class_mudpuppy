from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Snake
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    all_snakes = Snake.objects.all()
    print(all_snakes[0].picture.url)
    context = {
        'all_snakes_template': all_snakes,
    }
    return render(request, 'snakes_app/index.html', context)