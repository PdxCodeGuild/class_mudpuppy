from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from.models import Note 
import random
note_list = ['walk', 'run']
@login_required
def index(request):
    Note(
        user=request.user,
        text = random.choice(note_list)
        ).save()
    output = ''
    for note in request.user.notes.all():
        output = output + note.text + '<br>'
    return HttpResponse(output)
# Create your views here.
