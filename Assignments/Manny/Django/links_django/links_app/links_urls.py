from django.urls import path
from . import views

app_name = "links_paths" # New line
urlpatterns = [
    path('list/', views.index, name="index_path"), # Changed line
    path('l/<str:in_slug>/', views.link_slug, name="slug_path"), # New line
    path('comment/', views.add_comment, name="comment_path",),
]
 {% for comment in comments_template %}
               <div class="comment-div">
                       {{ comment.text }} # Changed line
               </div>
               {% endfor %}
               <form method="POST" action="{% url 'links_paths:comment_path' %}"> # New line
                       {% csrf_token %} # New line
                       <input type="hidden" name="link" value="{{found_link_template.id}}"></input> # New line
                       <textarea placeholder="Type your comment here" name="commenttext"></textarea> # New line
                       <button>submit</button> # New line
               <form> # New line
        </body>
 </html>