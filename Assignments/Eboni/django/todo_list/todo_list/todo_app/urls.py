from django.urls import path
from . import views
app_name = "todo"
urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add_list),
    path('delete/', views.delete_item),
    path('new-delete/<int:id>/', views.new_delete_item, name='new_delete'),
]