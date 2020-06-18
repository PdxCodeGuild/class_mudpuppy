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