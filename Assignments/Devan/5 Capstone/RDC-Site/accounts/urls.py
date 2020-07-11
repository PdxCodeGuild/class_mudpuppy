from django.urls import path
from . import views
from django.contrib import admin

app_name = 'accounts'


urlpatterns = [
        path('',views.index,name="home"),
        path('accounts/sign_up/',views.sign_up,name="sign-up"),
]


# urlpatterns = [
#     path('rl-page/', views.rl_page, name='rl_page'),
#     path('register/', views.register, name='register'),
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout, name='logout'),
# ]