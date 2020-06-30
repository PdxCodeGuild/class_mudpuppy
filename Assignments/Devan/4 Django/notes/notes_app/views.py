from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import Note
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return HttpResponse(
        "<br>".join(
            [note.text for note in request.user.notes.all()]
            ) + f'<br><a href="{reverse("users:logout")}">logout</a>'
    )