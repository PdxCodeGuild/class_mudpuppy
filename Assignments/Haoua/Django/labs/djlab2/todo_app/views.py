from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from . models import *
from  . forms import *

def index(request):
    items = Todo.objects.all()
    form = ItemForm()

    if request.method =='POST':
    
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save() #saves it to the database
        return redirect('/')
    context = {'items': items,'form': form}
    # return HttpResponse("Hello Amigo")
# Create your views here.
    return render(request, 'todo_app/list.html', context)

def update(request,pk):
    todo = Todo.objects.get(id=pk)

    form = ItemForm(instance=todo)

    if request.method =='POST':
        form = ItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'todo_app/update.html', context)

def delete(request, pk):
    title = Todo.objects.get(id=pk)

    if request.method =='POST':
        title.delete()
        return redirect('/')
    context = {'title':title}
    return render(request, 'todo_app/delete.html', context)