from django.urls import path
from . import views


app_name = "horoscope_app"

urlpatterns = [
    path('', views.index, name="horoscope"),
    path('detail/', views.detail, name="detail")
]