from django.urls import path, include
from . import views

app_name = 'ball_pythons_paths'

urlpatterns = [
    path("", views.index, name='index'),
]
