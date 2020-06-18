from django.shortcuts import render, reverse
from .models import ToDoItems
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

def index(request):
    list_items = ToDoItems.objects.all()
    context = {
        'all_list_items': list_items,
    }
    return render(request, 'todo_app/index.html', context)

# Create your views here. This is where the functions for my To Do List will go
def list_item(request):
    list_items = ToDoItems.objects.all().order_by('create_date')
    return render(request, 'todo_app/index.html', {'list_items_dict': list_items})

def add_item(request):
    data = request.POST
    new_item = ToDoItems (
        todo_text = data['todo_text']
    )
    new_item.save()
    # add the thing to the database
    # look at past tutorials and see how to save something to the database
    return HttpResponseRedirect(reverse('todo_app:list_item')) 

def complete_item(request):
    print(request.body)
    print(request.POST['todo_text'])    #from the user inputting the item to be marked as complete
    found_todo = ToDoItems.objects.get(todo_text = request.POST['todo_text'])   #pulled from the database after the user submitted the item to be marked as complete
    found_todo.completed_bool = True
    found_todo.complete_date = datetime.now()
    found_todo.save()
    print(found_todo.todo_text)
    return HttpResponseRedirect(reverse('todo_app:list_item')) 
    # change the Boolean value to True, activate the completed date, and show the list item as a strikethrough (or remove things)