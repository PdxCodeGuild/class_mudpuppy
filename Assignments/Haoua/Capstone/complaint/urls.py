from django.urls import path, include
from .views import ComplaintView, ComplaintDetail, CreateComplaint

urlpatterns = [
    path('complaint/', ComplaintView.as_view(), name="complaint"),
    path('complaints/<int:pk>', ComplaintDetail.as_view(), name="complaints"),
    path('create/', CreateComplaint.as_view(), name="create"),


]