from django.shortcuts import render
from .models import Snake
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.templatetags.static import static



@login_required
def index(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/pictures')

    all_snakes = Snake.objects.all()

    print(all_snakes[0].picture.url)
    context = {
        'all_snakes_template': all_snakes,
        'images' : img_list,
    }
    return render(request, 'snakes_app/index.html', context)
