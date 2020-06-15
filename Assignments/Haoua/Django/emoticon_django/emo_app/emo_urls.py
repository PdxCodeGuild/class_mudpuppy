from django.urls import path, include
from . import views


app_name = 'emo_paths' # New line
urlpatterns = [
       path('', views.index, name='index_path'), # Changed line
       path('add/', views.add, name='add_path'), # Changed line
]