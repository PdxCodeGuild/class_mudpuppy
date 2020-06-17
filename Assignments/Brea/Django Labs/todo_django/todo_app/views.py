from django.shortcuts import render, reverse
from .models import ToDoItems
from django.http import HttpResponse, HttpResponseRedirect

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
    # change the Boolean value to True, activate the completed date, and show the list item as a strikethrough (or remove things)
    pass

def strike_item(request):
    pass
    # make a function that does a strikethrough when completed_bool = True
    # pull something from the database, 
    # path('l/<str:in_slug>/', views.link_slug, name="slug_path"),
    #def link_slug(request, in_slug):
    # found_link = Link.objects.get(slug=in_slug)
    # comments = found_link.comment_set.all()
    # context = {
    #     'found_link_template': found_link,
    #     'comments_template': comments,
    # }
    # return render(request, 'links_app/slug.html', context)