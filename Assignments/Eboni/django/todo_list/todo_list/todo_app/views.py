from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import TodoItem

def index(request):
    display = list(TodoItem.objects.all())
    add_item = display
    context = {'list_template_var': add_item}
    return render(request, 'todo_app/index.html', context)

def add_list(request):
    print(request.body)
    print(request.POST["add_item"])
    data = request.POST
    new_todo = TodoItem(item_text=data["add_item"])
    new_todo.save()
    return HttpResponseRedirect(reverse("todo:index"))

# Create your views here.
