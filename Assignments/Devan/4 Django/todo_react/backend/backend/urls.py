from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo_app import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo_app')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
