from django.urls import path, include
from . import views
app_name = "todo_app"

urlpatterns = [
    path('', views.list_item, name="list_item"),
    path('additem/', views.add_item, name="add_item"),
    path('completeitem/', views.complete_item, name="complete_item"),
]