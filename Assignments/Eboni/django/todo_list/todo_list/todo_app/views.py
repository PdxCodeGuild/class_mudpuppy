from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import TodoItem

def index(request):
    display = TodoItem.objects.all()
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

def delete_item(request):
    print(request.body)
    print(request.POST["delete_item"])
    data = request.POST
    new_complete = TodoItem.objects.get(item_text=data["delete_item"])
    new_complete.delete()
    return HttpResponseRedirect(reverse("todo:index"))

def new_delete_item(request, id):
    new_complete_new = TodoItem.objects.get(id=id)
    new_complete_new.delete()
    return HttpResponseRedirect(reverse("todo:index"))
    
    
    


# Create your views here.
