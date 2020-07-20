from django.urls import path,include
from .views import ComplaintView, ComplaintDetailView, CreateComplaint, PersonCreateComplaint, PersonView, PersonDetailView

urlpatterns = [
    path('complaint/', ComplaintView.as_view(), name="complaint"),
    path('complaints/<str:pk>', ComplaintDetailView.as_view(), name="complaints"),
    path('create/', CreateComplaint.as_view(), name="create"),
    path('person/', PersonCreateComplaint.as_view(), name="person"),
    path('people/', PersonView.as_view(), name="people"),
    path('persons/<str:pk>', PersonDetailView.as_view(), name="persons"),

]