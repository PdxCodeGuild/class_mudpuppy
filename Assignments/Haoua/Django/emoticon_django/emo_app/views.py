from django.shortcuts import render, reverse # Changed line
from django.http import HttpResponseRedirect
from random import choice
from .models import Eye, Nose, Mouth

def index(request):
       # return HttpResponse( # Deleted line
       #         choice(';:') + # Deleted line
       #         choice('>-') + # Deleted line
       #         choice(')]') # Deleted line
       # ) # Deleted line
       eyes = list(Eye.objects.all())
       noses = list(Nose.objects.all())
       mouths = list(Mouth.objects.all())
       emoticon = str(choice(eyes)) + str(choice(noses)) + str(choice(mouths))
       context = {'emoticon_template_var': emoticon}
       return render(request, 'emo_app/index.html', context)


def add(request):
    print('*' * 80)
    print('dictionary:'.ljust(15), request.POST)
    print('*' * 80)
    print('raw:'.ljust(15), request.body)
    print('*' * 80)
    data = request.POST
    face_parts = {

        'eye': Eye,
        'nose': Nose,
        'mouth': Mouth,
    }
    #   new_part_class = face_parts[data['type']]
    #   new_part = new_part_class(char=data['new'])
    #   new_part.save()
    #   return HttpResponseRedirect('/emo/')

    new_part = new_part_class(char=data['new'])
    new_part.save()
    return HttpResponseRedirect(reverse('emo_paths:index_path'))