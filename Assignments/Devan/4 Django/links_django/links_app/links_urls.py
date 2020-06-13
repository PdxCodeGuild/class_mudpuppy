from django.urls import path, include
from . import views

app_name = 'links_paths'

urlpatterns = [
    path("list/", views.index, name='index_path'),
    path("l/<str:in_slug>", views.link_slug, name="slug_path"),
]
