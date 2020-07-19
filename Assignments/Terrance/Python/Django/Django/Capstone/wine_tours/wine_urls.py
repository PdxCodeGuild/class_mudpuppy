from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("vineyard/<int:vineyard_pk>/", views.vineyard_detail),
    path("receive/", views.receive_reservation),
    path("reservations/<int:vineyard_pk>/", views.make_reservation),
    path("contact/", views.contact),
    path("receive/contact/", views.receive_contact),
    # path('wine/', include('wine_tours.wine_urls')),
]