from django.conf import settings
from django.shortcuts import render
from .models import BallPython
from django.contrib.auth.decorators import login_required
import os


@login_required
def index(request):
    all_balls = BallPython.objects.all()
    print('DEGUG', all_balls)
    context = {
        'all_balls_template': all_balls,
    }
    return render(request, 'ball_pythons/index.html', context)
