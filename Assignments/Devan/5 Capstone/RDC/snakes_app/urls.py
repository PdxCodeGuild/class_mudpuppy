from django.urls import path, include
from . import views

app_name = 'snakes_paths'

urlpatterns = [
    path("ball-pythons/", views.index, name='index_path'),
]
