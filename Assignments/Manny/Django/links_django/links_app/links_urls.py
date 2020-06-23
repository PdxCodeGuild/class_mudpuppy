from django.urls import path
from . import views

app_name = "links_paths" # New line
urlpatterns = [
    path('list/', views.index, name="index_path"), # Changed line
    path('l/<str:in_slug>/', views.link_slug, name="slug_path"), # New line
    path('comment/', views.add_comment, name="comment_path",),
]
