from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect 
from .models import ToDo

def index(request):
    todos = ToDo.objects.all()
    print(todos)
    context = {
        "todos" : todos
    }
    return render(request, "todo_app/index.html", context)    
def add(request):
    print(request.POST)
    print(request.POST['task'])#creates 
    task = request.POST['task']
    newtodo = ToDo(task=task)
    newtodo.save()

    return HttpResponseRedirect(reverse("mandados:indexo"))
def strikethrough(request):
    id = (request.POST['id'])
    donetodo = ToDo.objects.get(id=id)
    donetodo.complete = True
    donetodo.save()
    #found_link = Link.objects.get(slug=in_slug)
    return HttpResponseRedirect(reverse("mandados:indexo"))
    