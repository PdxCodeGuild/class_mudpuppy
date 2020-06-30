from django.shortcuts import render,reverse
from django.http import HttpResponse
from . models import Note
from django.contrib.auth.decorators import login_required
import random

note_list = ['buy milk', 'walk the dog']
# makes sure someone is logged in first before the function runs.
@login_required
def index(request):
    # best_food = 'lamb kababs'
    Note(
        # gives use the logout option
        user=request.user,
        text = random.choice(note_list),
    ).save()
    return HttpResponse(
        # if we put it in paranthesis it becomes a generator
        #below is a four loop within a list
        '<br>'.join(
            [note.text 
                for note in request.user.notes.all()
            ] 
        )+ f'<br><a href="{reverse("users:logout")}.logout</a>'
    )
# Create your views here.
