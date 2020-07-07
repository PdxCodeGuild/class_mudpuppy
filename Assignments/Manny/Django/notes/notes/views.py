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
    active_user = request.user
    print(active_user.username)
    notes_associated_with_user = active_user.notes_tacos.all()
    print([note.text for note in notes_associated_with_user])
    for note in notes_associated_with_user:
    #for note in request.user.notes.all():
        output = output + note.text + '<br>'
    return HttpResponse(output)
# Create your views here.
