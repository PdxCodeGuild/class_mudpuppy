from django.urls import path 
from . import views

app_name = 'users'
urlpatterns = [
    path('login-page/', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]