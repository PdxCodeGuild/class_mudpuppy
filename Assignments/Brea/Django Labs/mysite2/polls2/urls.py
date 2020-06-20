from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]