from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('rl-page/', views.rl_page, name='rl_page'),
    path('register/', views.register, name='register'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout, name='logout'),
]