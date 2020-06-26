from django.shortcuts import render
from django.http import HttpResponse 
from .models import ToDo

def index(request):
    todos = ToDo.objects.all()
    print(todos)
    context = {
        "todos" : todos
    }
    return render(request, "todo_app/index.html", context)    

