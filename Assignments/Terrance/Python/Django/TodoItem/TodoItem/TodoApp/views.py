from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TodoForm
from .models import TodoItem

def index (request):
    print(request.body)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_text = form.cleaned_data['todo_text']
            todo = TodoItem(description_text = todo_text)
            todo.save()
            form = TodoForm()
    else:
        form = TodoForm()
    return render(request, "todo_item/index.html", {'form': form, 'ToDos': TodoItem.objects.all()})

def complete (request):
    print(request.body)
    data = request.POST    
    print(data["todo_text"])

    found_todo = TodoItem.objects.get(description_text = data["todo_text"])
    print(found_todo.completed)
    if found_todo.completed == False:
        found_todo.completed = True
        found_todo.save()
    return HttpResponseRedirect("/todo/index/")

# Create your views here.
