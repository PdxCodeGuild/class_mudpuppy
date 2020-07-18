from django.shortcuts import render
from ball_pythons.models import BallPython
from django.conf import settings


def index(request):
    sorted_all_balls = BallPython.objects.order_by('listed_on').reverse()
    print(sorted_all_balls)
    last_6_balls = sorted_all_balls[:2]
    context = {
        'last_6_balls_template': last_6_balls,
    }

    return render(request, 'main/index.html', context)
