from django.urls import path
from . import views

app_name = "url_shortener"

urlpatterns = [
    path('', views.index, name="index"),
    path('url_create/', views.url_create),
    path('r/<str:short_url_param>/', views.redirect_url, name="redirect")
]