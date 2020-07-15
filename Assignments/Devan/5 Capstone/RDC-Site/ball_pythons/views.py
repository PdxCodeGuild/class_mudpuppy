from django.conf import settings
from django.shortcuts import render
from .models import BallPython
from django.contrib.auth.decorators import login_required
import os




@login_required
def index(request):
    path = settings.MEDIA_ROOT
    # img_list = os.listdir(path + '/ball_pythons/img')
    all_balls = BallPython.objects.all()

    print('DEBUG:', all_balls[0].picture.url)
    print(dir(all_balls[0].picture))
    context = {
        'all_balls_template': all_balls,
    }
    return render(request, 'ball_pythons/index.html', context)
