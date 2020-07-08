from django.urls import path, include
from . import views

app_name = 'main_paths'

urlpatterns = [
    path("", views.index, name='index'),
]
