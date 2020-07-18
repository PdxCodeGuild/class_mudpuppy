from django.urls import path, include
from . import views
app_name = 'capstone'

urlpatterns = [
    path('', views.index),
    path('addreview/', views.add_review, name="add_review"),
    path('songdisplay/<int:song_id>/', views.song_display, name="song_display")
]