from django.urls import path, include
from . import views
app_name = 'capstone'

urlpatterns = [
    path('', views.index),
    path('addsong/', views.index, name="add_song")
]