from django.urls import path
from . import views

app_name = "shortener"

urlpatterns= [
    path('', views.index, name='index'),
    path('test/', views.shorten),
]