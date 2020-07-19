from django.urls import path, include
from . import views
app_name = 'capstone'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('input/', views.index, name='index'),
    path('addreview/', views.add_review, name="add_review"),
    path('songdisplay/<int:song_id>/', views.song_display, name="song_display"),
    path('songdisplay/<int:song_id>/index', views.add_review, name="add_review"),
]