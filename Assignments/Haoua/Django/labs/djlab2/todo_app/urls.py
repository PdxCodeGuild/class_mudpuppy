from django.urls import path
from . import views
# from django.shortcuts import render

urlpatterns = [
    path('', views.index, name="list"),
    path('update/<str:pk>/', views.update, name="update_item"),
    path('delete/<str:pk>/', views.delete, name="delete_item"),
   
]
