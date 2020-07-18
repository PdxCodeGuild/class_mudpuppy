from django.urls import path, include
from .views import ComplaintView

urlpatterns = [
    path('complaint/', ComplaintView.as_view(), name="complaint")
]