from django.urls import path
from . import views
urlpatterns = [
    path('add/<int:num1>/<int:num2>/', views.add),
    path('sub/<int:num1>/<int:num2>/', views.sub),
]