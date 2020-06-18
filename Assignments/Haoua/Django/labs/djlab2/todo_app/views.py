from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from  .forms import *
def index(request):
    items = Todo.objects.all()
    form = ItemForm()
    context = {'items': items,'form': form}
    # return HttpResponse("Hello Amigo")
# Create your views here.
    return render(request, 'todo_app/list.html', context)