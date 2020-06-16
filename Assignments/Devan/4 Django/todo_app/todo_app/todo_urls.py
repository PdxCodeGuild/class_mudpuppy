from django.urls import path, include
from . import views

app_name = 'todo_paths'

urlpatterns = [
    path('', views.index, name='index_path'),
]
