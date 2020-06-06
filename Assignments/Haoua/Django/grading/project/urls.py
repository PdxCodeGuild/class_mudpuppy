"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.http import JsonResponse 

def movie_fun(request):
    return JsonResponse({'messsage': 'I like the movie Django Unchained'})


def grading_fun(request):
    print(request.GET)
    grade_num = request.GET['grade']
    grade_num = int(grade_num)
    grade_let = ''

    if grade_num > 90:
        grade_let = 'A'
    elif grade_num > 80:
        grade_let = 'B'
    elif grade_num > 70:
        grade_let = 'C'
    elif grade_num > 60:
        grade_let = 'D'
    else:
        grade_let = 'F'
    return JsonResponse({'grade': grade_let})




urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', movie_fun),
    path('grading/', grading_fun),
]

