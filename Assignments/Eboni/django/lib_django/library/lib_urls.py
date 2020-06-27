from django.urls import path, include
from . import views

app_name = 'lib'
urlpatterns = [
    path('', views.index),
    path('auth/<int:author_pk>/', views.author_detail, name="author_detail"),
    path('checkout/<int:book_pk>/', views.checkout_page, name="checkout_page"),
    path('newcheck/', views.new_checkout, name="new_checkout"),

]

