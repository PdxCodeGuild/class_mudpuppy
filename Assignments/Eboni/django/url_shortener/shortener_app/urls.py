from django.urls import path
from . import views

app_name = "shortener"

urlpatterns= [
    path('', views.index, name='index'),
    path('test/', views.shorten),
    path('redirect/<str:second_code>/', views.redirection, name='reverse_url')
]