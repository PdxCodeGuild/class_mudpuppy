from django.shortcuts import render
from .models import Todo


# Create your views here.
def index(request):
    all_todos = Todo.objects.all()
    context = {
        'all_todos_template': all_todos,
    }
    return render(request, 'todo_app/index.html', context)
