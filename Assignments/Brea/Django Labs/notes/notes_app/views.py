from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import Note
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
note_list = ['buy Oatly', 'run Conroy']

@login_required
def index(request):
    Note(
        user = request.user,
        text = random.choice(note_list)
    ).save()
    return HttpResponse(
        '<br>'.join(
            [note.text
                for note in request.user.notes.all()    #request is always going to have a user attribute
            ]
        ) + f'<a href="{reverse("users:logout")}"">Logout</a>'
    )