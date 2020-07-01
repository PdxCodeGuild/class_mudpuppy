# from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "toapp"
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index, name = "index"), 
    path('complete/', views.complete, name = "complete"), 
]