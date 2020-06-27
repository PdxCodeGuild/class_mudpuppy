from django.urls import path
from . import views

app_name = "mandados"
urlpatterns = [
    path('', views.index, name='indexo'),
    path('add/', views.add)
    
]