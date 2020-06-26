from django.urls import path, include

from . import views
from .views import index

urlpatterns = [
    path('', views.index),
    path('short/', views.short, name='short_url')


]