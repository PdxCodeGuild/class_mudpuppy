from django.urls import path
from . import views

app_name = 'emo_paths'
urlpatterns = [
    path('', views.index, name='index_path'),
    path('add/', views.add, name='add_path'),
]

